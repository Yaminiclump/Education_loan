from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from http import HTTPStatus
from django.urls import reverse
from django.conf import settings
from los.services import customer_service
from los.services.customer_service import create_service,update_customer
from los.models.customer_auditlog_model import Customerauditlog
from los.models.customer_model import Customer
import django.utils.timezone
from los.los_dict import LosDictionary
import pytest
from types import SimpleNamespace
import json
import logging
from los.status_code import Statuses
import django.utils.timezone

logger = logging.getLogger("django")


@pytest.mark.django_db
class Test_Customer_Create():

    def test_first_name_blank(self):
        data = {
            "customer": {
                "salutation": "mr",
                "first_name": "  ",
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.first_name['status_code']

    def test_int_for_string(self):
        data = {
            "customer": {
                "first_name": 5,
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.first_name['status_code']

    def test_salutation_uppercase(self):
        data = {
            "customer": {
                "salutation": "MR",
                "first_name": "abc",
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_salutation_invalid(self):
        data = {
            "customer": {
                "salutation": "MRr",
                "first_name": "abc",
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.salutation['status_code']

    def test_salutation_int(self):
        data = {
            "customer": {
                "salutation": 1,
                "first_name": "abc",
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.generic_error_2['status_code']

    def test_gender_invalid(self):
        data = {
            "customer": {
                "salutation": "mr",
                "first_name": "abc",
                "gender": "mal",
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.gender['status_code']

    def test_marital_status_invalid(self):
        data = {
            "customer": {
                "first_name": "abc",
                "marital_status": "mar",
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.marital_status['status_code']

    def test_blank_middle_name(self):
        data = {
            "customer": {
                "first_name": "abc",
                "middle_name": "  ",
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_blank_last_name(self):
        data = {
            "customer": {
                "first_name": "abc",
                "last_name": "  ",
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_blank_father_first_name(self):
        data = {
            "customer": {
                "first_name": "abc",
                "father_first_name": "  ",
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_blank_father_middle_name(self):
        data = {
            "customer": {
                "first_name": "abc",
                "father_middle_name": "  ",
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_blank_father_last_name(self):
        data = {
            "customer": {
                "first_name": "abc",
                "father_last_name": "  ",
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_blank_mother_first_name(self):
        data = {
            "customer": {
                "first_name": "abc",
                "mother_first_name": "  ",
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_blank_mother_last_name(self):
        data = {
            "customer": {
                "first_name": "abc",
                "mother_last_name": "  ",
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_blank_mother_middle_name(self):
        data = {
            "customer": {
                "first_name": "abc",
                "mother_middle_name": "  ",
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_blank_spouse_first_name(self):
        data = {
            "customer": {
                "first_name": "abc",
                "spouse_first_name": "  ",
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_blank_spouse_last_name(self):
        data = {
            "customer": {
                "first_name": "abc",
                "spouse_last_name": "  ",
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_blank_spouse_middle_name(self):
        data = {
            "customer": {
                "first_name": "abc",
                "spouse_middle_name": "  ",
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_no_first_name_parameter(self):
        data = {
            "customer": {
                "salutation": "mr",
                "middle_name": "abc",
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.first_name['status_code']

    def test_no_middle_name_parameter(self):
        data = {
            "customer": {
                "salutation": "mr",
                "first_name": "abc",
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_no_last_name_parameter(self):
        data = {
            "customer": {
                "salutation": "mr",
                "first_name": "abc",
                "middle_name": "abc",
                "gender": "male",
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_no_gender_parameter(self):
        data = {
            "customer": {
                "salutation": "mr",
                "first_name": "abc",
                "middle_name": "abc",
                "last_name": "abc",
                "date_of_birth": "2019-10-25",
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_no_dob_parameter(self):
        data = {
            "customer": {
                "salutation": "mr",
                "first_name": "abc",
                "middle_name": "abc",
                "last_name": "abc",
                "gender": "male",
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_no_relation_with_applicant_parameter(self):
        data = {
            "customer": {
                "salutation": "mr",
                "first_name": "abc",
                "middle_name": "abc",
                "last_name": "abc",
                "gender": "male",
                "date_of_birth": "2019-10-25",
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

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
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_no_father_first_name_parameter(self):
        data = {
            "customer": {
                "salutation": "mr",
                "first_name": "abc",
                "middle_name": "abc",
                "last_name": "abc",
                "gender": "male",
                "date_of_birth": "2019-10-25",
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

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
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_no_father_last_name_parameter(self):
        data = {
            "customer": {
                "salutation": "mr",
                "first_name": "abc",
                "middle_name": "abc",
                "last_name": "abc",
                "gender": "male",
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_no_mother_first_name_parameter(self):
        data = {
            "customer": {
                "salutation": "mr",
                "first_name": "abc",
                "middle_name": "abc",
                "last_name": "abc",
                "gender": "male",
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_no_mother_middle_name_parameter(self):
        data = {
            "customer": {
                "salutation": "mr",
                "first_name": "abc",
                "middle_name": "abc",
                "last_name": "abc",
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
        response = create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_no_mother_last_name_parameter(self):
        data = {
            "customer": {
                "salutation": "mr",
                "first_name": "abc",
                "middle_name": "abc",
                "last_name": "abc",
                "gender": "male",
                "date_of_birth": "2019-10-25",
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_no_spouse_first_name_parameter(self):
        data = {
            "customer": {
                "salutation": "mr",
                "first_name": "abc",
                "middle_name": "abc",
                "last_name": "abc",
                "spouse_middle_name": "abc",
                "spouse_last_name": "abc",
                "no_of_family_members": 4,
                "household_income_monthly": 5000
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_no_spouse_middle_name_parameter(self):
        data = {
            "customer": {
                "salutation": "mr",
                "first_name": "abc",
                "middle_name": "abc",
                "marital_status": "married",
                "father_first_name": "abc",
                "father_middle_name": "abc",
                "father_last_name": "abc",
                "mother_first_name": "abc",
                "mother_middle_name": "abc",
                "mother_last_name": "abc",
                "spouse_first_name": "abc",
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_no_spouse_last_name_parameter(self):
        data = {
            "customer": {
                "salutation": "mr",
                "first_name": "abc",
                "marital_status": "married",
                "father_first_name": "abc",
                "father_middle_name": "abc",
                "father_last_name": "abc",
                "mother_first_name": "abc",
                "mother_middle_name": "abc",
                "mother_last_name": "abc",
                "spouse_first_name": "abc",

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_no_family_members_no_parameter(self):
        data = {
            "customer": {
                "salutation": "mr",
                "first_name": "abc",
                "household_income_monthly": 5000
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_no_household_income_monthly_parameter(self):
        data = {
            "customer": {
                "salutation": "mr",
                "first_name": "abc",
                "no_of_family_members": 4,
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_no_customer_parameter(self):
        data = {

        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.generic_error_1['status_code']

    def test_no_data_in_customer_object(self):
        data = {
            "customer": {

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.first_name['status_code']

    def test_dob_format(self):
        data = {
            "customer": {
                "first_name": "Abcdd",
                "date_of_birth": "05-11-1995"
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.check_dob['status_code']

    def test_relation_with_applicant_uppercase(self):
        data = {
            "customer": {
                "first_name": "abc",
                "relation_with_applicant": "FATHER"
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_relation_with_applicant_invalid(self):
        data = {
            "customer": {
                "first_name": "abc",
                "relation_with_applicant": "abc"
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.relation_with_applicant['status_code']

    def test_no_of_family_members_notint(self):
        data = {
            "customer": {
                "first_name": "Abcdd",
                "date_of_birth": "1995-05-11",
                "no_of_family_members": "67gg",
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.check_numeric_family['status_code']

    def test_household_income_monthly_notint(self):
        data = {
            "customer": {
                "first_name": "Abcdd",
                "date_of_birth": "1995-05-11",
                "household_income_monthly": "67gg",
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.check_numeric_income['status_code']

    def test_no_of_family_members_float(self):
        data = {
            "customer": {
                "first_name": "Abcdd",
                "no_of_family_members": 5.5
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.check_numeric_family['status_code']

    def test_household_income_monthly_float(self):
        data = {
            "customer": {
                "first_name": "Abcdd",
                "household_income_monthly": 5.5
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.check_numeric_income['status_code']

    def test_customer_create_service_success(self):
        data = {
            "customer": {
                "salutation": "mr",
                "first_name": "abc",
                "middle_name": "abc",
                "last_name": "abc",
                "gender": "male",
                "date_of_birth": "2019-10-25",
                "relation_with_applicant": "father",
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
        response = create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_customer_success_with_first_name(self):
        data = {
            "customer": {
                "first_name": "abc",
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']


@pytest.mark.django_db
class Test_Customer_Update():

    def test_first_name_blank(self):
        current_time = django.utils.timezone.now()
        logger.debug("current_time india: %s", current_time)
        create_customer = Customer(
            salutation=1,
            first_name="abc",
            middle_name="abc",
            last_name="abc",
            gender=1,
            date_of_birth="2019-10-25",
            relation_with_applicant=0,
            marital_status=1,
            father_first_name="abc",
            father_middle_name="abc",
            father_last_name="abc",
            mother_first_name="abc",
            mother_middle_name="abc",
            mother_last_name="abc",
            spouse_first_name="abc",
            spouse_middle_name="abc",
            spouse_last_name="abc",
            no_of_family_members=4,
            household_income_monthly=5000,
            status=1,
            creation_date=current_time,
            creation_by="System"
        )
        create_customer.save()

        data = {
            "customer": {
                "customer_id": create_customer.id,
                "first_name": " "
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = update_customer(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.first_name['status_code']

    def test_last_name_blank(self):
        current_time = django.utils.timezone.now()
        logger.debug("current_time india: %s", current_time)
        create_customer = Customer(
            salutation=1,
            first_name="abc",
            middle_name="abc",
            last_name="abc",
            gender=1,
            date_of_birth="2019-10-25",
            relation_with_applicant=0,
            marital_status=1,
            father_first_name="abc",
            father_middle_name="abc",
            father_last_name="abc",
            mother_first_name="abc",
            mother_middle_name="abc",
            mother_last_name="abc",
            spouse_first_name="abc",
            spouse_middle_name="abc",
            spouse_last_name="abc",
            no_of_family_members=4,
            household_income_monthly=5000,
            status=1,
            creation_date=current_time,
            creation_by="System"
        )
        create_customer.save()

        data = {
            "customer": {
                "customer_id": create_customer.id,
                "first_name": "abcd",
                "last_name": "  ",
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = update_customer(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_middle_name_blank(self):
        current_time = django.utils.timezone.now()
        logger.debug("current_time india: %s", current_time)
        create_customer = Customer(
            salutation=1,
            first_name="abc",
            middle_name="abc",
            last_name="abc",
            gender=1,
            date_of_birth="2019-10-25",
            relation_with_applicant=0,
            marital_status=1,
            father_first_name="abc",
            father_middle_name="abc",
            father_last_name="abc",
            mother_first_name="abc",
            mother_middle_name="abc",
            mother_last_name="abc",
            spouse_first_name="abc",
            spouse_middle_name="abc",
            spouse_last_name="abc",
            no_of_family_members=4,
            household_income_monthly=5000,
            status=1,
            creation_date=current_time,
            creation_by="System"
        )
        create_customer.save()

        data = {
            "customer": {
                "customer_id": create_customer.id,
                "first_name": "abcd",
                "middle_name": "  ",
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = update_customer(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_father_first_name_blank(self):
        current_time = django.utils.timezone.now()
        logger.debug("current_time india: %s", current_time)
        create_customer = Customer(
            salutation=1,
            first_name="abc",
            middle_name="abc",
            last_name="abc",
            gender=1,
            date_of_birth="2019-10-25",
            relation_with_applicant=0,
            marital_status=1,
            father_first_name="abc",
            father_middle_name="abc",
            father_last_name="abc",
            mother_first_name="abc",
            mother_middle_name="abc",
            mother_last_name="abc",
            spouse_first_name="abc",
            spouse_middle_name="abc",
            spouse_last_name="abc",
            no_of_family_members=4,
            household_income_monthly=5000,
            status=1,
            creation_date=current_time,
            creation_by="System"
        )
        create_customer.save()

        data = {
            "customer": {
                "customer_id": create_customer.id,
                "first_name": "abc",
                "father_first_name": "  ",
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = update_customer(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_father_middle_name_blank(self):
        current_time = django.utils.timezone.now()
        logger.debug("current_time india: %s", current_time)
        create_customer = Customer(
            salutation=1,
            first_name="abc",
            middle_name="abc",
            last_name="abc",
            gender=1,
            date_of_birth="2019-10-25",
            relation_with_applicant=0,
            marital_status=1,
            father_first_name="abc",
            father_middle_name="abc",
            father_last_name="abc",
            mother_first_name="abc",
            mother_middle_name="abc",
            mother_last_name="abc",
            spouse_first_name="abc",
            spouse_middle_name="abc",
            spouse_last_name="abc",
            no_of_family_members=4,
            household_income_monthly=5000,
            status=1,
            creation_date=current_time,
            creation_by="System"
        )
        create_customer.save()

        data = {
            "customer": {
                "customer_id": create_customer.id,
                "first_name": "abc",
                "father_middle_name": "  ",
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = update_customer(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_father_last_name_blank(self):
        current_time = django.utils.timezone.now()
        logger.debug("current_time india: %s", current_time)
        create_customer = Customer(
            salutation=1,
            first_name="abc",
            middle_name="abc",
            last_name="abc",
            gender=1,
            date_of_birth="2019-10-25",
            relation_with_applicant=0,
            marital_status=1,
            father_first_name="abc",
            father_middle_name="abc",
            father_last_name="abc",
            mother_first_name="abc",
            mother_middle_name="abc",
            mother_last_name="abc",
            spouse_first_name="abc",
            spouse_middle_name="abc",
            spouse_last_name="abc",
            no_of_family_members=4,
            household_income_monthly=5000,
            status=1,
            creation_date=current_time,
            creation_by="System"
        )
        create_customer.save()

        data = {
            "customer": {
                "customer_id": create_customer.id,
                "first_name": "abcd",
                "father_last_name": "  ",
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = update_customer(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_mother_first_name_blank(self):
        current_time = django.utils.timezone.now()
        logger.debug("current_time india: %s", current_time)
        create_customer = Customer(
            salutation=1,
            first_name="abc",
            middle_name="abc",
            last_name="abc",
            gender=1,
            date_of_birth="2019-10-25",
            relation_with_applicant=0,
            marital_status=1,
            father_first_name="abc",
            father_middle_name="abc",
            father_last_name="abc",
            mother_first_name="abc",
            mother_middle_name="abc",
            mother_last_name="abc",
            spouse_first_name="abc",
            spouse_middle_name="abc",
            spouse_last_name="abc",
            no_of_family_members=4,
            household_income_monthly=5000,
            status=1,
            creation_date=current_time,
            creation_by="System"
        )
        create_customer.save()

        data = {
            "customer": {
                "customer_id": create_customer.id,
                "first_name": "abc",
                "mother_first_name": "  ",
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = update_customer(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_mother_last_name_blank(self):
        current_time = django.utils.timezone.now()
        logger.debug("current_time india: %s", current_time)
        create_customer = Customer(
            salutation=1,
            first_name="abc",
            middle_name="abc",
            last_name="abc",
            gender=1,
            date_of_birth="2019-10-25",
            relation_with_applicant=0,
            marital_status=1,
            father_first_name="abc",
            father_middle_name="abc",
            father_last_name="abc",
            mother_first_name="abc",
            mother_middle_name="abc",
            mother_last_name="abc",
            spouse_first_name="abc",
            spouse_middle_name="abc",
            spouse_last_name="abc",
            no_of_family_members=4,
            household_income_monthly=5000,
            status=1,
            creation_date=current_time,
            creation_by="System"
        )
        create_customer.save()

        data = {
            "customer": {
                "customer_id": create_customer.id,
                "first_name": "abcd",
                "mother_last_name": "  ",
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = update_customer(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_mother_middle_name_blank(self):
        current_time = django.utils.timezone.now()
        logger.debug("current_time india: %s", current_time)
        create_customer = Customer(
            salutation=1,
            first_name="abc",
            middle_name="abc",
            last_name="abc",
            gender=1,
            date_of_birth="2019-10-25",
            relation_with_applicant=0,
            marital_status=1,
            father_first_name="abc",
            father_middle_name="abc",
            father_last_name="abc",
            mother_first_name="abc",
            mother_middle_name="abc",
            mother_last_name="abc",
            spouse_first_name="abc",
            spouse_middle_name="abc",
            spouse_last_name="abc",
            no_of_family_members=4,
            household_income_monthly=5000,
            status=1,
            creation_date=current_time,
            creation_by="System"
        )
        create_customer.save()

        data = {
            "customer": {
                "customer_id": create_customer.id,
                "first_name": "abcd",
                "mother_middle_name": "  ",
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = update_customer(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_spouse_first_name(self):
        current_time = django.utils.timezone.now()
        logger.debug("current_time india: %s", current_time)
        create_customer = Customer(
            salutation=1,
            first_name="abc",
            middle_name="abc",
            last_name="abc",
            gender=1,
            date_of_birth="2019-10-25",
            relation_with_applicant=0,
            marital_status=1,
            father_first_name="abc",
            father_middle_name="abc",
            father_last_name="abc",
            mother_first_name="abc",
            mother_middle_name="abc",
            mother_last_name="abc",
            spouse_first_name="abc",
            spouse_middle_name="abc",
            spouse_last_name="abc",
            no_of_family_members=4,
            household_income_monthly=5000,
            status=1,
            creation_date=current_time,
            creation_by="System"
        )
        create_customer.save()

        data = {
            "customer": {
                "customer_id": create_customer.id,
                "first_name": "abcd",
                "spouse_first_name": "  ",
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = update_customer(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_spouse_last_name_blank(self):
        current_time = django.utils.timezone.now()
        logger.debug("current_time india: %s", current_time)
        create_customer = Customer(
            salutation=1,
            first_name="abc",
            middle_name="abc",
            last_name="abc",
            gender=1,
            date_of_birth="2019-10-25",
            relation_with_applicant=0,
            marital_status=1,
            father_first_name="abc",
            father_middle_name="abc",
            father_last_name="abc",
            mother_first_name="abc",
            mother_middle_name="abc",
            mother_last_name="abc",
            spouse_first_name="abc",
            spouse_middle_name="abc",
            spouse_last_name="abc",
            no_of_family_members=4,
            household_income_monthly=5000,
            status=1,
            creation_date=current_time,
            creation_by="System"
        )
        create_customer.save()

        data = {
            "customer": {
                "customer_id": create_customer.id,
                "first_name": "abcd",
                "spouse_last_name": "  ",
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = update_customer(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_spouse_middle_name_blank(self):
        current_time = django.utils.timezone.now()
        logger.debug("current_time india: %s", current_time)
        create_customer = Customer(
            salutation=1,
            first_name="abc",
            middle_name="abc",
            last_name="abc",
            gender=1,
            date_of_birth="2019-10-25",
            relation_with_applicant=0,
            marital_status=1,
            father_first_name="abc",
            father_middle_name="abc",
            father_last_name="abc",
            mother_first_name="abc",
            mother_middle_name="abc",
            mother_last_name="abc",
            spouse_first_name="abc",
            spouse_middle_name="abc",
            spouse_last_name="abc",
            no_of_family_members=4,
            household_income_monthly=5000,
            status=1,
            creation_date=current_time,
            creation_by="System"
        )
        create_customer.save()

        data = {
            "customer": {
                "customer_id": create_customer.id,
                "first_name": "abcd",
                "spouse_middle_name": "  ",
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = update_customer(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_salutation_uppercase(self):
        current_time = django.utils.timezone.now()
        logger.debug("current_time india: %s", current_time)
        create_customer = Customer(
            salutation=1,
            first_name="abc",
            middle_name="abc",
            last_name="abc",
            gender=1,
            date_of_birth="2019-10-25",
            relation_with_applicant=0,
            marital_status=1,
            father_first_name="abc",
            father_middle_name="abc",
            father_last_name="abc",
            mother_first_name="abc",
            mother_middle_name="abc",
            mother_last_name="",
            spouse_first_name="abc",
            spouse_middle_name="",
            spouse_last_name="",
            no_of_family_members=4,
            household_income_monthly=5000,
            status=1,
            creation_date=current_time,
            creation_by="System"
        )
        create_customer.save()
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "first_name": "abc",
                "salutation": "MR",

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = update_customer(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_salutation_invalid(self):
        current_time = django.utils.timezone.now()
        logger.debug("current_time india: %s", current_time)
        create_customer = Customer(
            salutation=1,
            first_name="abc",
            middle_name="abc",
            last_name="abc",
            gender=1,
            date_of_birth="2019-10-25",
            relation_with_applicant=0,
            marital_status=1,
            father_first_name="abc",
            father_middle_name="abc",
            father_last_name="abc",
            mother_first_name="abc",
            mother_middle_name="abc",
            mother_last_name="",
            spouse_first_name="abc",
            spouse_middle_name="",
            spouse_last_name="",
            no_of_family_members=4,
            household_income_monthly=5000,
            status=1,
            creation_date=current_time,
            creation_by="System"
        )
        create_customer.save()
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "first_name": "abc",
                "salutation": "MRr",

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = update_customer(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.salutation['status_code']

    def test_gender_invalid(self):
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
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "salutation": "mr",
                "first_name": "abc",
                "middle_name": "abc",
                "last_name": "abc",
                "gender": "mal",
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = update_customer(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.gender['status_code']

    def test_marital_status_invalid(self):
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
            father_last_name="abc",
            mother_first_name="abc",
            mother_middle_name="abc",
            mother_last_name="abc",
            spouse_first_name="abc",
            spouse_middle_name="abc",
            spouse_last_name="",
            no_of_family_members=4,
            household_income_monthly=5000,
            status=1,
            creation_date=current_time,
            creation_by="System"
        )
        create_customer.save()
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "first_name": "abc",
                "marital_status": "mar",
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = update_customer(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.marital_status['status_code']

    def test_customer_id_not_exist(self):
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
        data = {
            "customer": {
                "customer_id": 10000,
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = update_customer(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.id_notexist['status_code']

    def test_customer_id_invalid(self):
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
        data = {
            "customer": {
                "customer_id": 5.6,
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = update_customer(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.id_notexist['status_code']

    def test_no_customer_id_parameter(self):
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
        data = {
            "customer": {

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = update_customer(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.customer_id['status_code']

    def test_no_customer_parameter(self):
        data = {

        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = update_customer(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.generic_error_1['status_code']

    def test_no_data_in_customer_object(self):
        data = {
            "customer": {
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = update_customer(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.customer_id['status_code']

    def test_dob_format(self):
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
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "first_name": "Abcdd",
                "date_of_birth": "05-11-1995"
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = update_customer(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.check_dob['status_code']

    def test_relation_with_applicant_uppercase(self):
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
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "first_name": "Abcdd",
                "date_of_birth": "1995-05-11",
                "relation_with_applicant": "FATHER",
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = update_customer(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_relation_with_applicant_invalid(self):
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
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "first_name": "Abcdd",
                "date_of_birth": "1995-05-11",
                "relation_with_applicant": "random123",
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = update_customer(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.relation_with_applicant['status_code']

    def test_no_of_family_members_notint(self):
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
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "first_name": "Abcdd",
                "date_of_birth": "1995-05-11",
                "no_of_family_members": "67gg",
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = update_customer(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.check_numeric_family['status_code']

    def test_household_income_monthly_notint(self):
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
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "first_name": "Abcdd",
                "date_of_birth": "1995-05-11",
                "household_income_monthly": "67gg",
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = update_customer(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.check_numeric_income['status_code']

    def test_no_of_family_members_float(self):
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
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "first_name": "Abcdd",
                "no_of_family_members": 5.5
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = update_customer(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.check_numeric_family['status_code']

    def test_household_income_monthly_float(self):
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
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "first_name": "Abcdd",
                "household_income_monthly": 5.5
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = update_customer(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.check_numeric_family['status_code']

    def test_customer_update_service_success(self):
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

        data = {
            "customer": {
                "customer_id": create_customer.id,
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
        response = update_customer(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']
