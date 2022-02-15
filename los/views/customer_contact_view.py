import json
import logging
from types import SimpleNamespace

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view

from los.services.customer_contact_service import contact_service, contact_update
from los.status_code import Statuses

logger = logging.getLogger("django")


@csrf_exempt
@swagger_auto_schema(
    method="post",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=["customer"],
        properties={"customer": openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["customer_id", "contacts"],
            properties={"customer_id": openapi.Schema(type=openapi.TYPE_INTEGER, description="customer id"),
                        "contacts": openapi.Items(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Items(
                                type=openapi.TYPE_OBJECT,
                                required=["type", "value"],
                                properties={
                                    "type": openapi.Schema(type=openapi.TYPE_STRING, description="mob:10, email:11"),
                                    "value": openapi.Schema(type=openapi.TYPE_STRING, description="value"),
                                    "value_extra_1": openapi.Schema(type=openapi.TYPE_STRING, description="value"),
                                    "country_code": openapi.Schema(type=openapi.TYPE_INTEGER, description="country code"),
                                }),
                            description="define all the variable, put their name and values"),
                        }, description="message body"),
                    },
    ),
    operation_id="payload",
)
@api_view(["POST"])
def customer_contact(request):
    response_obj = None
    try:
        logger.info("request: %s", request.body)

        if request.method == 'POST':
            data = json.loads(request.body.decode("utf-8"), object_hook=lambda d: SimpleNamespace(**d))
            response_obj = contact_service(data)
            logger.debug("finished create contact")
        else:
            response_obj = {"status_code": Statuses.invalid_request["status_code"], "message": Statuses.invalid_request["message"]}
    except Exception:
        logger.exception("Exception: ")
        response_obj = {"status_code": Statuses.generic_error_2["status_code"], "message": Statuses.generic_error_2["message"]}
    logger.info("response: %s", response_obj)
    return JsonResponse(response_obj, safe=False)

@csrf_exempt
@swagger_auto_schema(
    method="post",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=["customer"],
        properties={"customer": openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["contact_id", "customer_id", "contacts"],
            properties={"customer_id": openapi.Schema(type=openapi.TYPE_INTEGER, description="customer id"),
                        "contacts": openapi.Items(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Items(
                                type=openapi.TYPE_OBJECT,
                                properties={
                                    "contact_id": openapi.Schema(type=openapi.TYPE_INTEGER, description="contact id"),
                                    "type": openapi.Schema(type=openapi.TYPE_STRING, description="mob:10, email:11"),
                                    "value": openapi.Schema(type=openapi.TYPE_STRING, description="value"),
                                    "value_extra_1": openapi.Schema(type=openapi.TYPE_STRING, description="value"),
                                    "country_code": openapi.Schema(type=openapi.TYPE_INTEGER, description="country code"),
                                }),
                            description="define all the variable, put their name and values"),
                        }, description="message body"),
                    },
    ),
    operation_id="payload",
)
@api_view(["POST"])
def update_contact(request):
    response_obj = None
    try:
        logger.info("request: %s", request.body)

        if request.method == 'POST':
            data = json.loads(request.body.decode("utf-8"), object_hook=lambda d: SimpleNamespace(**d))
            response_obj = contact_update(data)
            logger.debug("finished contact update")
        else:
            response_obj = {"status_code": Statuses.invalid_request["status_code"], "message": Statuses.invalid_request["message"]}
    except Exception:
        logger.exception("Exception: ")
        response_obj = {"status_code": Statuses.generic_error_2["status_code"], "message": Statuses.generic_error_2["message"]}
    logger.info("response: %s", response_obj)
    return JsonResponse(response_obj, safe=False)
