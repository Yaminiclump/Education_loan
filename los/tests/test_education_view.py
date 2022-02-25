import json
import logging

import django.utils.timezone
import pytest
from django.urls import reverse

from los.models import Customer
from los.models import Education
from los.status_code import Statuses

logger = logging.getLogger("django")


@pytest.mark.django_db
class TestEducationCreateView:

    def test_create_education_view_GET(self, client):

        url = reverse('education_create')
        response = client.get(url)
        logger.info("response for get method : %s", response)
        assert response.status_code == Statuses.test_get['status_code']

    def test_create_education_view_POST(self, client):
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
                "educations": [
                    {
                        "institute_id": "1",
                        "institute_name": "string",
                        "course_id": "0",
                        "course_name": "string",
                        "stream_id": "0",
                        "stream_name": "string",
                        "start_month_year": "2022-05-11",
                        "end_month_year": "2022-11-01",
                        "marks": "10",
                        "max_marks": "0",
                        "marks_type": "string",
                        "duration_months": "0",
                        "course_type": "string"
                    },
                    {
                        "marks_type": "string",
                        "marks": "10"
                    },
                    {
                        "course_type": "string",
                        "duration": "0"
                    }
                ]

            }
        }

        url = reverse('education_create')
        data = json.dumps(data)
        response = client.post(url, data=data, content_type='application/json')
        logger.info("response for post method: %s", response)
        assert response.status_code == Statuses.test_post['status_code']


@pytest.mark.django_db
class TestEducationUpdateView():

    def test_update_education_view_GET(self, client):
        url = reverse('education_update')
        response = client.get(url)
        logger.info("response for get method : %s", response)
        assert response.status_code == Statuses.test_get['status_code']

    def test_update_education_view_POST(self,client):
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
        create_education1 = Education(
            institute_id= 1,
            institute_name= "string",
            course_id= 0,
            course_name= "string",
            stream_id= 0,
            stream_name= "string",
            start_month_year= "2022-05-11",
            end_month_year= "2022-11-01",
            marks= 10,
            max_marks= 0,
            marks_type= "string",
            duration_months= 0,
            course_type= "string",
            status=1,
            creation_date=current_time,
            creation_by="System",
            customer_id=create_customer.id
        )
        create_education1.save()

        current_time = django.utils.timezone.now()
        logger.debug("current_time india: %s", current_time)
        create_education2 = Education(
            institute_id= 1,
            institute_name= "string",
            course_id= 0,
            course_name= "string",
            stream_id= 0,
            stream_name= "string",
            start_month_year= "2022-05-11",
            end_month_year= "2022-11-01",
            marks= 10,
            max_marks= 0,
            marks_type= "string",
            duration_months= 0,
            course_type= "string",
            status=1,
            creation_date=current_time,
            creation_by="System",
            customer_id=create_customer.id
        )
        create_education2.save()
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "educations": [
                    {
                        "education_id": create_education1.id,
                        "marks_type": "string",
                        "marks": "10"
                    },
                    {
                        "education_id": create_education2.id,
                        "course_type": "string",
                        "duration": "0"
                    }
                ]

            }
        }
        url = reverse('education_update')
        data = json.dumps(data)
        response = client.post(url, data=data, content_type='application/json')
        logger.info("response for post method: %s", response)
        assert response.status_code == Statuses.test_post['status_code']