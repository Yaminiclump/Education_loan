import json
import logging
from types import SimpleNamespace

import django.utils.timezone
import django.utils.timezone
import pytest

from los.models.customer_model import Customer
from los.models.customer_contact_model import CustomerContact
from los.services.customer_contact_service import contact_service, contact_update
from los.status_code import Statuses

logger = logging.getLogger("django")


@pytest.mark.django_db
class TestContactCreate():

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
        assert response['status'] == Statuses.customer_id_not_exist['status_code']

    def test_customer_id_invalid_format(self):
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
                "customer_id": "10000",
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
        assert response['status'] == Statuses.customer_id_invalid_format['status_code']

    def test_customer_id_not_provided(self):
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
        assert response['status'] == Statuses.customer_id_not_provided['status_code']

    def test_no_contact_parameter(self):
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
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = contact_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.generic_error_1['status_code']

    def test_contact_parameter_blank(self):
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
                "contact": [],
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = contact_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.generic_error_1['status_code']

    def test_no_data_contact_parameter(self):
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
                "contact": [
                    {}
                ],
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = contact_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.generic_error_1['status_code']

    def test_no_data_contact_parameter_2(self):
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
                "contact": [
                    {
                        "type": "mob",
                        "value": "07360261469",
                        "country_code": "91"
                    },
                    {}
                ],
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = contact_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.generic_error_1['status_code']

    def test_no_type_parameter(self):
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
                "contact": [
                    {
                        "type": "email",
                        "value": "abc@abc.com"
                    },
                    {
                        "value": "07478267826",
                        "country_code": "91"
                    }
                ],
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = contact_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.contact_type['status_code']

    def test_contact_type_invalid(self):
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
                        "type": "fsfsa",
                        "value": "07478267826",
                        "country_code": "91"
                    }
                ]
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = contact_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.contact_type['status_code']

    def test_no_value_parameter(self):
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
                        "type": "email",
                        "value": "abc@abc.com"
                    },
                    {
                        "type": "mob",
                        "country_code": "91"
                    }
                ]
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = contact_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.contact_value['status_code']

    def test_no_value_parameter_2(self):
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
                        "type": "email",
                        "value": "abc@abc.com"
                    },
                    {
                        "type": "email",
                    }
                ]
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = contact_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.contact_value['status_code']

    def test_mob_value_invalid(self):
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
                        "type": "email",
                        "value": "abc@abc.com"
                    },
                    {
                        "type": "mob",
                        "value": "555555555",
                        "country_code": "91"
                    }
                ]
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = contact_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.mobile_number['status_code']

    def test_email_value_invalid(self):
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
                        "type": "email",
                        "value": "abc@abc.com"
                    },
                    {
                        "type": "email",
                        "value": "daj"
                    }
                ]
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = contact_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.email_address['status_code']

    def test_no_country_code_parameter(self):
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
                        "type": "email",
                        "value": "abc@abc.com"
                    },
                    {
                        "type": "mob",
                        "value": "07360261469",
                    }
                ]
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = contact_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.contact_country_code['status_code']

    def test_email_with_country_code(self):
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
                        "type": "email",
                        "value": "abc@abc.com"
                    },
                    {
                        "type": "email",
                        "value": "abc@abc.com",
                        "country_code": "+91"
                    }
                ]
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = contact_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.contact_country_code['status_code']

    def test_no_customer_parameter(self):
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

        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = contact_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.generic_error_1['status_code']

    def test_data_null(self):
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
        data = None
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = contact_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.generic_error_1['status_code']

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
                "customer_id": create_customer.id,
                "contacts": [
                    {
                        "type": "mob",
                        "value": "07478267826",
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

    def test_contact_success_with_mob_2(self):
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
                        "value": "06360261469",
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
                "customer_id": create_customer.id,
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

    def test_contact_success(self):
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
                        "value": "07360261469",
                        "country_code": "91"
                    },
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

    def test_exception(self, django_db_blocker):
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
                        "type": "email",
                        "value": "abc@abc.com"
                    }
                ]

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        with django_db_blocker.block():
            response_obj = contact_service(data)
        assert response_obj["status"] == Statuses.generic_error_2["status_code"]


