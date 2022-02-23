import logging

import django.utils.timezone
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction

from los import constants
from los.constants import STATUS_ACTIVE, CREATION_BY, UPDATION_BY
from los.custom_helper import get_string_lower, get_value, validate_dict, set_db_attr_request, validate_numeric, validate_date_yyyymm, \
    validate_amount, InvalidInputException

from los.los_dict import LosDictionary
from los.models.education_model import Education, EducationLog
from los.models.customer_model import Customer
from los.models.empty_class import EmptyClass
from los.status_code import get_response, get_response_1, get_response_resp_var, Statuses

logger = logging.getLogger("django")


def validate_education(variables, counter):

    variables.institute_id = validate_numeric(variables.institute_id)
    if variables.institute_id is None or variables.institute_id == constants.ERROR_NUMERIC:
        logger.debug("institute_id is either None or invalid, institute_id: %s", variables.institute_id)
        raise InvalidInputException(get_response_resp_var(Statuses.invalid_institute_id, {"sequence": counter}))

    if variables.institute_id != 0:
        if variables.institute_name:
            raise InvalidInputException(get_response_resp_var(Statuses.invalid_institute_name, {"sequence": counter}))
    else:
        if not variables.institute_name:
            raise InvalidInputException(get_response_resp_var(Statuses.invalid_institute_name, {"sequence": counter}))

    variables.course_id = validate_numeric(variables.course_id)
    if variables.course_id is None or variables.course_id == constants.ERROR_NUMERIC:
        logger.debug("course_id is either None or invalid, course_id: %s", variables.course_id)
        raise InvalidInputException(get_response_resp_var(Statuses.invalid_course_id, {"sequence": counter}))

    if variables.course_id != 0:
        if variables.course_name:
            raise InvalidInputException(get_response_resp_var(Statuses.invalid_course_name, {"sequence": counter}))
    else:
        if not variables.course_name:
            raise InvalidInputException(get_response_resp_var(Statuses.invalid_course_name, {"sequence": counter}))

    variables.stream_id = validate_numeric(variables.stream_id)
    if variables.stream_id is None or variables.stream_id == constants.ERROR_NUMERIC:
        raise InvalidInputException(get_response_resp_var(Statuses.invalid_stream_id, {"sequence": counter}))
        return response_obj

    if variables.stream_id != 0:
        if variables.stream_name:
            raise InvalidInputException(get_response_resp_var(Statuses.invalid_stream_name, {"sequence": counter}))
    else:
        if not variables.stream_name:
            raise InvalidInputException(get_response_resp_var(Statuses.invalid_stream_name, {"sequence": counter}))

    variables.start_month_year = validate_date_yyyymm(variables.start_month_year)
    if variables.start_month_year == "ERROR_DATE":
        raise InvalidInputException(get_response_resp_var(Statuses.invalid_start_month_year, {"sequence": counter}))

    variables.end_month_year = validate_date_yyyymm(variables.end_month_year)
    if variables.end_month_year is None or variables.end_month_year == "ERROR_DATE":
        raise InvalidInputException(get_response_resp_var(Statuses.invalid_end_month_year, {"sequence": counter}))

    # validation
    variables.marks_type = validate_dict(variables.marks_type, LosDictionary.marks_type)
    if variables.marks_type is None or variables.marks_type == dict():
        raise InvalidInputException(get_response_resp_var(Statuses.invalid_marks_type, {"sequence": counter}))
    if variables.marks_type == LosDictionary.marks_type['percentage'] or variables.marks_type == LosDictionary.marks_type['percentile']:
        # marks should be in percentage or percentile
        variables.marks = validate_amount(variables.marks)
        if variables.marks is None or variables.marks == constants.ERROR_AMOUNT:
            raise InvalidInputException(get_response_resp_var(Statuses.invalid_marks, {"sequence": counter}))
    else:
        # marks should be in numeric format...
        variables.marks = validate_numeric(variables.marks)
        if variables.marks is None or variables.marks == constants.ERROR_NUMERIC:
            raise InvalidInputException(get_response_resp_var(Statuses.invalid_marks, {"sequence": counter}))

    variables.max_marks = validate_numeric(variables.max_marks)
    if variables.max_marks is None or variables.max_marks == constants.ERROR_NUMERIC:
        raise InvalidInputException(get_response_resp_var(Statuses.invalid_max_marks, {"sequence": counter}))

    variables.course_type = validate_dict(variables.course_type, LosDictionary.course_type)
    if variables.course_type is None or variables.course_type == dict():
        raise InvalidInputException(get_response_resp_var(Statuses.invalid_course_type, {"sequence": counter}))

    variables.duration_months = validate_numeric(variables.duration_months)
    if variables.duration_months == "ERROR_DATE":
        raise InvalidInputException(get_response_resp_var(Statuses.invalid_duration_months, {"sequence": counter}))


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
                education_list = get_value(customer, 'educations')

                if customer_id:
                    if type(customer_id) == int:
                        if not Customer.objects.filter(id=customer_id, status=1).exists():
                            response_obj = get_response(Statuses.customer_id_not_exist)
                            return response_obj
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

                                variables = EmptyClass()
                                variables.institute_id = get_value(education, "institute_id")
                                variables.institute_name = get_string_lower(education, "institute_name")
                                variables.course_id = get_value(education, "course_id")
                                logger.debug("variables.course_id: %s", variables.course_id)
                                variables.course_name = get_string_lower(education, "course_name")
                                variables.stream_id = get_value(education, "stream_id")
                                variables.stream_name = get_string_lower(education, "stream_name")
                                variables.start_month_year = get_string_lower(education, "start_month_year")
                                variables.end_month_year = get_string_lower(education, "end_month_year")
                                variables.marks = get_value(education, "marks")
                                variables.max_marks = get_value(education, "max_marks")
                                variables.marks_type = get_value(education, "marks_type")
                                variables.duration_months = get_value(education, "duration_months")
                                variables.course_type = get_string_lower(education, "course_type")
                                logger.info("marks_type: %s", variables.marks_type)

                                validate_education(variables, counter)
                                current_time = django.utils.timezone.now()
                                logger.debug("current_time india: %s", current_time)
                                education = Education(
                                    institute_id=variables.institute_id,
                                    institute_name=variables.institute_name,
                                    course_id=variables.course_id,
                                    course_name=variables.course_name,
                                    stream_id=variables.stream_id,
                                    stream_name=variables.stream_name,
                                    start_month_year=variables.start_month_year,
                                    end_month_year=variables.end_month_year,
                                    marks=variables.marks,
                                    max_marks=variables.max_marks,
                                    marks_type=variables.marks_type,
                                    duration_months=variables.duration_months,
                                    course_type=variables.course_type,
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
                education_list = get_value(customer, 'educations')

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
                                variables.education_id = get_value(education, "education_id")
                                variables.institute_id = get_value(education, "institute_id")
                                variables.institute_name = get_string_lower(education, "institute_name")
                                variables.course_id = get_value(education, "course_id")
                                variables.course_name = get_string_lower(education, "course_name")
                                variables.stream_id = get_value(education, "stream_id")
                                variables.stream_name = get_string_lower(education, "stream_name")
                                variables.start_month_year = get_string_lower(education, "start_month_year")
                                variables.end_month_year = get_string_lower(education, "end_month_year")
                                variables.marks = get_value(education, "marks")
                                variables.max_marks = get_value(education, "max_marks")
                                variables.marks_type = get_value(education, "marks_type")
                                variables.duration_months = get_value(education, "duration_months")
                                variables.course_type = get_string_lower(education, "course_type")

                                education_db = None
                                if variables.education_id:
                                    try:
                                        education_db = Education.objects.get(pk=variables.education_id, customer_id=customer_id, status=1)
                                    except ObjectDoesNotExist as e:
                                        raise InvalidInputException(get_response(Statuses.education_id_not_exist))
                                else:
                                    raise InvalidInputException(get_response(Statuses.education_id_not_provided))

                                validate_education(variables, counter)

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
                        response_obj = eval(str(e))
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


