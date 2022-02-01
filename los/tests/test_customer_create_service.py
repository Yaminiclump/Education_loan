from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from http import HTTPStatus
from django.urls import reverse
from django.conf import settings
from los.services import customer_create_service
from los.models.customer_auditlog_model import Customerauditlog
from los.models.customer_model import Customer
import django.utils.timezone
from los.los_dict import LosDictionary
import pytest
from types import SimpleNamespace
import json
import logging
from los.error_code import errors


logger = logging.getLogger("django")


@pytest.mark.django_db
class Test():

    def test_first_name_blank(self):
        data = {
            "customer": {
                "salutation": "mr",
                "first_name": " ",
                "middle_name": "abc",
                "last_name": "abc",
                "gender": "male",
                "date_of_birth": "2019-10-25",
                "relation_with_applicant": 0,
                "marital_status": "married",
                "father_first_name": "abc",
                "father_middle_name": "abc",
                "father_last_name": "abc",
                "mother_first_name": "abc",
                "mother_middle_name": "abc",
                "mother_last_name": "abc",
                "spouse_first_name": "abc",
                "spouse_middle_name": "abc",
                "spouse_last_name": "abc",
                "no_of_family_members": 4,
                "household_income_monthly": 5000
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = customer_create_service.create_service(data)
        logger.info("response: %s", response)
        assert response['error_code'] == errors.name['error_code']

    def test_salutation_invalid(self):
        data = {
            "customer": {
                "salutation": "MR",
                "first_name": "abc",
                "middle_name": "abc",
                "last_name": "abc",
                "gender": "male",
                "date_of_birth": "2019-10-25",
                "relation_with_applicant": 0,
                "marital_status": "married",
                "father_first_name": "abc",
                "father_middle_name": "abc",
                "father_last_name": "abc",
                "mother_first_name": "abc",
                "mother_middle_name": "abc",
                "mother_last_name": "abc",
                "spouse_first_name": "abc",
                "spouse_middle_name": "abc",
                "spouse_last_name": "abc",
                "no_of_family_members": 4,
                "household_income_monthly": 5000
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = customer_create_service.create_service(data)
        logger.info("response: %s", response)
        assert response['error_code'] == errors.salutation['error_code']

    def test_gender_invalid(self):
        data = {
            "customer": {
                "salutation": "mr",
                "first_name": "abc",
                "middle_name": "abc",
                "last_name": "abc",
                "gender": "mal",
                "date_of_birth": "2019-10-25",
                "relation_with_applicant": 0,
                "marital_status": "married",
                "father_first_name": "abc",
                "father_middle_name": "abc",
                "father_last_name": "abc",
                "mother_first_name": "abc",
                "mother_middle_name": "abc",
                "mother_last_name": "abc",
                "spouse_first_name": "abc",
                "spouse_middle_name": "abc",
                "spouse_last_name": "abc",
                "no_of_family_members": 4,
                "household_income_monthly": 5000
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = customer_create_service.create_service(data)
        logger.info("response: %s", response)
        assert response['error_code'] == errors.gender['error_code']

    def test_marital_status_invalid(self):
        data = {
            "customer": {
                "salutation": "mr",
                "first_name": "abc",
                "middle_name": "abc",
                "last_name": "abc",
                "gender": "male",
                "date_of_birth": "2019-10-25",
                "relation_with_applicant": 0,
                "marital_status": "mar",
                "father_first_name": "abc",
                "father_middle_name": "abc",
                "father_last_name": "abc",
                "mother_first_name": "abc",
                "mother_middle_name": "abc",
                "mother_last_name": "abc",
                "spouse_first_name": "abc",
                "spouse_middle_name": "abc",
                "spouse_last_name": "abc",
                "no_of_family_members": 4,
                "household_income_monthly": 5000
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = customer_create_service.create_service(data)
        logger.info("response: %s", response)
        assert response['error_code'] == errors.marital_status['error_code']

    def test_no_salutation_parameter(self):
        data = {
            "customer": {
                "first_name": "abc",
                "middle_name": "abc",
                "last_name": "abc",
                "gender": "mal",
                "date_of_birth": "2019-10-25",
                "relation_with_applicant": 0,
                "marital_status": "married",
                "father_first_name": "abc",
                "father_middle_name": "abc",
                "father_last_name": "abc",
                "mother_first_name": "abc",
                "mother_middle_name": "abc",
                "mother_last_name": "abc",
                "spouse_first_name": "abc",
                "spouse_middle_name": "abc",
                "spouse_last_name": "abc",
                "no_of_family_members": 4,
                "household_income_monthly": 5000
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = customer_create_service.create_service(data)
        logger.info("response: %s", response)
        assert response['error_code'] == errors.generic_error_1['error_code']

    def test_no_firstname_parameter(self):
        data = {
            "customer": {
                "salutation": "mr",
                "middle_name": "abc",
                "last_name": "abc",
                "gender": "male",
                "date_of_birth": "2019-10-25",
                "relation_with_applicant": 0,
                "marital_status": "married",
                "father_first_name": "abc",
                "father_middle_name": "abc",
                "father_last_name": "abc",
                "mother_first_name": "abc",
                "mother_middle_name": "abc",
                "mother_last_name": "abc",
                "spouse_first_name": "abc",
                "spouse_middle_name": "abc",
                "spouse_last_name": "abc",
                "no_of_family_members": 4,
                "household_income_monthly": 5000
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = customer_create_service.create_service(data)
        logger.info("response: %s", response)
        assert response['error_code'] == errors.generic_error_1['error_code']

    def test_no_middle_name_parameter(self):
        data = {
            "customer": {
                "salutation": "mr",
                "first_name": "abc",
                "last_name": "abc",
                "gender": "male",
                "date_of_birth": "2019-10-25",
                "relation_with_applicant": 0,
                "marital_status": "married",
                "father_first_name": "abc",
                "father_middle_name": "abc",
                "father_last_name": "abc",
                "mother_first_name": "abc",
                "mother_middle_name": "abc",
                "mother_last_name": "abc",
                "spouse_first_name": "abc",
                "spouse_middle_name": "abc",
                "spouse_last_name": "abc",
                "no_of_family_members": 4,
                "household_income_monthly": 5000
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = customer_create_service.create_service(data)
        logger.info("response: %s", response)
        assert response['error_code'] == errors.generic_error_1['error_code']

    def test_no_last_name_parameter(self):
        data = {
            "customer": {
                "salutation": "mr",
                "first_name": "abc",
                "middle_name": "abc",
                "gender": "male",
                "date_of_birth": "2019-10-25",
                "relation_with_applicant": 0,
                "marital_status": "married",
                "father_first_name": "abc",
                "father_middle_name": "abc",
                "father_last_name": "abc",
                "mother_first_name": "abc",
                "mother_middle_name": "abc",
                "mother_last_name": "abc",
                "spouse_first_name": "abc",
                "spouse_middle_name": "abc",
                "spouse_last_name": "abc",
                "no_of_family_members": 4,
                "household_income_monthly": 5000
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = customer_create_service.create_service(data)
        logger.info("response: %s", response)
        assert response['error_code'] == errors.generic_error_1['error_code']

    def test_no_gender_parameter(self):
        data = {
            "customer": {
                "salutation": "mr",
                "first_name": "abc",
                "middle_name": "abc",
                "last_name": "abc",
                "date_of_birth": "2019-10-25",
                "relation_with_applicant": 0,
                "marital_status": "married",
                "father_first_name": "abc",
                "father_middle_name": "abc",
                "father_last_name": "abc",
                "mother_first_name": "abc",
                "mother_middle_name": "abc",
                "mother_last_name": "abc",
                "spouse_first_name": "abc",
                "spouse_middle_name": "abc",
                "spouse_last_name": "abc",
                "no_of_family_members": 4,
                "household_income_monthly": 5000
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = customer_create_service.create_service(data)
        logger.info("response: %s", response)
        assert response['error_code'] == errors.generic_error_1['error_code']

    def test_no_dob_parameter(self):
        data = {
            "customer": {
                "salutation": "mr",
                "first_name": "abc",
                "middle_name": "abc",
                "last_name": "abc",
                "gender": "male",
                "relation_with_applicant": 0,
                "marital_status": "married",
                "father_first_name": "abc",
                "father_middle_name": "abc",
                "father_last_name": "abc",
                "mother_first_name": "abc",
                "mother_middle_name": "abc",
                "mother_last_name": "abc",
                "spouse_first_name": "abc",
                "spouse_middle_name": "abc",
                "spouse_last_name": "abc",
                "no_of_family_members": 4,
                "household_income_monthly": 5000
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = customer_create_service.create_service(data)
        logger.info("response: %s", response)
        assert response['error_code'] == errors.generic_error_1['error_code']

    def test_no_relation_with_applicant_parameter(self):
        data = {
            "customer": {
                "salutation": "mr",
                "first_name": "abc",
                "middle_name": "abc",
                "last_name": "abc",
                "gender": "male",
                "date_of_birth": "2019-10-25",
                "marital_status": "married",
                "father_first_name": "abc",
                "father_middle_name": "abc",
                "father_last_name": "abc",
                "mother_first_name": "abc",
                "mother_middle_name": "abc",
                "mother_last_name": "abc",
                "spouse_first_name": "abc",
                "spouse_middle_name": "abc",
                "spouse_last_name": "abc",
                "no_of_family_members": 4,
                "household_income_monthly": 5000
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = customer_create_service.create_service(data)
        logger.info("response: %s", response)
        assert response['error_code'] == errors.generic_error_1['error_code']

    def test_no_marital_status_parameter(self):
        data = {
            "customer": {
                "salutation": "mr",
                "first_name": "abc",
                "middle_name": "abc",
                "last_name": "abc",
                "gender": "male",
                "date_of_birth": "2019-10-25",
                "relation_with_applicant": 0,
                "father_first_name": "abc",
                "father_middle_name": "abc",
                "father_last_name": "abc",
                "mother_first_name": "abc",
                "mother_middle_name": "abc",
                "mother_last_name": "abc",
                "spouse_first_name": "abc",
                "spouse_middle_name": "abc",
                "spouse_last_name": "abc",
                "no_of_family_members": 4,
                "household_income_monthly": 5000
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = customer_create_service.create_service(data)
        logger.info("response: %s", response)
        assert response['error_code'] == errors.generic_error_1['error_code']

    def test_no_father_first_name_parameter(self):
        data = {
            "customer": {
                "salutation": "mr",
                "first_name": "abc",
                "middle_name": "abc",
                "last_name": "abc",
                "gender": "male",
                "date_of_birth": "2019-10-25",
                "relation_with_applicant": 0,
                "marital_status": "married",
                "father_middle_name": "abc",
                "father_last_name": "abc",
                "mother_first_name": "abc",
                "mother_middle_name": "abc",
                "mother_last_name": "abc",
                "spouse_first_name": "abc",
                "spouse_middle_name": "abc",
                "spouse_last_name": "abc",
                "no_of_family_members": 4,
                "household_income_monthly": 5000
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = customer_create_service.create_service(data)
        logger.info("response: %s", response)
        assert response['error_code'] == errors.generic_error_1['error_code']

    def test_no_father_middle_name_parameter(self):
        data = {
            "customer": {
                "salutation": "mr",
                "first_name": "abc",
                "middle_name": "abc",
                "last_name": "abc",
                "gender": "male",
                "date_of_birth": "2019-10-25",
                "relation_with_applicant": 0,
                "marital_status": "married",
                "father_first_name": "abc",
                "father_last_name": "abc",
                "mother_first_name": "abc",
                "mother_middle_name": "abc",
                "mother_last_name": "abc",
                "spouse_first_name": "abc",
                "spouse_middle_name": "abc",
                "spouse_last_name": "abc",
                "no_of_family_members": 4,
                "household_income_monthly": 5000
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = customer_create_service.create_service(data)
        logger.info("response: %s", response)
        assert response['error_code'] == errors.generic_error_1['error_code']

    def test_no_father_last_name_parameter(self):
        data = {
            "customer": {
                "salutation": "mr",
                "first_name": "abc",
                "middle_name": "abc",
                "last_name": "abc",
                "gender": "male",
                "date_of_birth": "2019-10-25",
                "relation_with_applicant": 0,
                "marital_status": "married",
                "father_first_name": "abc",
                "father_middle_name": "abc",
                "mother_first_name": "abc",
                "mother_middle_name": "abc",
                "mother_last_name": "abc",
                "spouse_first_name": "abc",
                "spouse_middle_name": "abc",
                "spouse_last_name": "abc",
                "no_of_family_members": 4,
                "household_income_monthly": 5000
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = customer_create_service.create_service(data)
        logger.info("response: %s", response)
        assert response['error_code'] == errors.generic_error_1['error_code']

    def test_no_mother_first_name_parameter(self):
        data = {
            "customer": {
                "salutation": "mr",
                "first_name": "abc",
                "middle_name": "abc",
                "last_name": "abc",
                "gender": "male",
                "date_of_birth": "2019-10-25",
                "relation_with_applicant": 0,
                "marital_status": "married",
                "father_first_name": "abc",
                "father_middle_name": "abc",
                "father_last_name": "abc",
                "mother_middle_name": "abc",
                "mother_last_name": "abc",
                "spouse_first_name": "abc",
                "spouse_middle_name": "abc",
                "spouse_last_name": "abc",
                "no_of_family_members": 4,
                "household_income_monthly": 5000
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = customer_create_service.create_service(data)
        logger.info("response: %s", response)
        assert response['error_code'] == errors.generic_error_1['error_code']

    def test_no_mother_middle_name_parameter(self):
        data = {
            "customer": {
                "salutation": "mr",
                "first_name": "abc",
                "middle_name": "abc",
                "last_name": "abc",
                "gender": "male",
                "date_of_birth": "2019-10-25",
                "relation_with_applicant": 0,
                "marital_status": "married",
                "father_first_name": "abc",
                "father_middle_name": "abc",
                "father_last_name": "abc",
                "mother_first_name": "abc",
                "mother_last_name": "abc",
                "spouse_first_name": "abc",
                "spouse_middle_name": "abc",
                "spouse_last_name": "abc",
                "no_of_family_members": 4,
                "household_income_monthly": 5000
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = customer_create_service.create_service(data)
        logger.info("response: %s", response)
        assert response['error_code'] == errors.generic_error_1['error_code']

    def test_no_mother_last_name_parameter(self):
        data = {
            "customer": {
                "salutation": "mr",
                "first_name": "abc",
                "middle_name": "abc",
                "last_name": "abc",
                "gender": "male",
                "date_of_birth": "2019-10-25",
                "relation_with_applicant": 0,
                "marital_status": "married",
                "father_first_name": "abc",
                "father_middle_name": "abc",
                "father_last_name": "abc",
                "mother_first_name": "abc",
                "mother_middle_name": "abc",
                "spouse_first_name": "abc",
                "spouse_middle_name": "abc",
                "spouse_last_name": "abc",
                "no_of_family_members": 4,
                "household_income_monthly": 5000
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = customer_create_service.create_service(data)
        logger.info("response: %s", response)
        assert response['error_code'] == errors.generic_error_1['error_code']

    def test_no_spouse_first_name_parameter(self):
        data = {
            "customer": {
                "salutation": "mr",
                "first_name": "abc",
                "middle_name": "abc",
                "last_name": "abc",
                "gender": "male",
                "date_of_birth": "2019-10-25",
                "relation_with_applicant": 0,
                "marital_status": "married",
                "father_first_name": "abc",
                "father_middle_name": "abc",
                "father_last_name": "abc",
                "mother_first_name": "abc",
                "mother_middle_name": "abc",
                "mother_last_name": "abc",
                "spouse_middle_name": "abc",
                "spouse_last_name": "abc",
                "no_of_family_members": 4,
                "household_income_monthly": 5000
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = customer_create_service.create_service(data)
        logger.info("response: %s", response)
        assert response['error_code'] == errors.generic_error_1['error_code']

    def test_no_spouse_middle_name_parameter(self):
        data = {
            "customer": {
                "salutation": "mr",
                "first_name": "abc",
                "middle_name": "abc",
                "last_name": "abc",
                "gender": "male",
                "date_of_birth": "2019-10-25",
                "relation_with_applicant": 0,
                "marital_status": "married",
                "father_first_name": "abc",
                "father_middle_name": "abc",
                "father_last_name": "abc",
                "mother_first_name": "abc",
                "mother_middle_name": "abc",
                "mother_last_name": "abc",
                "spouse_first_name": "abc",
                "spouse_last_name": "abc",
                "no_of_family_members": 4,
                "household_income_monthly": 5000
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = customer_create_service.create_service(data)
        logger.info("response: %s", response)
        assert response['error_code'] == errors.generic_error_1['error_code']

    def test_no_spouse_last_name_parameter(self):
        data = {
            "customer": {
                "salutation": "mr",
                "first_name": "abc",
                "middle_name": "abc",
                "last_name": "abc",
                "gender": "male",
                "date_of_birth": "2019-10-25",
                "relation_with_applicant": 0,
                "marital_status": "married",
                "father_first_name": "abc",
                "father_middle_name": "abc",
                "father_last_name": "abc",
                "mother_first_name": "abc",
                "mother_middle_name": "abc",
                "mother_last_name": "abc",
                "spouse_first_name": "abc",
                "spouse_middle_name": "abc",
                "no_of_family_members": 4,
                "household_income_monthly": 5000
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = customer_create_service.create_service(data)
        logger.info("response: %s", response)
        assert response['error_code'] == errors.generic_error_1['error_code']

    def test_no_family_members_no_parameter(self):
        data = {
            "customer": {
                "salutation": "mr",
                "first_name": "abc",
                "middle_name": "abc",
                "last_name": "abc",
                "gender": "male",
                "date_of_birth": "2019-10-25",
                "relation_with_applicant": 0,
                "marital_status": "married",
                "father_first_name": "abc",
                "father_middle_name": "abc",
                "father_last_name": "abc",
                "mother_first_name": "abc",
                "mother_middle_name": "abc",
                "mother_last_name": "abc",
                "spouse_first_name": "abc",
                "spouse_middle_name": "abc",
                "spouse_last_name": "abc",
                "household_income_monthly": 5000
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = customer_create_service.create_service(data)
        logger.info("response: %s", response)
        assert response['error_code'] == errors.generic_error_1['error_code']

    def test_no_household_income_monthly_parameter(self):
        data = {
            "customer": {
                "salutation": "mr",
                "first_name": "abc",
                "middle_name": "abc",
                "last_name": "abc",
                "gender": "male",
                "date_of_birth": "2019-10-25",
                "relation_with_applicant": 0,
                "marital_status": "married",
                "father_first_name": "abc",
                "father_middle_name": "abc",
                "father_last_name": "abc",
                "mother_first_name": "abc",
                "mother_middle_name": "abc",
                "mother_last_name": "abc",
                "spouse_first_name": "abc",
                "spouse_middle_name": "abc",
                "spouse_last_name": "abc",
                "no_of_family_members": 4,
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = customer_create_service.create_service(data)
        logger.info("response: %s", response)
        assert response['error_code'] == errors.generic_error_1['error_code']

    def test_no_customer_parameter(self):
        data = {

        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = customer_create_service.create_service(data)
        logger.info("response: %s", response)
        assert response['error_code'] == 20001

    def test_customer_create_service_success(self):
        data = {
            "customer": {
                "salutation": "mr",
                "first_name": "abc",
                "middle_name": "abc",
                "last_name": "abc",
                "gender": "male",
                "date_of_birth": "2019-10-25",
                "relation_with_applicant": 0,
                "marital_status": "married",
                "father_first_name": "abc",
                "father_middle_name": "abc",
                "father_last_name": "abc",
                "mother_first_name": "abc",
                "mother_middle_name": "abc",
                "mother_last_name": "abc",
                "spouse_first_name": "abc",
                "spouse_middle_name": "abc",
                "spouse_last_name": "abc",
                "no_of_family_members": 4,
                "household_income_monthly": 5000
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = customer_create_service.create_service(data)
        logger.info("response: %s", response)
        assert response['error_code'] == errors.success['error_code']
