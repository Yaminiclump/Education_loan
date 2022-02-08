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


def contact_service(req_data):
    response_obj = None
    logger.info("tryservice: %s", req_data)
    try:
        logger.info("request_service: %s", req_data)

        if req_data:
            customer = None
            if hasattr(req_data, 'customer'):
                customer = req_data.customer
                customer_id = get_value(customer, 'customer_id')
                contact = get_value(customer, 'contacts')

                # contacts = req_data.customer.contacts
                for i in contact:
                    type = get_value(i, "type")
                    value = get_value(i, "value")
                    value_extra_1 = get_value(i, "value_extra_1")
                    country_code = get_value(i, "country_code")
                    logger.info("for_loop: %s", type)

                # logger.info("get_contact: %s", req_data.customer.contacts)
                # logger.info("get_contactitem: %s", req_data.customer.contacts[0].type)
                # type = get_value(customer.contacts, 'type')

    except Exception as e:
        logger.exception("Exception: ")
        response_obj = get_response("generic_error_2")
        logger.info("response: %s", response_obj)
    return response_obj