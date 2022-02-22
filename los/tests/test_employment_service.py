import json
import logging
from types import SimpleNamespace
import django.utils.timezone
import pytest
from los.models.customer_model import Customer
from los.models.employment_model import EmploymentLog, Employment
from los.services.employment_service import employment_create_service, employment_update_service
from los.status_code import Statuses
from los.constants import STATUS_ACTIVE, CREATION_BY, UPDATION_BY

logger = logging.getLogger("django")


@pytest.mark.django_db
class TestEmploymentCreate():
    def test_customer_id_not_exist(self):
        current_time = django.utils.timezone.now()
        logger.debug("current_time india: %s", current_time)
        create_customer = Customer(
            salutation=1,
            first_name="abcdf",
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
        data = {
            "customer": {
                "customer_id": 1000000,
                "employment": {
                    "type": "salaried",
                    "employer_id": 0,
                    "employer_name": "string",
                    "address_id": 0,
                    "designation_id": 0,
                    "designation_name": "string",
                    "retirement_age_years": 0,
                    "current_employer_months": 0,
                    "gross_income_monthly": 9987.98,
                    "net_income_monthly": 9876.56,
                    "other_income_monthly": 0,
                    "work_experience_month": 0
                }

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = employment_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.customer_id_not_exist['status_code']

    def test_customer_id_not_provided(self):
        current_time = django.utils.timezone.now()
        logger.debug("current_time india: %s", current_time)
        create_customer = Customer(
            salutation=1,
            first_name="abcdf",
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
        data = {
            "customer": {
                "employment": {
                    "type": "salaried",
                    "employer_id": 0,
                    "employer_name": "string",
                    "address_id": 0,
                    "designation_id": 0,
                    "designation_name": "string",
                    "retirement_age_years": 0,
                    "current_employer_months": 0,
                    "gross_income_monthly": 9987.98,
                    "net_income_monthly": 9876.56,
                    "other_income_monthly": 0,
                    "work_experience_month": 0
                }

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = employment_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.customer_contact_id_not_provided['status_code']

    def test_no_employment_parameter(self):
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
        data = {
            "customer": {
                "customer_id": create_customer.id,
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = employment_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.employment_details_not_provided['status_code']

    def test_employment_parameter_blank(self):
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
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "employment": {
                }

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = employment_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.employer_name['status_code']

    def test_employment_type_invalid(self):
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
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "employment": {
                    "type": "salar",
                    "employer_id": 1,
                    "designation_id": 2,
                    "gross_income_monthly": 9987.98,
                    "net_income_monthly": 9876.56,
                    "other_income_monthly": 0,
                    "work_experience_month": 0
                }

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = employment_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.employment_type['status_code']

    def test_employer_id_not_int(self):
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
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "employment": {
                    "type": "salaried",
                    "employer_id": "abcd",
                    "gross_income_monthly": 9987.98,
                    "net_income_monthly": 9876.56,
                    "other_income_monthly": 0,
                    "work_experience_month": 0
                }
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = employment_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.employer_id['status_code']

    def test_employer_id_is_zero(self):
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
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "employment": {
                    "type": "salaried",
                    "employer_id": 0,  # If employer id is zero then employer name should not be None
                    "employer_name": "",
                    "gross_income_monthly": 9987.98,
                    "net_income_monthly": 9876.56,
                    "other_income_monthly": 0,
                    "work_experience_month": 0
                }
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = employment_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.employer_name['status_code']

    def test_employer_id_is_non_zero(self):
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
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "employment": {
                    "type": "salaried",
                    "employer_id": 12,  # If employer id is non zero then employer name should be None
                    "employer_name": "abcd",
                    "gross_income_monthly": 9987.98,
                    "net_income_monthly": 9876.56,
                    "other_income_monthly": 0,
                    "work_experience_month": 0
                }
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = employment_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.employer_name['status_code']

    def test_designation_id_is_zero(self):
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
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "employment": {
                    "type": "salaried",
                    "employer_id": 12,
                    "designation_id": 0,  # If designation id is zero then designation name should not be None
                    "designation_name": "",
                    "gross_income_monthly": 9987.98,
                    "net_income_monthly": 9876.56,
                    "other_income_monthly": 0,
                    "work_experience_month": 0
                }
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = employment_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.designation_name['status_code']

    def test_designation_id_is_non_zero(self):
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
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "employment": {
                    "type": "salaried",
                    "employer_id": 12,  # If employer id is non zero then employer name should be None
                    "designation_id": 97,
                    "designation_name": "abcd",
                    "gross_income_monthly": 9987.98,
                    "net_income_monthly": 9876.56,
                    "other_income_monthly": 0,
                    "work_experience_month": 0
                }
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = employment_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.designation_name['status_code']

    def test_address_id_not_int(self):
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
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "employment": {
                    "type": "salaried",
                    "employer_id": 1,
                    "designation_id": 2,
                    "address_id": "abcd",
                    "gross_income_monthly": 9987.98,
                    "net_income_monthly": 9876.56,
                    "other_income_monthly": 0,
                    "work_experience_month": 0
                }
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = employment_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.address_id['status_code']

    def test_designation_id_not_int(self):
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
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "employment": {
                    "type": "salaried",
                    "employer_id": 1,
                    "designation_id": "abcd",
                    "gross_income_monthly": 9987.98,
                    "net_income_monthly": 9876.56,
                    "other_income_monthly": 0,
                    "work_experience_month": 0
                }
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = employment_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.designation_id['status_code']

    def test_current_employer_months_not_int(self):
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
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "employment": {
                    "type": "salaried",
                    "employer_id": 1,
                    "designation_id": 2,
                    "current_employer_months": "abcd",
                    "gross_income_monthly": 9987.98,
                    "net_income_monthly": 9876.56,
                    "other_income_monthly": 0,
                    "work_experience_month": 0
                }
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = employment_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.current_employer_months['status_code']

    def test_retirement_age_years_not_int(self):
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
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "employment": {
                    "type": "salaried",
                    "employer_id": 1,
                    "designation_id": 2,
                    "retirement_age_years": "abcd",
                    "gross_income_monthly": 9987.98,
                    "net_income_monthly": 9876.56,
                    "other_income_monthly": 0,
                    "work_experience_month": 0
                }
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = employment_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.retirement_age_years['status_code']

    def test_no_gross_income_monthly_pram(self):
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
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "employment": {
                    "type": "salaried",
                    "employer_id": 1,
                    "designation_id": 2,
                    "net_income_monthly": 9876.56,
                    "other_income_monthly": 0,
                    "work_experience_month": 0
                }
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = employment_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.gross_income_monthly['status_code']

    def test_no_net_income_monthly_pram(self):
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
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "employment": {
                    "type": "salaried",
                    "employer_id": 1,
                    "designation_id": 2,
                    "gross_income_monthly": 9876.56,
                    "other_income_monthly": 0,
                    "work_experience_month": 0
                }
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = employment_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.net_income_monthly['status_code']

    def test_gross_income_monthly_invalid(self):
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
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "employment": {
                    "type": "salaried",
                    "employer_id": 1,
                    "designation_id": 2,
                    "gross_income_monthly": "abcd",
                    "net_income_monthly": 9876.56,
                    "other_income_monthly": 0,
                    "work_experience_month": 0
                }
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = employment_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.gross_income_monthly['status_code']

    def test_net_income_monthly_invalid(self):
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
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "employment": {
                    "type": "salaried",
                    "employer_id": 1,
                    "designation_id": 2,
                    "gross_income_monthly": 9876.56,
                    "net_income_monthly": "abcd",
                    "other_income_monthly": 0,
                    "work_experience_month": 0
                }
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = employment_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.net_income_monthly['status_code']

    def test_other_income_monthly_not_int(self):
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
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "employment": {
                    "type": "salaried",
                    "employer_id": 1,
                    "designation_id": 2,
                    "gross_income_monthly": 9987.98,
                    "net_income_monthly": 9876.56,
                    "other_income_monthly": "abcd",
                    "work_experience_month": 0,
                }
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = employment_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.other_income_monthly['status_code']

    def test_work_experience_month_not_int(self):
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
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "employment": {
                    "type": "salaried",
                    "employer_id": 1,
                    "designation_id": 2,
                    "gross_income_monthly": 9987.98,
                    "net_income_monthly": 9876.56,
                    "other_income_monthly": 0,
                    "work_experience_month": "abcd",
                }
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = employment_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.work_experience_month['status_code']

    def test_employment_success(self):
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
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "employment": {
                    "type": "salaried",
                    "employer_id": 1,
                    "designation_id": 2,
                    "gross_income_monthly": 9987.98,
                    "net_income_monthly": 9876.56,
                }
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = employment_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_exception(self, django_db_blocker):
        current_time = django.utils.timezone.now()
        logger.info("Test for checking if the program throws an exception when db access is denied")
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
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "employment": {
                    "type": "salaried",
                    "employer_id": 1,
                    "designation_id": 2,
                    "gross_income_monthly": 9987.98,
                    "net_income_monthly": 9876.56,
                }
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        with django_db_blocker.block():
            response_obj = employment_create_service(data)
        assert response_obj["status"] == Statuses.generic_error_2["status_code"]

    def test_no_param(self):
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
        data = {}
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = employment_create_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.generic_error_1['status_code']


@pytest.mark.django_db
class TestEmploymentUpdate():

    def test_customer_id_not_exist(self):
        current_time = django.utils.timezone.now()
        logger.debug("current_time india: %s", current_time)
        create_customer = Customer(
            salutation=1,
            first_name="abcdf",
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

        data = {
            "customer": {
                "customer_id": 10000000,
                "employment": {
                    "employment_id": create_employment.id,
                    "type": "salaried",
                    "employer_id": 0,
                    "employer_name": "string",
                    "address_id": 0,
                    "designation_id": 0,
                    "designation_name": "string",
                    "retirement_age_years": 0,
                    "current_employer_months": 0,
                    "gross_income_monthly": 9987.98,
                    "net_income_monthly": 9876.56,
                    "other_income_monthly": 0,
                    "work_experience_month": 0
                }

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = employment_update_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.customer_id_not_exist['status_code']

    def test_no_employment_param(self):
        current_time = django.utils.timezone.now()
        logger.debug("current_time india: %s", current_time)
        create_customer = Customer(
            salutation=1,
            first_name="abcdf",
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

        data = {
            "customer": {
                "customer_id": create_customer.id,

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = employment_update_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.employment_details_not_provided['status_code']

    def test_employment_id_not_exist(self):
        current_time = django.utils.timezone.now()
        logger.debug("current_time india: %s", current_time)
        create_customer = Customer(
            salutation=1,
            first_name="abcdf",
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

        data = {
            "customer": {
                "customer_id": create_customer.id,
                "employment": {
                    "employment_id": 10000000000000,
                    "type": "salaried",
                    "employer_id": 0,
                    "employer_name": "string",
                    "address_id": 0,
                    "designation_id": 0,
                    "designation_name": "string",
                    "retirement_age_years": 0,
                    "current_employer_months": 0,
                    "gross_income_monthly": 9987.98,
                    "net_income_monthly": 9876.56,
                    "other_income_monthly": 0,
                    "work_experience_month": 0
                }

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = employment_update_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.employment_id_not_exists['status_code']

    def test_customer_id_not_provided(self):
        current_time = django.utils.timezone.now()
        logger.debug("current_time india: %s", current_time)
        create_customer = Customer(
            salutation=1,
            first_name="abcdf",
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
        data = {
            "customer": {
                "employment": {
                    "employment_id": create_employment.id,
                    "type": "salaried",
                    "employer_id": 0,
                    "employer_name": "string",
                    "address_id": 0,
                    "designation_id": 0,
                    "designation_name": "string",
                    "retirement_age_years": 0,
                    "current_employer_months": 0,
                    "gross_income_monthly": 9987.98,
                    "net_income_monthly": 9876.56,
                    "other_income_monthly": 0,
                    "work_experience_month": 0
                }

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = employment_update_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.customer_contact_id_not_provided['status_code']

    def test_employment_id_not_provided(self):
        current_time = django.utils.timezone.now()
        logger.debug("current_time india: %s", current_time)
        create_customer = Customer(
            salutation=1,
            first_name="abcdf",
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
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "employment": {
                    "type": "salaried",
                    "employer_id": 0,
                    "employer_name": "string",
                    "address_id": 0,
                    "designation_id": 0,
                    "designation_name": "string",
                    "retirement_age_years": 0,
                    "current_employer_months": 0,
                    "gross_income_monthly": 9987.98,
                    "net_income_monthly": 9876.56,
                    "other_income_monthly": 0,
                    "work_experience_month": 0
                }

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = employment_update_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.employment_id_not_provided['status_code']

    def test_employment_parameter_blank(self):
        current_time = django.utils.timezone.now()
        logger.debug("current_time india: %s", current_time)
        create_customer = Customer(
            salutation=1,
            first_name="abcdf",
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
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "employment": {

                }

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = employment_update_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.employment_id_not_provided['status_code']

    def test_employment_type_invalid(self):
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
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "employment": {
                    "employment_id": create_employment.id,
                    "type": "salar",
                    "gross_income_monthly": 9987.98,
                    "net_income_monthly": 9876.56,
                    "other_income_monthly": 0,
                    "work_experience_month": 0
                }

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = employment_update_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.employment_type['status_code']

    def test_employer_id_not_int(self):
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
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "employment": {
                    "employment_id": create_employment.id,
                    "type": "salaried",
                    "employer_id": "abcd",
                    "gross_income_monthly": 9987.98,
                    "net_income_monthly": 9876.56,
                    "other_income_monthly": 0,
                    "work_experience_month": 0
                }

            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = employment_update_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.employer_id['status_code']

    def test_address_id_not_int(self):
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
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "employment": {
                    "employment_id": create_employment.id,
                    "type": "salaried",
                    "employer_id": 1,
                    "designation_id": 2,
                    "address_id": "abcd",
                    "gross_income_monthly": 9987.98,
                    "net_income_monthly": 9876.56,
                    "other_income_monthly": 0,
                    "work_experience_month": 0
                }
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = employment_update_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.address_id['status_code']

    def test_designation_id_not_int(self):
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
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "employment": {
                    "employment_id": create_employment.id,
                    "type": "salaried",
                    "employer_id": 1,
                    "designation_id": "abcd",
                    "gross_income_monthly": 9987.98,
                    "net_income_monthly": 9876.56,
                    "other_income_monthly": 0,
                    "work_experience_month": 0
                }
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = employment_update_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.designation_id['status_code']

    def test_current_employer_months_not_int(self):
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
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "employment": {
                    "employment_id": create_employment.id,
                    "type": "salaried",
                    "employer_id": 1,
                    "designation_id": 2,
                    "current_employer_months": "abcd",
                    "gross_income_monthly": 9987.98,
                    "net_income_monthly": 9876.56,
                    "other_income_monthly": 0,
                    "work_experience_month": 0
                }
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = employment_update_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.current_employer_months['status_code']

    def test_retirement_age_years_not_int(self):
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
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "employment": {
                    "employment_id": create_employment.id,
                    "type": "salaried",
                    "employer_id": 1,
                    "designation_id": 2,
                    "retirement_age_years": "abcd",
                    "gross_income_monthly": 9987.98,
                    "net_income_monthly": 9876.56,
                    "other_income_monthly": 0,
                    "work_experience_month": 0
                }
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = employment_update_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.retirement_age_years['status_code']

    def test_no_gross_income_monthly_pram(self):
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
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "employment": {
                    "employment_id": create_employment.id,
                    "type": "salaried",
                    "employer_id": 1,
                    "designation_id": 2,
                    "net_income_monthly": 9876.56,
                    "other_income_monthly": 0,
                    "work_experience_month": 0
                }
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = employment_update_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_no_net_income_monthly_pram(self):
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
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "employment": {
                    "employment_id": create_employment.id,
                    "type": "salaried",
                    "employer_id": 1,
                    "designation_id": 2,
                    "gross_income_monthly": 9876.56,
                    "other_income_monthly": 0,
                    "work_experience_month": 0
                }
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = employment_update_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_gross_income_monthly_invalid(self):
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
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "employment": {
                    "employment_id": create_employment.id,
                    "type": "salaried",
                    "employer_id": 1,
                    "designation_id": 2,
                    "gross_income_monthly": "abcd",
                    "net_income_monthly": 9876.56,
                    "other_income_monthly": 0,
                    "work_experience_month": 0
                }
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = employment_update_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.gross_income_monthly['status_code']

    def test_net_income_monthly_invalid(self):
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
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "employment": {
                    "employment_id": create_employment.id,
                    "type": "salaried",
                    "employer_id": 1,
                    "designation_id": 2,
                    "gross_income_monthly": 9876.56,
                    "net_income_monthly": "abcd",
                    "other_income_monthly": 0,
                    "work_experience_month": 0
                }
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = employment_update_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.net_income_monthly['status_code']

    def test_other_income_monthly_not_int(self):
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
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "employment": {
                    "employment_id": create_employment.id,
                    "type": "salaried",
                    "employer_id": 1,
                    "designation_id": 2,
                    "gross_income_monthly": 9987.98,
                    "net_income_monthly": 9876.56,
                    "other_income_monthly": "abcd",
                    "work_experience_month": 0,
                }
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = employment_update_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.other_income_monthly['status_code']

    def test_work_experience_month_not_int(self):
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
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "employment": {
                    "employment_id": create_employment.id,
                    "type": "salaried",
                    "employer_id": 1,
                    "designation_id": 2,
                    "gross_income_monthly": 9987.98,
                    "net_income_monthly": 9876.56,
                    "other_income_monthly": 0,
                    "work_experience_month": "abcd",
                }
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = employment_update_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.work_experience_month['status_code']

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
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "employment": {
                    "employment_id": create_employment.id,
                    "employer_id": 1,
                    "designation_id": 2,
                    "gross_income_monthly": 9987.98,
                    "net_income_monthly": 9876.56,
                }
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = employment_update_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.success['status_code']

    def test_exception(self, django_db_blocker):
        current_time = django.utils.timezone.now()
        logger.info("Test for checking if the program throws an exception when db access is denied")
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
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "employment": {
                    "employment_id": create_employment.id,
                    "type": "salaried",
                    "employer_id": 1,
                    "designation_id": 2,
                    "gross_income_monthly": 9987.98,
                    "net_income_monthly": 9876.56,
                }
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        with django_db_blocker.block():
            response_obj = employment_update_service(data)
        assert response_obj["status"] == Statuses.generic_error_2["status_code"]

    def test_no_param(self):
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
        data = {}
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = employment_update_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.generic_error_1['status_code']

    def test_employer_id_is_zero(self):
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
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "employment": {
                    "employment_id": create_employment.id,
                    "type": "salaried",
                    "employer_id": 0,  # If employer id is zero then employer name should not be None
                    "employer_name": "",
                    "gross_income_monthly": 9987.98,
                    "net_income_monthly": 9876.56,
                    "other_income_monthly": 0,
                    "work_experience_month": 0
                }
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = employment_update_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.employer_name['status_code']

    def test_employer_id_is_non_zero(self):
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
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "employment": {
                    "employment_id": create_employment.id,
                    "type": "salaried",
                    "employer_id": 12,  # If employer id is non zero then employer name should be None
                    "employer_name": "abcd",
                    "gross_income_monthly": 9987.98,
                    "net_income_monthly": 9876.56,
                    "other_income_monthly": 0,
                    "work_experience_month": 0
                }
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = employment_update_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.employer_name['status_code']

    def test_designation_id_is_zero(self):
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
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "employment": {
                    "employment_id": create_employment.id,
                    "type": "salaried",
                    "employer_id": 12,
                    "designation_id": 0,  # If designation id is zero then designation name should not be None
                    "designation_name": "",
                    "gross_income_monthly": 9987.98,
                    "net_income_monthly": 9876.56,
                    "other_income_monthly": 0,
                    "work_experience_month": 0
                }
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = employment_update_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.designation_name['status_code']

    def test_designation_id_is_non_zero(self):
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
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "employment": {
                    "employment_id": create_employment.id,
                    "type": "salaried",
                    "employer_id": 12,  # If employer id is non zero then employer name should be None
                    "designation_id": 97,
                    "designation_name": "abcd",
                    "gross_income_monthly": 9987.98,
                    "net_income_monthly": 9876.56,
                    "other_income_monthly": 0,
                    "work_experience_month": 0
                }
            }
        }
        data = json.dumps(data)
        data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        response = employment_update_service(data)
        logger.info("response: %s", response)
        assert response['status'] == Statuses.designation_name['status_code']
