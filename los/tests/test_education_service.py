import json
import logging
from types import SimpleNamespace

import django.utils.timezone
import django.utils.timezone
import pytest

from los.models.customer_model import Customer
from los.models.education_model import Education
from los.services.education_service import education_create_service, education_update_service
from los.status_code import Statuses

logger = logging.getLogger("django")


def customer_insert():
    current_time = django.utils.timezone.now()
    logger.debug("current_time india: %s", current_time)
    create_customer = Customer(
        salutation=1,
        first_name="abc",
        middle_name="",
        last_name="",
        gender=1,
        date_of_birth="2019-10-25",
        relation_with_applicant=0,
        marital_status=1,
        father_first_name="abc",
        father_middle_name="abc",
        father_last_name="",
        mother_first_name="",
        mother_middle_name="",
        mother_last_name="",
        spouse_first_name="",
        spouse_middle_name="",
        spouse_last_name="",
        no_of_family_members=4,
        household_income_monthly=5000,
        status=1,
        creation_date=current_time,
        creation_by="System"
    )
    create_customer.save()
    return create_customer


def education_insert(customer_id):
    current_time = django.utils.timezone.now()
    logger.debug("current_time india: %s", current_time)
    create_education = Education(
        institute_id= 1,
        institute_name= "string",
        course_id= 0,
        course_name= "string",
        stream_id= 0,
        stream_name= "string",
        start_month_year= "2018-06-11",
        end_month_year= "2022-06-10",
        marks= 10,
        max_marks= 0,
        marks_type= "string",
        duration_months= 0,
        course_type= "string",
        creation_date=current_time,
        creation_by="System",
        customer_id=customer_id
    )
    create_education.save()
    return create_education


def marks_type_insert(customer_id):
    current_time = django.utils.timezone.now()
    logger.debug("current_time india: %s", current_time)
    marks_type_insert = Education(
        marks_type= "string",
        marks= 10,
        max_marks= 0,
        status=1,
        creation_date=current_time,
        creation_by="System",
        customer_id=customer_id
    )
    marks_type_insert.save()
    return marks_type_insert


def course_type_insert(customer_id):
    current_time = django.utils.timezone.now()
    logger.debug("current_time india: %s", current_time)
    course_type_insert = Education(
        course_type= "string",
        duration_months= 0,
        status=1,
        creation_date=current_time,
        creation_by="System",
        customer_id=customer_id
    )
    course_type_insert.save()
    return course_type_insert

