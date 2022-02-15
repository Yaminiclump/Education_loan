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
        required=["message", "receiver"],
        properties={"message": openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["type", "template_id", "variables"],
            properties={"type": openapi.Schema(type=openapi.TYPE_INTEGER, description="notification type: sms=10, email=11, push notificationL: 12"),
                        "template_id": openapi.Schema(type=openapi.TYPE_INTEGER, description="template id"),
                        "variables": openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            required=["variable_1", "variable_2"],
                            properties={"variable_1": openapi.Schema(type=openapi.TYPE_STRING, description="name & value of variables"),
                                        "variable_2": openapi.Schema(type=openapi.TYPE_STRING, description="name & value of variables")
                                        },
                            description="define all the variable, put their name and values"),
                        }, description="message body"),
                    "receiver": openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            required=["receiver_info_1", "receiver_info_2"],
                            properties={"receiver_info_1": openapi.Schema(type=openapi.TYPE_STRING, description="email=email id, sms=mobile number, push notification=device id"),
                                        "receiver_info_2": openapi.Schema(type=openapi.TYPE_STRING, description="for future use")
                                        },
                            description="receiver details"),},
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
            logger.debug("finished create contact")
        else:
            response_obj = {"status_code": Statuses.invalid_request["status_code"], "message": Statuses.invalid_request["message"]}
    except Exception:
        logger.exception("Exception: ")
        response_obj = {"status_code": Statuses.generic_error_2["status_code"], "message": Statuses.generic_error_2["message"]}
    logger.info("response: %s", response_obj)
    return JsonResponse(response_obj, safe=False)

