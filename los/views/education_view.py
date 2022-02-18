import json
import logging
from types import SimpleNamespace
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view, parser_classes
from los.services.education_service import education_create_service, education_update_service
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
            required=["customer_id", "institute_id","course_id","stream_id","end_month_year","marks","max_marks","marks_type","status"],
            properties={"customer_id": openapi.Schema(type=openapi.TYPE_INTEGER, description="customer id"),
                        "educations": openapi.Items(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Items(
                                type=openapi.TYPE_OBJECT,
                                required=["institute_id", "institute_name","course_id","course_name","stream_id","stream_name","marks","max_marks"],
                                properties={
                                    "institute_id": openapi.Schema(type=openapi.TYPE_INTEGER, description="institute_id"),
                                    "institute_name": openapi.Schema(type=openapi.TYPE_STRING, description="institute_name"),
                                    "course_id": openapi.Schema(type=openapi.TYPE_INTEGER, description="course_id"),
                                    "course_name": openapi.Schema(type=openapi.TYPE_STRING, description="course_name"),
                                    "stream_id": openapi.Schema(type=openapi.TYPE_INTEGER, description="stream_id"),
                                    "stream_name": openapi.Schema(type=openapi.TYPE_STRING, description="stream_name"),
                                    "start_month_year": openapi.Schema(type=openapi.TYPE_INTEGER, description="In yyyy-mm"),
                                    "end_month_year": openapi.Schema(type=openapi.TYPE_INTEGER, description="In yyyy-mm"),
                                    "marks": openapi.Schema(type=openapi.TYPE_INTEGER, description="marks or cgpa obtained"),
                                    "max_marks": openapi.Schema(type=openapi.TYPE_INTEGER, description="max_marks"),
                                    "marks_type": openapi.Schema(type=openapi.TYPE_INTEGER, description="percentage/cgpa"),
                                    "duration_months": openapi.Schema(type=openapi.TYPE_INTEGER, description="duration"),
                                    "course_type": openapi.Schema(type=openapi.TYPE_INTEGER, description="full_time/part_time"),

                                }),
                            description="define all the variable, put their name and values"),
                        }, description="message body"),
                    },
    ),
    operation_id="payload",
)
@api_view(["POST"])
def education_create(request):
    response_obj = None
    try:
        logger.info("request: %s", request.body)

        if request.method == 'POST':
            data = json.loads(request.body.decode("utf-8"), object_hook=lambda d: SimpleNamespace(**d))
            response_obj = education_create_service(data)
            logger.debug("finished create education")
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
            required=["customer_id", "institute_id","course_id","stream_id","end_month_year","marks","max_marks","marks_type","status"],
            properties={"customer_id": openapi.Schema(type=openapi.TYPE_INTEGER, description="customer id"),
                        "educations": openapi.Items(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Items(
                                type=openapi.TYPE_OBJECT,
                                properties={
                                    "institute_id": openapi.Schema(type=openapi.TYPE_INTEGER, description="institute_id"),
                                    "institute_name": openapi.Schema(type=openapi.TYPE_STRING, description="institute_name"),
                                    "course_id": openapi.Schema(type=openapi.TYPE_INTEGER, description="course_id"),
                                    "course_name": openapi.Schema(type=openapi.TYPE_STRING, description="course_name"),
                                    "stream_id": openapi.Schema(type=openapi.TYPE_INTEGER, description="stream_id"),
                                    "stream_name": openapi.Schema(type=openapi.TYPE_STRING, description="stream_name"),
                                    "start_month_year": openapi.Schema(type=openapi.TYPE_INTEGER, description="In yyyy-mm"),
                                    "end_month_year": openapi.Schema(type=openapi.TYPE_INTEGER, description="In yyyy-mm"),
                                    "marks": openapi.Schema(type=openapi.TYPE_INTEGER, description="marks or cgpa obtained"),
                                    "max_marks": openapi.Schema(type=openapi.TYPE_INTEGER, description="max_marks"),
                                    "marks_type": openapi.Schema(type=openapi.TYPE_INTEGER, description="percentage/cgpa"),
                                    "duration_months": openapi.Schema(type=openapi.TYPE_INTEGER, description="duration"),
                                    "course_type": openapi.Schema(type=openapi.TYPE_INTEGER, description="full_time/part_time"),
                                }),
                            description="define all the variable, put their name and values"),
                        }, description="message body"),
                    },
    ),
    operation_id="payload",
)
@api_view(["POST"])
def education_update(request):
    response_obj = None
    try:
        logger.info("request: %s", request.body)

        if request.method == 'POST':
            data = json.loads(request.body.decode("utf-8"), object_hook=lambda d: SimpleNamespace(**d))
            response_obj = education_update_service(data)
            logger.debug("finished education update")
        else:
            response_obj = {"status_code": Statuses.invalid_request["status_code"], "message": Statuses.invalid_request["message"]}
    except Exception:
        logger.exception("Exception: ")
        response_obj = {"status_code": Statuses.generic_error_2["status_code"], "message": Statuses.generic_error_2["message"]}
    logger.info("response: %s", response_obj)
    return JsonResponse(response_obj, safe=False)
