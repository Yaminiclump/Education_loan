import logging
from io import BytesIO
import django.utils.timezone
from django.core.files.storage import default_storage
from los.status_code import get_response
from los.models.customer_contact_model import Contact
from los.los_dict import LosDictionary
from django.http import JsonResponse,HttpResponse
import datetime
from datetime import datetime,date
from los.custom_helper import get_string_lower, clean_string, get_value, validate_numeric,validate_dict,fetch_value
logger = logging.getLogger("django")



def customer_contact(req_data):
    response_obj = None
    try:
        logger.info("request: %s", req_data)
        if req_data:
            customer = None
            if hasattr(req_data, 'customer'):
                customer = req_data.customer
                customer_id = get_value(customer, 'customer_id')
                logger.info("response_data: %s", customer_id)
                response_obj = get_response("success")
                return response_obj
    except Exception as e:
        logger.exception("Exception: ")
        response_obj = get_response("generic_error_2")
        logger.info("response: %s", response_obj)
    return response_obj