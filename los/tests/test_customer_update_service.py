from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from http import HTTPStatus
from django.urls import reverse
from django.conf import settings
from los.services.customer_update_service import update_customer
import django.utils.timezone
from los.los_dict import LosDictionary
import pytest
from types import SimpleNamespace
import json
import logging
logger = logging.getLogger("django")

@pytest.mark.django_db
class Test():
    def test_type_invalid(self):
        data = {
            "customer": {
                "salutation": "mr",
                "first_name": "zain",
                "middle_name": "",
                "last_name": "",
                "gender": "male",
                "date_of_birth": "1994-11-05",
                "relation_with_applicant": 1,
                "marital_status": "single",
                "father_first_name": "",
                "father_middle_name": "",
                "father_last_name": "",
                "mother_first_name": "",
                "mother_middle_name": "",
                "mother_last_name": "",
                "spouse_first_name": "",
                "spouse_middle_name": "",
                "spouse_last_name": "",
                "no_of_family_members": 1,
                "household_income_monthly": 987
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = update_customer(data)
        logger.info("response: %s", response)
        assert response['error_code'] == 20005
