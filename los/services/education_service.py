import logging
from io import BytesIO

import django.utils.timezone
import django.utils.timezone
from django.core.files.storage import default_storage

from los.status_code import get_response
from los.models.customer_education_model import Education
from los.los_dict import LosDictionary
from django.http import JsonResponse,HttpResponse
import datetime
from datetime import datetime,date
from los.custom_helper import get_value
logger = logging.getLogger("django")


def create_education_service(req_data):
    response_obj = None

    try:
        logger.info("request: %s", req_data)

        if req_data:
            education = None
            if hasattr(req_data, 'education'):
                education = req_data.education

                institute_id = get_value(education, 'institute_id')
                institute_name = get_value(education, 'first_name')
                course_id = get_value(education, 'course_id')
                course_name = get_value(education, 'course_name')
                stream_id = get_value(education, 'stream_id')
                stream_name = get_value(education, 'stream_name')
                logger.debug("stream_name_data: %s", stream_name)
                start_month_year = get_value(education, 'start_month_year')
                end_month_year = get_value(education, 'end_month_year')
                marks = get_value(education,'marks')
                max_marks = get_value(education,'max_marks')
                marks_type = get_value(education,'marks_type')
                duration_month=get_value(education,'duration_month')
                course_type=get_value(education,'course_type')
                status=get_value(education,'status')
                logger.debug("status_data: %d", status)

                # string validation
                


                # if date_of_birth:
                #     try:
                #         formated_dob = datetime.strptime(date_of_birth, "%Y-%m-%d").date()
                #         date_of_birth = formated_dob
                #     except ValueError:
                #         response_obj = get_response("check_dob")
                #         return response_obj
                

                current_time = django.utils.timezone.now()
                logger.debug("current_time india: %s", current_time)
                education = education(
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
                    duration_month=duration_month,
                    course_type=course_type,
                    status=1,
                    creation_date=current_time, creation_by="System")
                education.save()
                logger.info("inserted in education table")

                response_obj = get_response("success")
            else:
                response_obj = get_response("generic_error_1")
        else:
            response_obj = get_response("generic_error_1")

    except Exception as e:
        logger.exception("Exception: ")
        response_obj = get_response("generic_error_2")

    logger.info("response: %s", response_obj)
    return response_obj



def update_education(req_data):
    response_obj = None

    try:
        logger.info("request: %s", req_data)

        if req_data:
            education = None
            if hasattr(req_data, 'education'):
                education = req_data.education

                institute_id = get_value(education, 'institute_id')
                institute_name = get_value(education, 'first_name')
                course_id = get_value(education, 'course_id')
                course_name = get_value(education, 'course_name')
                stream_id = get_value(education, 'stream_id')
                stream_name = get_value(education, 'stream_name')
                logger.debug("stream_name_data: %s", stream_name)
                start_month_year = get_value(education, 'start_month_year')
                end_month_year = get_value(education, 'end_month_year')
                marks = get_value(education,'marks')
                max_marks = get_value(education,'max_marks')
                marks_type = get_value(education,'marks_type')
                duration_month=get_value(education,'duration_month')
                course_type=get_value(education,'course_type')
                status=get_value(education,'status')
                logger.debug("status_data: %d", status)

                # string validation
                


                # if date_of_birth:
                #     try:
                #         formated_dob = datetime.strptime(date_of_birth, "%Y-%m-%d").date()
                #         date_of_birth = formated_dob
                #     except ValueError:
                #         response_obj = get_response("check_dob")
                #         return response_obj
                

                current_time = django.utils.timezone.now()
                logger.debug("current_time india: %s", current_time)
                education = education(
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
                    duration_month=duration_month,
                    course_type=course_type,
                    status=1,
                    creation_date=current_time, creation_by="System")
                education.save()
                logger.info("inserted in education table")

                response_obj = get_response("success")
            else:
                response_obj = get_response("generic_error_1")
        else:
            response_obj = get_response("generic_error_1")

    except Exception as e:
        logger.exception("Exception: ")
        response_obj = get_response("generic_error_2")

    logger.info("response: %s", response_obj)
    return response_obj