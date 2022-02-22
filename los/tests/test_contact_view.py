import json
import logging

import django.utils.timezone
import pytest
from django.urls import reverse

from los.models import Customer
from los.models import CustomerContact
from los.status_code import Statuses

logger = logging.getLogger("django")


@pytest.mark.django_db
class TestContactCreateView:

    def test_create_contact_view_GET(self, client):

        url = reverse('customer_contact_create')
        response = client.get(url)
        logger.info("response for get method : %s", response)
        assert response.status_code == Statuses.test_get['status_code']

    def test_create_contact_view_POST(self, client):
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
                "contacts": [
                    {
                        "type": "mob",
                        "value": "7360261469",
                        "country_code": "91"
                    },
                    {
                        "type": "email",
                        "value": "abc@abc.com"
                    }
                ]

            }
        }

        url = reverse('customer_contact_create')
        data = json.dumps(data)
        response = client.post(url, data=data, content_type='application/json')
        logger.info("response for post method: %s", response)
        assert response.status_code == Statuses.test_post['status_code']


@pytest.mark.django_db
class TestCustomerUpdateView():

    def test_update_contact_view_GET(self, client):
        url = reverse('customer_contact_update')
        response = client.get(url)
        logger.info("response for get method : %s", response)
        assert response.status_code == Statuses.test_get['status_code']

    def test_update_contact_view_POST(self,client):
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

        current_time = django.utils.timezone.now()
        logger.debug("current_time india: %s", current_time)
        create_contact1 = CustomerContact(
            type=10,
            value="7360261469",
            value_extra_1=None,
            country_code="+91",
            status=1,
            creation_date=current_time,
            creation_by="System",
            customer_id=create_customer.id
        )
        create_contact1.save()

        current_time = django.utils.timezone.now()
        logger.debug("current_time india: %s", current_time)
        create_contact2 = CustomerContact(
            type=10,
            value="7360261469",
            value_extra_1=None,
            country_code="+91",
            status=1,
            creation_date=current_time,
            creation_by="System",
            customer_id=create_customer.id
        )
        create_contact2.save()
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "contacts": [
                    {
                        "contact_id": create_contact1.id,
                        "type": "email",
                        "value": "abc@abc.com"
                    },
                    {
                        "contact_id": create_contact2.id,
                        "type": "mob",
                        "value": "7360261469",
                        "country_code": "+91"
                    }
                ]

            }
        }
        url = reverse('customer_contact_update')
        data = json.dumps(data)
        response = client.post(url, data=data, content_type='application/json')
        logger.info("response for post method: %s", response)
        assert response.status_code == Statuses.test_post['status_code']