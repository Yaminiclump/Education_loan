import json
import logging
from types import SimpleNamespace
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view, parser_classes
from los.services.customer_contact_service import contact_service
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
            properties={"customer_id": openapi.Schema(type=openapi.TYPE_INTEGER, description=""),
                        "contacts": openapi.Items(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Items(
                                type=openapi.TYPE_OBJECT,
                                required=["type", "value"],
                                properties={
                                    "type": openapi.Schema(type=openapi.TYPE_INTEGER, description=""),
                                    "value": openapi.Schema(type=openapi.TYPE_STRING, description="name & value of variables"),
                                    "value_extra_1": openapi.Schema(type=openapi.TYPE_STRING, description="name & value of variables"),
                                    "country_code": openapi.Schema(type=openapi.TYPE_STRING, description="name & value of variables"),
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
            logger.debug("post_data: %s", request.body)

            data = json.loads(request.body.decode("utf-8"), object_hook=lambda d: SimpleNamespace(**d))
            logger.debug("post_after: %s", data.customer.customer_id)

            response_obj = contact_service(data)
            logger.debug("customer_obj: %s", response_obj)
            logger.debug("inserted customer and audit table")
            logger.info("response: %s", data)
            return HttpResponse(data)
        else:
            response_obj = {"status_code": Statuses.invalid_request["status_code"], "message": Statuses.invalid_request["message"]}

    except Exception:
        logger.exception("Exception: ")
        response_obj = {"status_code": Statuses.generic_error_2["status_code"], "message": Statuses.generic_error_2["message"]}
    logger.info("response: %s", "innnnn")
    return JsonResponse(response_obj, safe=False)
