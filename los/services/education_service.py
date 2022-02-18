import logging

import django.utils.timezone
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction

from los.constants import STATUS_ACTIVE, CREATION_BY, UPDATION_BY
from los.custom_helper import get_string_lower, get_value, validate_dict, validate_stu, validate_sub, \
    set_db_attr_request, InvalidInputException
from los.los_dict import LosDictionary
from los.models.education_model import Education, EducationLog
from los.models.customer_model import Customer
from los.models.empty_class import EmptyClass
from los.status_code import get_response, get_response_1, get_response_resp_var, Statuses
from los.views.education_view import education

logger = logging.getLogger("django")


def education_create_service(req_data):
    response_obj = None
    logger.info("service_request: %s", req_data)
    try:
        logger.info("request_service: %s", req_data)
        if req_data:
            customer = None
            if hasattr(req_data, 'customer'):
                customer = req_data.customer
                logger.info("customer_get: %s",req_data.customer)
                customer_id = get_value(customer, 'customer_id')
                education_list = get_value(education, 'education_list')

                if customer_id:
                    if type(customer_id) == int:
                        if not Customer.objects.filter(id=customer_id,status=1).exists():
                            response_obj = get_response(Statuses.customer_id_not_exist)
                            return response_obj
                        customer_id = customer_id
                    else:
                        response_obj = get_response(Statuses.customer_id_invalid_format)
                        return response_obj
                else:
                    response_obj = get_response(Statuses.customer_id_not_provided)
                    return response_obj
                education_insert_ids = []
                counter = 1

                if education_list:
                    try:
                        with transaction.atomic():

                            for education in education_list:
                                institute_id = get_string_lower(education, "institute_id")
                                institute_name = get_string_lower(education, "institute_name")
                                course_id = get_string_lower(education, "course_id")
                                course_name = get_value(education, "course_name")
                                stream_id = get_value(education, "stream_id")
                                stream_name = get_value(education, "stream_name")
                                start_month_year = get_value(education, "start_month_year")
                                end_month_year = get_value(education, "end_month_year")
                                marks = get_value(education, "marks")
                                max_marks = get_value(education, "max_marks")
                                marks_type = get_value(education, "marks_type")
                                duration_months = get_value(education, "duration_months")
                                course_type = get_value(education, "course_type")
                                logger.info("marks_type: %s", marks_type)

                                if marks_type is None:
                                    logger.debug("marks_type is None...")
                                    raise InvalidInputException(get_response_resp_var(Statuses.education_marks_type, {"sequence": counter}))

                                if institute_name is None:
                                    logger.debug("institute_name is None...")
                                    raise InvalidInputException(get_response_resp_var(Statuses.education_value, {"sequence": counter}))

                                # validation
                                marks_type = validate_dict(marks_type, LosDictionary.education_type)
                                if marks_type == dict():
                                    raise InvalidInputException(get_response_resp_var(Statuses.education_type, {"sequence": counter}))

                                if marks_type == LosDictionary.marks_type['']:
                                    check_stu = validate_stu(institute_id)
                                    if check_stu == str():
                                        raise InvalidInputException(get_response_resp_var(Statuses.student, {"sequence": counter}))

                                    if institute_name is None:
                                        raise InvalidInputException(get_response_resp_var(Statuses.education_institute_name, {"sequence": counter}))

                                if course_type == LosDictionary.education_type['sub']:
                                    check_sub = validate_sub(course_id)
                                    if check_sub == str():
                                        raise InvalidInputException(get_response_resp_var(Statuses.subject, {"sequence": counter}))

                                    if course_name is not None:
                                        raise InvalidInputException(get_response_resp_var(Statuses.education_course_name, {"sequence": counter}))

                                current_time = django.utils.timezone.now()
                                logger.debug("current_time india: %s", current_time)
                                education = Education(
                                    institute_id=institute_id,
                                    institute_name=institute_name,
                                    course_id=course_id,
                                    course_name=course_name,
                                    stream_id=stream_id,
                                    stream_name=stream_name,
                                    start_month_year=start_month_year,
                                    end_month_year=end_month_year,
                                    marks=marks,
                                    max_marks=max_marks,
                                    marks_type=marks_type,
                                    duration_months=duration_months,
                                    course_type=course_type,
                                    status=STATUS_ACTIVE,
                                    creation_date=current_time,
                                    creation_by=CREATION_BY,
                                    customer_id=customer_id)
                                education.save()

                                education_log = Education()
                                education_log.__dict__ = education.__dict__.copy()
                                education_log.id = None
                                education_log.education = education
                                education_log.save()

                                logger.info("finished eduction create...")
                                logger.debug("education_id: %s", education.id)

                                education_insert_ids.append(education.id)
                                counter = counter + 1

                                educations = EmptyClass()
                                educations = education_insert_ids
                            response_obj = get_response_1(Statuses.success, {"educations": education_insert_ids})
                    except InvalidInputException as e:
                        logger.debug("Exception...")
                        response_obj = str(e)
                else:
                    response_obj = get_response(Statuses.generic_error_1)
            else:
                response_obj = get_response(Statuses.generic_error_1)
        else:
            response_obj = get_response(Statuses.generic_error_1)
    except Exception as e:
        logger.exception("Exception: ")
        response_obj = get_response(Statuses.generic_error_2)
        logger.info("response: %s", response_obj)
    return response_obj


