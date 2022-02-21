import json
import pytest
from los.models.customer_model import Customer
from los.models.employment_model import Employment
from los.status_code import Statuses
import json
import logging
from django.test import TestCase, Client
from django.urls import reverse
from los.services.employment_service import employment_create_service,employment_update_service
from los.constants import STATUS_ACTIVE, CREATION_BY, UPDATION_BY
import django.utils.timezone

logger = logging.getLogger("django")

class TestCreateEmploymentyView(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('employment_create')

    def postreq(self, payload):
        return self.client.post(self.url, json.dumps(payload), content_type="application/json")

    def test_invalid_request(self):
        logger.info("Check if it rejects request for GET request")
        response = self.client.get(self.url)
        logger.info("Response %s", response)
        # 405 = request not allowed
        self.assertEqual(response.status_code, 405)

    def test_exception(self):
        body = {
            "customer": {
                "customer_id": 5000,
                "employment": {
                    "employment_id": 7000,
                    "type": "salaried",
                    "gross_income_monthly": 9987.98,
                    "net_income_monthly": 9876.56,
                }
            }
        }
        # not using postreq() to send post request will result in data to be distorted and hence will go into exception.
        response = self.client.post(self.url, data=body)
        content = json.loads(response.content)
        error_code = content['status_code']
        # logger.info("Response %s", content['status_code'])
        # 200 = successful response
        self.assertEqual(response.status_code, 200)
        # 20101 Invalid Request Details
        self.assertEqual(error_code, Statuses.generic_error_2["status_code"])

    def test_success(self):
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
            status=STATUS_ACTIVE,
            creation_date=current_time,
            creation_by=CREATION_BY
        )
        create_customer.save()
        body = {
            "customer": {
                "customer_id": create_customer.id,
                "employment": {
                    "type": "salaried",
                    "gross_income_monthly": 9987.98,
                    "net_income_monthly": 9876.56,
                }
            }
        }
        response = self.postreq(body)
        content = json.loads(response.content)
        error_code = content['status']
        logger.info("Response %s", content['status'])

        # 200 = successful response
        self.assertEqual(response.status_code, 200)
        # success = 10000 successfully found and fetched data
        self.assertEqual(error_code, Statuses.success["status_code"])

class TestUpdateEmploymentyView(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('employment_update')

    def postreq(self, payload):
        return self.client.post(self.url, json.dumps(payload), content_type="application/json")

    def test_invalid_request(self):
        logger.info("Check if it rejects request for GET request")
        response = self.client.get(self.url)
        logger.info("Response %s", response)
        # 405 = request not allowed
        self.assertEqual(response.status_code, 405)

    def test_exception(self):
        body = {
            "customer": {
                "customer_id": 500000,
                "employment": {
                    "employment_id": 7000,
                    "type": "salaried",
                    "gross_income_monthly": 9987.98,
                    "net_income_monthly": 9876.56,
                }
            }
        }
        # not using postreq() to send post request will result in data to be distorted and hence will go into exception.
        response = self.client.post(self.url, data=body)
        content = json.loads(response.content)
        error_code = content['status_code']
        # logger.info("Response %s", content['status_code'])
        # 200 = successful response
        self.assertEqual(response.status_code, 200)
        # 20101 Invalid Request Details
        self.assertEqual(error_code, Statuses.generic_error_2["status_code"])

    def test_success(self):
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
            status=STATUS_ACTIVE,
            creation_date=current_time,
            creation_by=CREATION_BY
        )
        create_customer.save()
        create_employment = Employment(
            type=11,
            employer_id=1,
            employer_name="abc",
            address_id=0,
            designation_id=0,
            designation_name="string",
            retirement_age_years=0,
            current_employer_months=0,
            gross_income_monthly=9876.98,
            net_income_monthly=123.98,
            other_income_monthly=0,
            work_experience_month=0,
            status=STATUS_ACTIVE,
            creation_date=current_time,
            creation_by=CREATION_BY,
            customer_id=create_customer.id,
        )
        create_employment.save()
        body = {
            "customer": {
                "customer_id": create_customer.id,
                "employment": {
                    "employment_id": create_employment.id,
                    "type": "salaried",
                    "gross_income_monthly": 9987.98,
                    "net_income_monthly": 9876.56,
                }
            }
        }
        response = self.postreq(body)
        content = json.loads(response.content)
        error_code = content['status']
        logger.info("Response %s", content['status'])
        # 200 = successful response
        self.assertEqual(response.status_code, 200)
        # success = 10000 successfully found and fetched data
        self.assertEqual(error_code, Statuses.success["status_code"])

