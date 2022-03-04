import json
import logging

import django.utils.timezone
import pytest
from django.urls import reverse

from los.models import Customer
from los.models import Education
from los.status_code import Statuses
from los.tests.test_education_service import customer_insert, education_insert

logger = logging.getLogger("django")


@pytest.mark.django_db
class TestEducationCreateView:

    def test_create_education_view_get(self, client):

        url = reverse('education_create')
        response = client.get(url)
        logger.info("response for get method : %s", response)
        assert response.status_code == Statuses.test_get['status_code']

    def test_create_education_view_post(self, client):
        current_time = django.utils.timezone.now()
        logger.debug("current_time india: %s", current_time)
        create_customer = customer_insert()
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "educations": [
                    {
                        "institute_id": "1",
                        "course_id": "1",
                        "stream_id": "1",
                        "end_month_year": "2022-06",
                        "marks": "93",
                        "max_marks": "100",
                        "marks_type": "percentage",
                        "duration_months": "48",
                        "course_type": "full_time"
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

    def test_update_education_view_get(self, client):
        url = reverse('education_update')
        response = client.get(url)
        logger.info("response for get method : %s", response)
        assert response.status_code == Statuses.test_get['status_code']

    def test_update_education_view_post(self,client):
        current_time = django.utils.timezone.now()
        logger.debug("current_time india: %s", current_time)
        create_customer = customer_insert()
        create_customer.save()

        current_time = django.utils.timezone.now()
        logger.debug("current_time india: %s", current_time)
        create_education1 = Education(
            institute_id= "1",
            course_id= "1",
            stream_id= "1",
            end_month_year= "2022-06",
            marks= "93",
            max_marks= "100",
            marks_type= "percentage",
            duration_months= "48",
            course_type= "full_time",
            status=1,
            creation_date=current_time,
            creation_by="System",
            customer_id=create_customer.id
        )

        create_education1.save()
        data = {
            "customer": {
                "customer_id": create_customer.id,
                "educations": [
                    {
                        "institute_id": "1",
                        "course_id": "1",
                        "stream_id": "1",
                        "end_month_year": "2022-06",
                        "marks": "93",
                        "max_marks": "100",
                        "marks_type": "percentage",
                        "duration_months": "48",
                        "course_type": "full_time"
                    }
                ]

            }
        }
        url = reverse('education_update')
        data = json.dumps(data)
        response = client.post(url, data=data, content_type='application/json')
        logger.info("response for post method: %s", response)
        assert response.status_code == Statuses.test_post['status_code']