@pytest.mark.django_db
class TestEducationCreate:

    def test_customer_id_not_exist(self):
        data = {
            "customer": {
                "customer_id": 10000,
                "educations": [
                    {
                        "institute_id": "1",
                        "institute_name": "string",
                        "course_id": "0",
                        "course_name": "string",
                        "stream_id": "0",
                        "stream_name": "string",
                        "start_month_year": "2018-06-10",
                        "end_month_year": "2022-06-10",
                        "marks": "10",
                        "max_marks": "0",
                        "marks_type": "string",
                        "duration_months": "0",
                        "course_type": "string"
                    }
                ]

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.customer_id_not_exist['status_code']

    def test_customer_id_invalid_format(self):
        data = {
            "customer": {
                "customer_id": "10000",
                "educations": [
                    {
                        "institute_id": "1",
                        "institute_name": "string",
                        "course_id": "0",
                        "course_name": "string",
                        "stream_id": "0",
                        "stream_name": "string",
                        "start_month_year": "2018-06-10",
                        "end_month_year": "2022-06-10",
                        "marks": "10",
                        "max_marks": "0",
                        "marks_type": "string",
                        "duration_months": "0",
                        "course_type": "string"
                    }
                ]

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.customer_id_invalid_format['status_code']

    def test_customer_id_not_provided(self):
        data = {
            "customer": {
                "educations": [
                    {
                        "institute_id": "1",
                        "institute_name": "string",
                        "course_id": "0",
                        "course_name": "string",
                        "stream_id": "0",
                        "stream_name": "string",
                        "start_month_year": "2018-06-10",
                        "end_month_year": "2022-06-10",
                        "marks": "10",
                        "max_marks": "0",
                        "marks_type": "string",
                        "duration_months": "0",
                        "course_type": "string"
                    }
                ]

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.customer_id_not_provided['status_code']

    def test_institute_id_parameter(self):
        create_customer = customer_insert()

        data = {
            "customer": {
                "customer_id": create_customer.id,
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.generic_error_1['status_code']

    def test_institute_id_parameter_blank(self):
        create_customer = customer_insert()

        data = {
            "customer": {
                "customer_id": create_customer.id,
                "institute_id": [],
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.generic_error_1['status_code']

    def test_no_data_institute_id_parameter(self):
        create_customer = customer_insert()

        data = {
            "customer": {
                "customer_id": create_customer.id,
                "institute_id": [
                    {}
                ],
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.generic_error_1['status_code']

    def test_institute_name_parameter(self):
        create_customer = customer_insert()

        data = {
            "customer": {
                "customer_id": create_customer.id,
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.generic_error_1['status_code']

    def test_institute_name_parameter_blank(self):
        create_customer = customer_insert()

        data = {
            "customer": {
                "customer_id": create_customer.id,
                "institute_name": [],
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.generic_error_1['status_code']

    def test_no_data_institute_name_parameter(self):
        create_customer = customer_insert()

        data = {
            "customer": {
                "customer_id": create_customer.id,
                "institute_name": [
                    {}
                ],
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.generic_error_1['status_code']        

    def test_course_id_parameter(self):
        create_customer = customer_insert()

        data = {
            "customer": {
                "customer_id": create_customer.id,
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.generic_error_1['status_code']

    def test_course_id_parameter_blank(self):
        create_customer = customer_insert()

        data = {
            "customer": {
                "customer_id": create_customer.id,
                "course_id": [],
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.generic_error_1['status_code']

    def test_no_data_course_id_parameter(self):
        create_customer = customer_insert()

        data = {
            "customer": {
                "customer_id": create_customer.id,
                "course_id": [
                    {}
                ],
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.generic_error_1['status_code']

    def test_course_name_parameter(self):
        create_customer = customer_insert()

        data = {
            "customer": {
                "customer_id": create_customer.id,
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.generic_error_1['status_code']

    def test_course_name_parameter_blank(self):
        create_customer = customer_insert()

        data = {
            "customer": {
                "customer_id": create_customer.id,
                "course_name": [],
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.generic_error_1['status_code']

    def test_no_data_course_name_parameter(self):
        create_customer = customer_insert()

        data = {
            "customer": {
                "customer_id": create_customer.id,
                "course_name": [
                    {}
                ],
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.generic_error_1['status_code']

    def test_stream_id_parameter(self):
        create_customer = customer_insert()

        data = {
            "customer": {
                "customer_id": create_customer.id,
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.generic_error_1['status_code']

    def test_stream_id_parameter_blank(self):
        create_customer = customer_insert()

        data = {
            "customer": {
                "customer_id": create_customer.id,
                "stream_id": [],
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.generic_error_1['status_code']

    def test_no_data_stream_id_parameter(self):
        create_customer = customer_insert()

        data = {
            "customer": {
                "customer_id": create_customer.id,
                "stream_id": [
                    {}
                ],
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.generic_error_1['status_code']

    def test_stream_name_parameter(self):
        create_customer = customer_insert()

        data = {
            "customer": {
                "customer_id": create_customer.id,
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.generic_error_1['status_code']

    def test_stream_name_parameter_blank(self):
        create_customer = customer_insert()

        data = {
            "customer": {
                "customer_id": create_customer.id,
                "stream_name": [],
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.generic_error_1['status_code']

    def test_no_data_stream_name_parameter(self):
        create_customer = customer_insert()

        data = {
            "customer": {
                "customer_id": create_customer.id,
                "stream_name": [
                    {}
                ],
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.generic_error_1['status_code']

    def test_start_month_year_parameter(self):
        create_customer = customer_insert()

        data = {
            "customer": {
                "customer_id": create_customer.id,
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.generic_error_1['status_code']

    def test_start_month_year_parameter_blank(self):
        create_customer = customer_insert()

        data = {
            "customer": {
                "customer_id": create_customer.id,
                "start_month_year": [],
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.generic_error_1['status_code']

    def test_no_data_start_month_year_parameter(self):
        create_customer = customer_insert()

        data = {
            "customer": {
                "customer_id": create_customer.id,
                "start_month_year": [
                    {}
                ],
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.generic_error_1['status_code']

    def test_end_month_year_parameter(self):
        create_customer = customer_insert()

        data = {
            "customer": {
                "customer_id": create_customer.id,
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.generic_error_1['status_code']

    def test_start_end_year_parameter_blank(self):
        create_customer = customer_insert()

        data = {
            "customer": {
                "customer_id": create_customer.id,
                "start_end_year": [],
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.generic_error_1['status_code']

    def test_no_data_end_month_year_parameter(self):
        create_customer = customer_insert()

        data = {
            "customer": {
                "customer_id": create_customer.id,
                "start_end_year": [
                    {}
                ],
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.generic_error_1['status_code']

    def test_marks_type_parameter(self):
        create_customer = customer_insert()

        data = {
            "customer": {
                "customer_id": create_customer.id,
                "educations": [
                    {
                        "marks_type": "percentage",
                        "marks": 75,
                        "max_marks": 0
                    },
                    {
                        "marks_type": "percentile",
                        "marks": 80
                    }
                ]

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.invalid_marks_type['status_code']

    def test_marks_type_invalid(self):
        create_customer = customer_insert()

        data = {
            "customer": {
                "customer_id": create_customer.id,
                "educations": [
                    {
                        "marks_type": "percentage",
                        "marks": 75,
                        "max_marks": 0
                    }
                ]
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.invalid_marks_type['status_code']

    def test_no_data_marks_type_parameter(self):
        create_customer = customer_insert()

        data = {
            "customer": {
                "customer_id": create_customer.id,
                "educations": [
                    {
                        "marks_type": "percentage",
                        "marks": 75,
                        "max_marks": 0
                    },
                    {
                        "marks_type": "percentile",
                        "marks": 80
                    }
                ]
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.invalid_marks_type['status_code']

    def test_course_type_parameter(self):
        create_customer = customer_insert()

        data = {
            "customer": {
                "customer_id": create_customer.id,
                "educations": [
                    {
                        "course_type": "part_time",
                        "duration_months": "0"
                    },
                    {
                        "course_type": "full_time",
                        "duration_months": "0"
                    }
                ]

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.invalid_course_type['status_code']

    def test_course_type_invalid(self):
        create_customer = customer_insert()

        data = {
            "customer": {
                "customer_id": create_customer.id,
                "educations": [
                    {
                        "course_type": "part_time",
                        "duration_months": "0"
                    }
                ]
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.invalid_course_type['status_code']

    def test_no_data_course_type_parameter(self):
        create_customer = customer_insert()

        data = {
            "customer": {
                "customer_id": create_customer.id,
                "educations": [
                    {
                        "course_type": "part_time",
                        "duration_months": "0"
                    },
                    {
                        "course_type": "full_time",
                        "duration_months": "0"
                    }
                ]
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.invalid_course_type['status_code']

    
    def test_no_customer_parameter(self):
        data = {

        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.generic_error_1['status_code']

    def test_data_null(self):
        data = None
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.generic_error_1['status_code']

    def test_education_success_with_institute_id(self):
        create_customer = customer_insert()

        data = {
            "customer": {
                "customer_id": create_customer.id,
                "educations": [
                    {
                        "institute_id": "1"
                    }
                ]
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_education_success_with_institute_name(self):
        create_customer = customer_insert()

        data = {
            "customer": {
                "customer_id": create_customer.id,
                "educations": [
                    {
                        "institute_name": "fdyjhh"
                    }
                ]
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_education_success_with_course_id(self):
        create_customer = customer_insert()

        data = {
            "customer": {
                "customer_id": create_customer.id,
                "educations": [
                    {
                        "course_id": "0"
                    }
                ]
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_education_success_with_course_name(self):
        create_customer = customer_insert()

        data = {
            "customer": {
                "customer_id": create_customer.id,
                "educations": [
                    {
                        "course_name": "string"
                    }
                ]
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_education_success_with_stream_id(self):
        create_customer = customer_insert()

        data = {
            "customer": {
                "customer_id": create_customer.id,
                "educations": [
                    {
                        "stream_id": "0"
                    }
                ]
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_education_success_with_stream_name(self):
        create_customer = customer_insert()

        data = {
            "customer": {
                "customer_id": create_customer.id,
                "educations": [
                    {
                        "stream_name": "string"
                    }
                ]
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_education_success_with_start_month_year(self):
        create_customer = customer_insert()

        data = {
            "customer": {
                "customer_id": create_customer.id,
                "educations": [
                    {
                        "start_month_year": "2018-06-10"
                    }
                ]
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_education_success_with_end_month_year(self):
        create_customer = customer_insert()

        data = {
            "customer": {
                "customer_id": create_customer.id,
                "educations": [
                    {
                        "end_month_year": "2022-06-10"
                    }
                ]
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']
        
    def test_contact_success_with_marks_type(self):
        create_customer = customer_insert()

        data = {
            "customer": {
                "customer_id": create_customer.id,
                "educations": [
                    {
                        "marks_type": "cgpa",
                        "marks": "7.5",
                        "max_marks": "0"
                    }
                ]
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_contact_success_with_course_type(self):
        create_customer = customer_insert()

        data = {
            "customer": {
                "customer_id": create_customer.id,
                "educations": [
                    {
                        "course_type": "part time",
                        "duration_months": "0"
                    }
                ]
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']                                                    

    def test_education_success(self):
        create_customer = customer_insert()

        data = {
            "customer": {
                "customer_id": create_customer.id,
                "educations": [
                    {
                        "institute_id": "1",
                        "institute_name": "string",
                        "course_id": "0",
                        "course_name": "string",
                        "stream_id": "0",
                        "stream_name": "string",
                        "start_month_year": "2018-06-10",
                        "end_month_year": "2022-06-10",
                        "marks": "10",
                        "max_marks": "0",
                        "marks_type": "string",
                        "duration_months": "0",
                        "course_type": "string"
                    },
                    {
                        "marks_type": "cgpa",
                        "marks": "7.5",
                        "max_marks": "0"
                    },

                    {
                        "course_type": "part time",
                        "duration_months": "0"  
                    }
            
                ]

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_exception(self, django_db_blocker):
        create_customer = customer_insert()

        data = {
            "customer": {
                "customer_id": create_customer.id,
                "educations": [
                    {
                        "institute_id": "1",
                        "institute_name": "string",
                        "course_id": "0",
                        "course_name": "string",
                        "stream_id": "0",
                        "stream_name": "string",
                        "start_month_year": "2018-06-10",
                        "end_month_year": "2022-06-10",
                        "marks": "10",
                        "max_marks": "0",
                        "marks_type": "string",
                        "duration_months": "0",
                        "course_type": "string"
                    }
                ]

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        with django_db_blocker.block():
            response_obj = education_create_service(data)
        assert response_obj["status"] == Statuses.generic_error_2["status_code"]


@pytest.mark.django_db
class TestEducationUpdate:

    def test_customer_id_not_exist(self):
        create_customer = customer_insert()

        create_education = education_insert(create_customer.id)
        create_marks_type = marks_type_insert(create_customer.id)
        create_course_type = course_type_insert(create_customer.id)
        data = {
            "customer": {
                "customer_id": 10000,
                "educations": [
                    {
                        "education_id": create_education.id,
                        "institute_id": 1,
                        "institute_name": "string",
                        "course_id": 0,
                        "course_name": "string",
                        "stream_id": 0,
                        "stream_name": "string",
                        "start_month_year": "2018-06-10",
                        "end_month_year": "2022-06-10",
                        "marks": 10,
                        "max_marks": 0,
                        "marks_type": "string",
                        "duration_months": 0,
                        "course_type": "string"
                    },
                    {
                        "education_id": create_marks_type.id,
                        "marks_type": "string",
                        "marks": 10,
                        "max_marks": 0
                    },
                    {
                        "education_id": create_course_type.id,
                        "course_type": "string",
                        "duration_months": 0
                    }
                ]

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_update_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.customer_id_not_exist['status_code']

    def test_customer_id_invalid_format(self):
        create_customer = customer_insert()

        create_education = education_insert(create_customer.id)
        create_marks_type = marks_type_insert(create_customer.id)
        create_course_type = course_type_insert(create_customer.id)
        data = {
            "customer": {
                "customer_id": "10000",
                "educations": [
                    {
                        "education_id": create_education.id,
                        "institute_id": "1",
                        "institute_name": "string",
                        "course_id": "0",
                        "course_name": "string",
                        "stream_id": "0",
                        "stream_name": "string",
                        "start_month_year": "2018-06-10",
                        "end_month_year": "2022-06-10",
                        "marks": "10",
                        "max_marks": "0",
                        "marks_type": "string",
                        "duration_months": "0",
                        "course_type": "string"
                    },
                    {
                        "education_id": create_marks_type.id,
                        "marks_type": "string",
                        "marks": "10",
                        "max_marks": "0"
                    },
                    {
                        "education_id": create_course_type.id,
                        "course_type": "string",
                        "duration_months": "0"
                    }
                ]

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_update_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.customer_id_invalid_format['status_code']

    def test_customer_id_not_provided(self):
        create_customer = customer_insert()

        create_education = education_insert(create_customer.id)
        create_marks_type = marks_type_insert(create_customer.id)
        create_course_type = course_type_insert(create_customer.id) 
        data = {
            "customer": {
                "educations": [
                    {
                        "education_id": create_education.id,
                        "institute_id": "1",
                        "institute_name": "string",
                        "course_id": "0",
                        "course_name": "string",
                        "stream_id": "0",
                        "stream_name": "string",
                        "start_month_year": "2018-06-10",
                        "end_month_year": "2022-06-10",
                        "marks": "10",
                        "max_marks": "0",
                        "marks_type": "string",
                        "duration_months": "0",
                        "course_type": "string"
                    },
                    {
                        "education_id": create_marks_type.id,
                        "marks_type": "string",
                        "marks": "10",
                        "max_marks": "0"
                    },
                    {
                        "education_id": create_course_type.id,
                        "course_type": "string",
                        "duration_months": "0"
                    }
                ]

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_update_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.customer_id_not_provided['status_code']

    def test_no_education_parameter(self):
        create_customer = customer_insert()
        data = {
            "customer": {
                "customer_id": create_customer.id,
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_update_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.generic_error_1['status_code']

    def test_education_parameter_blank(self):
        create_customer = customer_insert()
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "educations": []

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_update_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.generic_error_1['status_code']

    def test_no_customer_education_id(self):
        create_customer = customer_insert()
        create_education = education_insert(create_customer.id)
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "educations": [
                    {
                        "education_id": create_education.id,
                        "institute_id": "1",
                        "institute_name": "string",
                        "course_id": "0",
                        "course_name": "string",
                        "stream_id": "0",
                        "stream_name": "string",
                        "start_month_year": "2018-06-10",
                        "end_month_year": "2022-06-10",
                        "marks": "10",
                        "max_marks": "0",
                        "marks_type": "string",
                        "duration_months": "0",
                        "course_type": "string"
                    },
                    {
                    }
                ]

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_update_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.education_id_not_provided['status_code']

    def test_education_id_not_exist(self):
        create_customer = customer_insert()
        create_education = education_insert(create_customer.id)
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "educations": [
                    {
                        "education_id": create_education.id,
                        "institute_id": "1",
                        "institute_name": "string",
                        "course_id": "0",
                        "course_name": "string",
                        "stream_id": "0",
                        "stream_name": "string",
                        "start_month_year": "2018-06-10",
                        "end_month_year": "2022-06-10",
                        "marks": "10",
                        "max_marks": "0",
                        "marks_type": "string",
                        "duration_months": "0",
                        "course_type": "string"
                    },
                    {
                        "education_id": 10000

                    }
                ]

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_update_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.education_id_not_exist['status_code']

    def test_education_id_invalid(self):
        create_customer = customer_insert()
        create_education = education_insert(create_customer.id)
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "educations": [
                    {
                        "education_id": create_education.id,
                        "institute_id": "1",
                        "institute_name": "string",
                        "course_id": "0",
                        "course_name": "string",
                        "stream_id": "0",
                        "stream_name": "string",
                        "start_month_year": "2018-06-10",
                        "end_month_year": "2022-06-10",
                        "marks": "10",
                        "max_marks": "0",
                        "marks_type": "string",
                        "duration_months": "0",
                        "course_type": "string"
                    },
                    {
                        "institute_id": "10000"
                    }
                ]

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_update_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.education_id_not_exist['status_code']

    def test_marks_type_parameter(self):
        create_customer = customer_insert()

        create_education = education_insert(create_customer.id)
        create_marks_type = marks_type_insert(create_customer.id)
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "educations": [
                    {
                        "education_id": create_education.id,
                        "institute_id": 1,
                        "institute_name": "string",
                        "course_id": 0,
                        "course_name": "string",
                        "stream_id": 0,
                        "stream_name": "string",
                        "start_month_year": 2018-11-10,
                        "end_month_year": 2022-11-10,
                        "marks": 10,
                        "max_marks": 0,
                        "marks_type": "string",
                        "duration_months": 0,
                        "course_type": "string"
                    },
                    {
                        "education_id": create_marks_type.id,
                        "marks_type": "cgpa",
                        "marks": 7.5,
                        "max_marks": "0"
                    }
                ]

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_update_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.invalid_marks_type['status_code']

    def test_marks_type_invalid(self):
        create_customer = customer_insert()

        create_education = education_insert(create_customer.id)
        create_marks_type = marks_type_insert(create_customer.id)
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "educations": [
                    {
                        "education_id": create_education.id,
                        "institute_id": "1",
                        "institute_name": "string",
                        "course_id": "0",
                        "course_name": "string",
                        "stream_id": "0",
                        "stream_name": "string",
                        "start_month_year": "2018-06-10",
                        "end_month_year": "2022-06-10",
                        "marks": "10",
                        "max_marks": "0",
                        "marks_type": "string",
                        "duration_months": "0",
                        "course_type": "string"
                    },
                    {
                        "education_id": create_marks_type.id,
                        "marks_type": "fasfa",
                        "marks": "7.5",
                        "max_marks": "0"
                    }
                ]

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_update_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.invalid_marks_type['status_code']

    def test_course_type_parameter(self):
        create_customer = customer_insert()

        create_education = education_insert(create_customer.id)
        create_course_type = course_type_insert(create_customer.id)
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "educations": [
                    {
                        "education_id": create_education.id,
                        "institute_id": "1",
                        "institute_name": "string",
                        "course_id": "0",
                        "course_name": "string",
                        "stream_id": "0",
                        "stream_name": "string",
                        "start_month_year": "2018-06-10",
                        "end_month_year": "2022-06-10",
                        "marks": "10",
                        "max_marks": "0",
                        "marks_type": "string",
                        "duration_months": "0",
                        "course_type": "string"
                    },
                    {
                        "education_id": create_course_type.id,
                        "course_type": "part time",
                        "duration_months": "0"
                    }
                ]

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_update_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.invalid_course_type['status_code']

    def test_course_type_invalid(self):
        create_customer = customer_insert()

        create_education = education_insert(create_customer.id)
        create_course_type = course_type_insert(create_customer.id)
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "educations": [
                    {
                        "education_id": create_education.id,
                        "institute_id": "1",
                        "institute_name": "string",
                        "course_id": "0",
                        "course_name": "string",
                        "stream_id": "0",
                        "stream_name": "string",
                        "start_month_year": "2018-06-10",
                        "end_month_year": "2022-06-10",
                        "marks": "10",
                        "max_marks": "0",
                        "marks_type": "string",
                        "duration_months": "0",
                        "course_type": "string"
                    },
                    {
                        "education_id": create_course_type.id,
                        "course_type": "fasfa",
                        "duration_months": "0"
                    }
                ]

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_update_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.invalid_course_type['status_code']     


    # 
    def test_no_customer_parameter(self):
        data = {
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_update_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.generic_error_1['status_code']

    def test_data_null(self):
        data = None
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_update_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.generic_error_1['status_code']

    def test_education_update_success(self):
        create_customer = customer_insert()
        create_education = education_insert(create_customer.id)
        create_marks_type = marks_type_insert(create_customer.id)
        create_course_type = course_type_insert(create_customer.id)
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "educations": [
                    {
                        "education_id": create_education.id,
                        "institute_id": "1",
                        "institute_name": "string",
                        "course_id": "0",
                        "course_name": "string",
                        "stream_id": "0",
                        "stream_name": "string",
                        "start_month_year": "2018-06-10",
                        "end_month_year": "2022-06-10",
                        "marks": "10",
                        "max_marks": "0",
                        "marks_type": "string",
                        "duration_months": "0",
                        "course_type": "string"
                    },
                    {
                        "education_id": create_marks_type.id,
                        "marks_type": "cgpa",
                        "marks": "7.5",
                        "max_marks": "0"

                    },
                    {
                        "education_id": create_course_type.id,
                        "course_type": "part time",
                        "duration_months": "0"
                    }
                ]

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = education_update_service(data)
        logger.info("response: %s", response)
        assert response["status"] == Statuses.success["status_code"]

    def test_exception(self, django_db_blocker):
        create_customer = customer_insert()

        create_education = education_insert(create_customer.id)
        create_marks_type = marks_type_insert(create_customer.id)
        create_course_type = course_type_insert(create_customer.id)
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "educations": [
                    {
                        "education_id": create_education.id,
                        "institute_id": "1",
                        "institute_name": "string",
                        "course_id": "0",
                        "course_name": "string",
                        "stream_id": "0",
                        "stream_name": "string",
                        "start_month_year": "2018-06-10",
                        "end_month_year": "2022-06-10",
                        "marks": "10",
                        "max_marks": "0",
                        "marks_type": "string",
                        "duration_months": "0",
                        "course_type": "string"
                    },
                    {
                        "education_id": create_marks_type.id,
                        "marks_type": "cgpa",
                        "marks": "7.5",
                        "max_marks": "0"
                    },
                    {
                        "education_id": create_course_type.id,
                        "course_type": "part time",
                        "duration_months": "0"
                    }
                ]

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        with django_db_blocker.block():
            response_obj = education_update_service(data)
        assert response_obj["status"] == Statuses.generic_error_2["status_code"]