def education_update_service(req_data):
    response_obj = None
    try:
        logger.info("request_service: %s", req_data)
        if req_data:
            customer = None
            if hasattr(req_data, 'customer'):
                customer = req_data.customer
                customer_id = get_value(customer, 'customer_id')
                education_list = get_value(education, 'education_list')

                if customer_id:
                    if type(customer_id) == int:
                        if not Customer.objects.filter(id=customer_id,status=1).exists():
                            response_obj = get_response(Statuses.customer_id_not_exist)
                            return response_obj
                        customer_id = customer_id
                    else:
                        response_obj = get_response(Statuses.customer_id_invalid_format)
                        return response_obj
                else:
                    response_obj = get_response(Statuses.customer_id_not_provided)
                    return response_obj
                counter = 1
                if education_list:
                    try:
                        with transaction.atomic():
                            for education in education_list:
                                variables = EmptyClass()
                                # set_obj_attr_request(contact, variables)
                                variables.education_id = get_string_lower(education, "education_id")
                                variables.institute_id = get_string_lower(education, "institute_id")
                                variables.institute_name = get_string_lower(education, "institute_name")
                                variables.course_id = get_string_lower(education, "course_id")
                                variables.course_name = get_value(education, "course_name")
                                variables.stream_id = get_value(education, "stream_id")
                                variables.stream_name = get_value(education, "stream_name")
                                variables.start_month_year = get_value(education, "start_month_year")
                                variables.end_month_year = get_value(education, "end_month_year")
                                variables.marks = get_value(education, "marks")
                                variables.max_marks = get_value(education, "max_marks")
                                variables.marks_type = get_value(education, "marks_type")
                                variables.duration_months = get_value(education, "duration_months")
                                variables.course_type = get_value(education, "course_type")

                                education_db = None
                                if variables.education_id:
                                    try:
                                        education_db = Education.objects.get(pk=variables.education_id, customer_id=customer_id, status=1)
                                    except ObjectDoesNotExist as e:
                                        raise InvalidInputException(get_response(Statuses.education_id_not_exist))
                                else:
                                    raise InvalidInputException(get_response(Statuses.education_id_not_provided))

                                # validation
                                variables.type = validate_dict(variables.type, LosDictionary.education_type)
                                logger.info("type: %s", variables.type)
                                if variables.type == dict():
                                    raise InvalidInputException(get_response(Statuses.education_type, {"sequence": counter}))

                                if variables.type is None:
                                    variables.type = education_db.type

                                if variables.type == LosDictionary.education_type['stu']:
                                    check_stu = validate_stu(variables.institute_id)
                                    if check_stu == str():
                                        raise InvalidInputException(get_response_resp_var(Statuses.student, {"sequence": counter}))

                                    if variables.institute_name is None:
                                        raise InvalidInputException(get_response_resp_var(Statuses.education_institute_name, {"sequence": counter}))

                                if variables.type == LosDictionary.education_type['sub']:
                                    check_sub = validate_sub(variables.course_id)
                                    if check_sub== str():
                                        raise InvalidInputException(get_response_resp_var(Statuses.subject, {"sequence": counter}))

                                    if variables.course_type is not None:
                                        raise InvalidInputException(get_response_resp_var(Statuses.education_course_type, {"sequence": counter}))

                                set_db_attr_request(education_db, education, variables)
                                current_time = django.utils.timezone.now()
                                logger.debug("current_time india: %s", current_time)
                                education_db.updation_date = current_time
                                education_db.updation_by = UPDATION_BY
                                education_db.save()

                                education_log = EducationLog()
                                education_log.__dict__ = education_db.__dict__.copy()
                                education_log.id = None
                                education_log.education = education_db
                                education_log.creation_date = current_time
                                education_log.creation_by = CREATION_BY
                                education_log.save()
                                logger.info("finished education update service")
                                response_obj = get_response(Statuses.success)
                                counter = counter + 1

                    except InvalidInputException as e:
                        logger.debug("Exception...")
                        response_obj = str(e)
                else:
                    response_obj = get_response(Statuses.generic_error_1)
                    return response_obj
            else:
                response_obj = get_response(Statuses.generic_error_1)
        else:
            response_obj = get_response(Statuses.generic_error_1)
    except Exception as e:
        logger.exception("Exception: ")
        response_obj = get_response(Statuses.generic_error_2)
        logger.info("response: %s", response_obj)
    return response_obj

