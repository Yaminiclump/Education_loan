import json
import logging
from types import SimpleNamespace

from django.http import JsonResponse
from rest_framework.decorators import api_view

from los.services.education_service import create_education_service, update_education
from los.status_code import Statuses

logger = logging.getLogger("django")

@api_view(["POST"])
def customer_education_create(request):
    response_obj = None
    try:
        logger.info("request: %s", request.body)

        if request.method == 'POST':
            logger.debug("response data: %s", request.body)
            data = json.loads(request.body.decode("utf-8"), object_hook=lambda d: SimpleNamespace(**d))
            response_obj = create_education_service(data)
            logger.debug("inserted education table")
        else:
            response_obj = {"status_code": Statuses.invalid_request["status_code"], "message": Statuses.invalid_request["message"]}

    except Exception:
        logger.exception("Exception: ")
        response_obj = {"status_code": Statuses.generic_error_2["status_code"], "message": Statuses.generic_error_2["message"]}

    logger.info("response: %s", response_obj)
    return JsonResponse(response_obj, safe=False)

@api_view(["POST"])
def update_education(request):
    response_obj = None
    try:
        logger.info("request: %s", request.body)

        if request.method == 'POST':
            logger.debug("response data: %s", request.body)
            data = json.loads(request.body.decode("utf-8"), object_hook=lambda d: SimpleNamespace(**d))
            response_obj = update_education(data)
            logger.debug("inserted education table")
        else:
            response_obj = {"status_code": Statuses.invalid_request["status_code"], "message": Statuses.invalid_request["message"]}

    except Exception:
        logger.exception("Exception: ")
        response_obj = {"status_code": Statuses.generic_error_2["status_code"], "message": Statuses.generic_error_2["message"]}

    logger.info("response: %s", response_obj)
    return JsonResponse(response_obj, safe=False)