@pytest.mark.django_db
class TestContactUpdate():

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

        current_time = django.utils.timezone.now()
        logger.debug("current_time india: %s", current_time)
        create_contact1 = CustomerContact(
            type=10,
            value="07360261469",
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
            value="07360261469",
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
                "customer_id":10000,
                "contacts": [
                    {
                        "contact_id": create_contact1.id,
                        "type": "email",
                        "value": "abc@abc.com"
                    },
                    {
                        "contact_id": create_contact2.id,
                        "type": "mob",
                        "value": "07360261469",
                        "country_code": "+91"
                    }
                ]

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = contact_update(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.customer_id_not_exist['status_code']

    def test_customer_id_invalid_format(self):
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
            value="07360261469",
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
            value="07360261469",
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
                "customer_id": "10000",
                "contacts": [
                    {
                        "contact_id": create_contact1.id,
                        "type": "email",
                        "value": "abc@abc.com"
                    },
                    {
                        "contact_id": create_contact2.id,
                        "type": "mob",
                        "value": "07360261469",
                        "country_code": "+91"
                    }
                ]

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = contact_update(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.customer_id_invalid_format['status_code']

    def test_customer_id_not_provided(self):
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
            value="07360261469",
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
            value="07360261469",
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
                "contacts": [
                    {
                        "contact_id": create_contact1.id,
                        "type": "email",
                        "value": "abc@abc.com"
                    },
                    {
                        "contact_id": create_contact2.id,
                        "type": "mob",
                        "value": "07360261469",
                        "country_code": "+91"
                    }
                ]

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = contact_update(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.customer_id_not_provided['status_code']

    def test_no_contact_parameter(self):
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
            value="07360261469",
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
            value="07360261469",
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
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = contact_update(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.generic_error_1['status_code']

    def test_contact_parameter_blank(self):
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
            value="07360261469",
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
            value="07360261469",
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
                "contacts": []

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = contact_update(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.generic_error_1['status_code']

    def test_no_customer_contact_id(self):
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
            value="07360261469",
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
            value="07360261469",
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
                    }
                ]

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = contact_update(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.customer_contact_id_not_provided['status_code']

    def test_customer_contact_id_not_exist(self):
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
            value="07360261469",
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
            value="07360261469",
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
                        "contact_id": 10000

                    }
                ]

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = contact_update(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.customer_contact_id_not_exist['status_code']

    def test_customer_contact_id_invalid(self):
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
            value="07360261469",
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
            value="07360261469",
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
                        "contact_id": "10000"
                    }
                ]

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = contact_update(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.customer_contact_id_not_exist['status_code']

    def test_no_type_parameter(self):
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
            value="07360261469",
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
            value="07360261469",
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
                        "value": "07360261469",
                        "country_code": "+91"
                    }
                ]

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = contact_update(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.contact_type['status_code']

    def test_contact_type_invalid(self):
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
            value="07360261469",
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
            value="07360261469",
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
                        "type": "fdefgd",
                        "value": "07360261469",
                        "country_code": "+91"
                    }
                ]

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = contact_update(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.contact_type['status_code']

    def test_no_value_parameter(self):
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
            value="07360261469",
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
            value="07360261469",
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
                        "country_code": "+91"
                    }
                ]

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = contact_update(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.contact_value['status_code']

    def test_no_value_parameter_2(self):
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
            value="07360261469",
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
            value="07360261469",
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
                        "type": "email",
                    }
                ]

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = contact_update(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.contact_value['status_code']

    def test_mob_value_invalid(self):
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
            value="07360261469",
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
            value="07360261469",
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
                        "value": "555555555",
                        "country_code": "+91"
                    }
                ]

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = contact_update(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.mobile_number['status_code']

    def test_email_value_invalid(self):
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
            value="07360261469",
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
            value="07360261469",
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
                        "type": "email",
                        "value": "gadfsgeq",
                        "country_code": "+91"
                    }
                ]

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = contact_update(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.email_address['status_code']

    def test_no_country_code_parameter(self):
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
            value="07360261469",
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
            value="07360261469",
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
                        "value": "07360261469",
                    }
                ]

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = contact_update(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.contact_country_code['status_code']

    def test_email_with_country_code(self):
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
            value="07360261469",
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
            value="07360261469",
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
                        "type": "email",
                        "value": "abc@abc.com",
                        "country_code": "+91"
                    }
                ]

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = contact_update(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.contact_country_code['status_code']

    def test_no_customer_parameter(self):
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
            value="07360261469",
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
            value="07360261469",
            value_extra_1=None,
            country_code="+91",
            status=1,
            creation_date=current_time,
            creation_by="System",
            customer_id=create_customer.id
        )
        create_contact2.save()
        data = {
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = contact_update(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.generic_error_1['status_code']

    def test_data_null(self):
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
            value="07360261469",
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
            value="07360261469",
            value_extra_1=None,
            country_code="+91",
            status=1,
            creation_date=current_time,
            creation_by="System",
            customer_id=create_customer.id
        )
        create_contact2.save()
        data = None
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = contact_update(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.generic_error_1['status_code']

    def test_contact_update_success(self):
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
            value="07360261469",
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
            value="07360261469",
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
                        "value": "07360261469",
                        "country_code": "+91"
                    }
                ]

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = contact_update(data)
        logger.info("response: %s", response)
        assert response["status"] == Statuses.success["status_code"]

    def test_contact_update_same_id(self):
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
            value="07360261469",
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
            value="07360261469",
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
                        "contact_id": create_contact1.id,
                        "type": "mob",
                        "value": "07360261469",
                        "country_code": "+91"
                    }
                ]

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = contact_update(data)
        logger.info("response: %s", response)
        assert response["status"] == Statuses.same_contact_id["status_code"]

    def test_exception(self, django_db_blocker):
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
            value="07360261469",
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
            value="07360261469",
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
                        "value": "07360261469",
                        "country_code": "+91"
                    }
                ]

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        with django_db_blocker.block():
            response_obj = contact_service(data)
        assert response_obj["status"] == Statuses.generic_error_2["status_code"]