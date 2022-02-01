from rest_framework import status
from rest_framework.test import APITestCase
from http import HTTPStatus
from django.conf import settings
from los.services import customer_service
from los.models.customer_model import Customer
import django.utils.timezone
from los.los_dict import LosDictionary
import pytest
from types import SimpleNamespace
import json
from django.test import TestCase, Client
import logging
from django.urls import reverse_lazy, reverse
from types import SimpleNamespace
import requests
from los.error_code import errors
logger = logging.getLogger("django")


@pytest.mark.django_db
class Test():

    def test_update_customer_view_GET(self, client):

        url = reverse('customer_update')
        response = client.get(url)
        logger.info("response for get method : %s", response)
        assert response.status_code == errors.test_get['error_code']

    def test_update_customer_view_POST(self,client):
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
        url = reverse('customer_update')
        data = json.dumps(data)
        response = client.post(url, data=data, content_type='application/json')
        logger.info("response for post method: %s", response)
        assert response.status_code == errors.test_post['error_code']