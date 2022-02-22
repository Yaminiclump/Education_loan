import logging

import django.utils.timezone
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction

from los.constants import STATUS_ACTIVE, CREATION_BY, UPDATION_BY
from los.custom_helper import get_string_lower, get_value, validate_dict, set_db_attr_request, validate_numeric, validate_date_yyyymm, \
    InvalidInputException, get_income_value

from los.los_dict import LosDictionary
from los.models.education_model import Education, EducationLog
from los.models.customer_model import Customer
from los.models.empty_class import EmptyClass
from los.status_code import get_response, get_response_1, get_response_resp_var, Statuses

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

                                institute_id = validate_numeric(institute_id)
                                if institute_id is None or institute_id == int():
                                    raise InvalidInputException(get_response_resp_var(Statuses.invalid_institute_id, {"sequence": counter}))

                                if institute_id != 0:
                                    if institute_name:
                                        raise InvalidInputException(get_response_resp_var(Statuses.invalid_institute_name, {"sequence": counter}))
                                else:
                                    if not institute_name:
                                        raise InvalidInputException(get_response_resp_var(Statuses.invalid_institute_name, {"sequence": counter}))


                                course_id = validate_numeric(course_id)
                                if course_id is None or course_id == int():
                                    raise InvalidInputException(get_response_resp_var(Statuses.invalid_course_id, {"sequence": counter}))
                                    
                                if course_id != 0:
                                    if course_name:
                                        raise InvalidInputException(get_response_resp_var(Statuses.invalid_course_name, {"sequence": counter}))
                                else:
                                    if not course_name:
                                        raise InvalidInputException(get_response_resp_var(Statuses.invalid_course_name, {"sequence": counter}))        

                                
                                stream_id = validate_numeric(stream_id)
                                if stream_id is None or stream_id == int():
                                    raise InvalidInputException(get_response_resp_var(Statuses.invalid_stream_id, {"sequence": counter}))
                                    return response_obj

                                if stream_id != 0:
                                    if stream_name:
                                        raise InvalidInputException(get_response_resp_var(Statuses.invalid_stream_name, {"sequence": counter}))
                                else:
                                    if not stream_name:
                                        raise InvalidInputException(get_response_resp_var(Statuses.invalid_stream_name, {"sequence": counter}))
                                

                                start_month_year = validate_date_yyyymm(start_month_year)
                                if start_month_year == "ERROR_DATE":
                                    raise InvalidInputException(get_response_resp_var(Statuses.invalid_start_month_year, {"sequence": counter}))


                                end_month_year = validate_date_yyyymm(end_month_year)
                                if end_month_year is None or end_month_year == "ERROR_DATE":
                                    raise InvalidInputException(get_response_resp_var(Statuses.invalid_end_month_year, {"sequence": counter}))


                                # validation
                                marks_type = validate_dict(marks_type, LosDictionary.marks_type)
                                if marks_type is None or marks_type == dict():
                                    raise InvalidInputException(get_response_resp_var(Statuses.invalid_marks_type, {"sequence": counter}))
                                if marks_type == LosDictionary.marks_type['percentage'] or marks_type == LosDictionary.marks_type['percentile']:
                                    # marks should be in percentage or percentile
                                    marks = get_income_value(marks)
                                    if marks is None or marks == int():
                                        raise InvalidInputException(get_response_resp_var(Statuses.invalid_marks, {"sequence": counter}))
                                else:
                                    # marks should be in numeric format...
                                    marks = validate_numeric(marks)
                                    if marks is None or marks == int():
                                        raise InvalidInputException(get_response_resp_var(Statuses.invalid_marks, {"sequence": counter}))

                                max_marks = validate_numeric(marks)
                                if max_marks is None or max_marks == int():
                                    raise InvalidInputException(get_response_resp_var(Statuses.invalid_max_marks, {"sequence": counter}))


                                course_type = validate_dict(course_type, LosDictionary.course_type)
                                if course_type is None or course_type == dict():
                                    raise InvalidInputException(get_response_resp_var(Statuses.invalid_course_type, {"sequence": counter}))
                                if course_type == LosDictionary.course_type['full time'] or course_type == LosDictionary.course_type['part time']:
                                    duration_months = validate_numeric(duration_months)
                                    # if duration_months is None or duration_months == int():
                                    #     raise InvalidInputException(get_response_resp_var(Statuses.invalid_duration_months, {"sequence": counter}))
                                else:
                                    duration_months = validate_numeric(duration_months)
                                    if duration_months == "ERROR_DATE":
                                        raise InvalidInputException(get_response_resp_var(Statuses.invalid_duration_months, {"sequence": counter}))
                               


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
                                ducation_db = None
                                if variables.education_id:
                                        try:
                                            education_db = Education.objects.get(pk=variables.education_id, customer_id=customer_id, status=1)
                                        except ObjectDoesNotExist as e:
                                            raise InvalidInputException(get_response(Statuses.education_id_not_exist))
                                else:
                                    raise InvalidInputException(get_response(Statuses.education_id_not_provided))

                                # validation
                                if variables.institute_id is None:
                                    logger.debug("institute_id is None...")
                                    raise InvalidInputException(get_response_resp_var(Statuses.invalid_institute_id, {"sequence": counter}))

                                if variables.institute_name is None:
                                    logger.debug("institute_name is None...")
                                    raise InvalidInputException(get_response_resp_var(Statuses.invalid_institute_name, {"sequence": counter}))

                            
                                if variables.course_id is None:
                                    logger.debug("course_id is None...")
                                    raise InvalidInputException(get_response_resp_var(Statuses.invalid_course_id, {"sequence": counter}))

                                if variables.course_name is None:
                                    logger.debug("course_name is None...")
                                    raise InvalidInputException(get_response_resp_var(Statuses.invalid_course_name, {"sequence": counter}))
                                

                                if variables.stream_id is None:
                                    logger.debug("stream_id is None...")
                                    raise InvalidInputException(get_response_resp_var(Statuses.invalid_stream_id, {"sequence": counter}))

                                if variables.stream_name is None:
                                    logger.debug("stream_name is None...")
                                    raise InvalidInputException(get_response_resp_var(Statuses.invalid_stream_name, {"sequence": counter}))


                                if variables.start_month_year is None:
                                    logger.debug("start_month_year is None...")
                                    raise InvalidInputException(get_response_resp_var(Statuses.invalid_start_month_year, {"sequence": counter}))

                                if variables.end_month_year is None:
                                    logger.debug("end_month_year is None...")
                                    raise InvalidInputException(get_response_resp_var(Statuses.invalid_end_month_year, {"sequence": counter})) 

                                variables.marks_type = validate_dict(variables.marks_type, LosDictionary.marks_type)
                                logger.info("marks_type: %s", variables.marks_type)
                                if variables.marks_type == dict():
                                    raise InvalidInputException(get_response(Statuses.invalid_marks_type, {"sequence": counter}))    

                                if variables.marks == LosDictionary.marks_type['percentage']:
                                    check_percentage = validate_numeric(variables.marks)
                                    if check_percentage == int():
                                        raise InvalidInputException(get_response_resp_var(Statuses.invalid_marks, {"sequence": counter}))

                                    if variables.max_marks is None:
                                        raise InvalidInputException(get_response_resp_var(Statuses.invalid_max_marks, {"sequence": counter}))

                                if variables.marks == LosDictionary.marks_type['cgpa']:
                                    check_cgpa = validate_numeric(variables.marks)
                                    if check_cgpa == int():
                                        raise InvalidInputException(get_response_resp_var(Statuses.invalid_marks, {"sequence": counter}))

                                    if variables.max_marks is None:
                                        raise InvalidInputException(get_response_resp_var(Statuses.invalid_max_marks, {"sequence": counter}))  

                                if variables.marks == LosDictionary.marks_type['percentile']:
                                    check_percentile = validate_numeric(variables.marks)

                                    if check_percentile == int():
                                        raise InvalidInputException(get_response_resp_var(Statuses.invalid_marks, {"sequence": counter}))

                                    if variables.max_marks is None:
                                        raise InvalidInputException(get_response_resp_var(Statuses.invalid_max_marks, {"sequence": counter}))     

                                variables.course_type = validate_dict(variables.course_type, LosDictionary.course_type)
                                logger.info("course_type: %s", variables.course_type)
                                if variables.course_type == dict():
                                    raise InvalidInputException(get_response(Statuses.invalid_course_type, {"sequence": counter}))    

                                if variables.duration_months == LosDictionary.course_type['part time']:
                                    check_part_time = validate_numeric(variables.duration_months)
                                    if check_part_time == str():
                                        raise InvalidInputException(get_response_resp_var(Statuses.invalid_duration_months, {"sequence": counter}))

                                    if variables.duration_months is None:
                                        raise InvalidInputException(get_response_resp_var(Statuses.invalid_duration_months, {"sequence": counter}))
                                
                                if variables.duration_months == LosDictionary.course_type['full time']:
                                    check_full_time = validate_numeric(variables.duration)
                                    if check_full_time == str():
                                        raise InvalidInputException(get_response_resp_var(Statuses.invalid_duration_months, {"sequence": counter}))

                                    if variables.duration_months is None:
                                        raise InvalidInputException(get_response_resp_var(Statuses.invalid_duration_months, {"sequence": counter}))

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


