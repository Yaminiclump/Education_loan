from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from http import HTTPStatus
from django.urls import reverse
from django.conf import settings
from los.services.customer_contact_service import contact_service
from los.services.customer_contact_service import contact_update

from los.models.customer_contact_model import CustomerContact
from los.models.customer_contact_model import CustomerContactLog
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
class TestContactCreate():

    def test_contact_success_with_mob(self):
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
                "customer_id":  create_customer.id,
                "contacts": [
                    {
                        "type": "mob",
                        "value": "07360261469",
                        "country_code": "91"
                    }
                ]

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = contact_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_contact_success_with_email(self):
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
                "customer_id":  create_customer.id,
                "contacts": [
                    {
                        "type": "email",
                        "value": "abc@abc.com"
                    }
                ]

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = contact_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

