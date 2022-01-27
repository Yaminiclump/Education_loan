
from django.http import JsonResponse, HttpResponse
import json
import logging
from types import SimpleNamespace
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from drf_yasg import openapi
from drf_yasg.inspectors import SwaggerAutoSchema
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view, parser_classes
from los.error_code import errors
from los.services.customer_update_service import update_customer
logger = logging.getLogger("django")


@csrf_exempt
@swagger_auto_schema(
    method="post",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=[
            "salutation", "first_name", "middle_name", "last_name", "gender", "date_of_birth",
            "relation_with_applicant", "marital_status", "father_first_name", "father_middle_name",
            "father_last_name", "mother_first_name", "mother_middle_name", "mother_last_name",
            "spouse_first_name", "spouse_middle_name", "spouse_last_name", "no_of_family_members",
            "household_income_monthly"
        ],
        properties={"customer_id": openapi.Schema(type=openapi.TYPE_STRING, description="customer Id")
                    "salutation": openapi.Schema(type=openapi.TYPE_STRING, description="mr:1, mrs:2, dr:3 undefined:0"),
                    "first_name": openapi.Schema(type=openapi.TYPE_STRING, description="first name"),
                    "middle_name": openapi.Schema(type=openapi.TYPE_STRING, description="middle name"),
                    "last_name": openapi.Schema(type=openapi.TYPE_STRING, description="last name"),
                    "gender": openapi.Schema(type=openapi.TYPE_STRING, description="male:1, female:2, trans:3, will_hide:0"),
                    "date_of_birth": openapi.Schema(type=openapi.TYPE_STRING, description="date should be in YYYY-MM-DD format"),
                    "relation_with_applicant": openapi.Schema(type=openapi.TYPE_INTEGER, description="self:0, father:1, mother:2, brother:3"),
                    "marital_status": openapi.Schema(type=openapi.TYPE_STRING, description="married:1, single:2,separated:3, will_hide:0"),
                    "father_first_name": openapi.Schema(type=openapi.TYPE_STRING, description="father first name"),
                    "father_middle_name": openapi.Schema(type=openapi.TYPE_STRING, description="father middle name"),
                    "father_last_name": openapi.Schema(type=openapi.TYPE_STRING, description="father last name"),
                    "mother_first_name": openapi.Schema(type=openapi.TYPE_STRING, description="mother first name"),
                    "mother_middle_name": openapi.Schema(type=openapi.TYPE_STRING, description="mother middle name"),
                    "mother_last_name": openapi.Schema(type=openapi.TYPE_STRING, description="mother last name"),
                    "spouse_first_name": openapi.Schema(type=openapi.TYPE_STRING, description="spouse first name"),
                    "spouse_middle_name": openapi.Schema(type=openapi.TYPE_STRING, description="spouse middle name"),
                    "spouse_last_name": openapi.Schema(type=openapi.TYPE_STRING, description="spouse last name"),
                    "no_of_family_members": openapi.Schema(type=openapi.TYPE_INTEGER, description="no of family members"),
                    "household_income_monthly": openapi.Schema(type=openapi.TYPE_INTEGER, description="household income monthly"),

                    },
    ),
    operation_id="payload",
)

@api_view(["POST"])
def customer_update(request):
    response_obj = None
    try:
        logger.info("request: %s", request.body)

        if request.method == 'POST':
            logger.debug("response data: %s", request.body)
            data = json.loads(request.body.decode("utf-8"), object_hook=lambda d: SimpleNamespace(**d))
            response_obj = update_customer(data)
            logger.debug("inserted customer and audit table")
        else:
            response_obj = {"error_code": errors.invalid_request["error_code"], "message": errors.invalid_request["message"]}

    except Exception:
        logger.exception("Exception: ")
        response_obj = {"error_code": errors.generic_error_2["error_code"], "message": errors.generic_error_2["message"]}

    logger.info("response: %s", response_obj)
    return JsonResponse(response_obj, safe=False)

