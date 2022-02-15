import json
import logging
from types import SimpleNamespace
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from los.status_code import Statuses
from los.services.employment_service import employment_create
logger = logging.getLogger("django")


@csrf_exempt
@swagger_auto_schema(
    method="post",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=["customer"],
        properties={"customer": openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["customer_id", "employment"],
            properties={"customer_id": openapi.Schema(type=openapi.TYPE_INTEGER, description="customer id"),
                        "employment": openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            required=["gross_income_monthly", "net_income_monthly"],
                            properties={"type": openapi.Schema(type=openapi.TYPE_STRING, description="11:salaried, 12:self_employed,13:professional, 14:retired, 15:others"),
                                        "employer_id": openapi.Schema(type=openapi.TYPE_INTEGER, description="employer id"),
                                        "employer_name": openapi.Schema(type=openapi.TYPE_STRING, description="employer name"),
                                        "address_id": openapi.Schema(type=openapi.TYPE_INTEGER, description="address id"),
                                        "designation_id": openapi.Schema(type=openapi.TYPE_INTEGER, description="designation id"),
                                        "designation_name": openapi.Schema(type=openapi.TYPE_STRING, description="designation name"),
                                        "retirement_age_years": openapi.Schema(type=openapi.TYPE_INTEGER, description="retirement age years"),
                                        "current_employer_months": openapi.Schema(type=openapi.TYPE_INTEGER, description="current employer months"),
                                        "gross_income_monthly": openapi.Schema(type=openapi.TYPE_INTEGER, description="gross income monthly"),
                                        "net_income_monthly": openapi.Schema(type=openapi.TYPE_INTEGER, description="net income monthly"),
                                        "other_income_monthly": openapi.Schema(type=openapi.TYPE_INTEGER, description="other income monthly"),
                                        "work_experience_month": openapi.Schema(type=openapi.TYPE_INTEGER, description="work experience month"),
                                        },
                            description="define all the variable, put their name and values"),
                        }, description="message body"),
        },
    ),
    operation_id="payload",
)
@api_view(["POST"])
def create_empolyment(request):
    response_obj = None
    try:
        logger.info("request: %s", request.body)

        if request.method == 'POST':
            data = json.loads(request.body.decode("utf-8"), object_hook=lambda d: SimpleNamespace(**d))
            response_obj = employment_create(data)
            logger.debug("finished create employment")
        else:
            response_obj = {"status_code": Statuses.invalid_request["status_code"], "message": Statuses.invalid_request["message"]}
    except Exception:
        logger.exception("Exception: ")
        response_obj = {"status_code": Statuses.generic_error_2["status_code"], "message": Statuses.generic_error_2["message"]}
    logger.info("response: %s", response_obj)
    return JsonResponse(response_obj, safe=False)

