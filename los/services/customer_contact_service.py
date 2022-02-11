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
from los.custom_helper import get_string_lower, clean_string, get_value, validate_numeric,validate_dict,fetch_value,validate_email,validate_mob
from los.models.customer_model import Customer
from los.models.customer_contact_model import Contact, ContactLog
logger = logging.getLogger("django")


def contact_service(req_data):
    response_obj = None
    logger.info("service_request: %s", req_data)
    try:
        logger.info("request_service: %s", req_data)
        if req_data:
            customer = None
            if hasattr(req_data, 'customer'):
                customer = req_data.customer
                logger.info("customer_get: %s",req_data.customer)
                customer_id = get_value(customer, 'customer_id')
                contact = get_value(customer, 'contacts')

                if customer_id:
                    if type(customer_id) == int:
                        if not Customer.objects.filter(id=customer_id).exists():
                            response_obj = get_response("customer_id_not_exist")
                            return response_obj
                        customer_id = customer_id
                    else:
                        response_obj = get_response("check_numeric")
                        return response_obj
                else:
                    response_obj = get_response("customer_id_not_exist")
                    return response_obj

                if contact:
                    for i in contact:
                        type_val = get_value(i, "type")
                        value = get_value(i, "value")
                        value_extra_1 = get_value(i, "value_extra_1")
                        country_code = get_value(i, "country_code")
                        logger.info("type_val: %s", type_val)

                        if type_val is None:
                            response_obj = get_response("check_parameter")
                            return response_obj

                        if value is None:
                            response_obj = get_response("check_parameter")
                            return response_obj

                        # validation
                        type_val = validate_dict(type_val, LosDictionary.type)
                        if type_val == dict():
                            response_obj = get_response("type")
                            return response_obj

                        if type_val == 10:
                            check_mob = validate_mob(value)
                            if check_mob == str():
                                response_obj = get_response("mob_validate")
                                return response_obj

                            if country_code is None:
                                response_obj = get_response("check_country_code")
                                return response_obj

                        if type_val == 11:
                            check_email = validate_email(value)
                            if check_email == str():
                                response_obj = get_response("email_validate")
                                return response_obj

                        logger.info("dict_type: %s", type_val)
                        current_time = django.utils.timezone.now()
                        logger.debug("current_time india: %s", current_time)
                        contact = Contact(
                            type=type_val,
                            value=value,
                            value_extra_1=value_extra_1,
                            country_code=country_code,
                            status=1,
                            creation_date=current_time,
                            creation_by="System",
                            customer_id=customer_id)
                        contact.save()
                        contact_log = ContactLog(
                                type=type_val,
                                value=value,
                                value_extra_1=value_extra_1,
                                country_code=country_code,
                                status=1,
                                creation_date=current_time,
                                creation_by="System",
                                customer_id=customer_id)
                        contact_log.save()
                        logger.info("inserted in contact audit table")
                        response_obj = get_response("success")
                else:
                    response_obj = get_response("check_parameter")
                    return response_obj
            else:
                response_obj = get_response("check_parameter")
        else:
            response_obj = get_response("generic_error_1")
    except Exception as e:
        logger.exception("Exception: ")
        response_obj = get_response("generic_error_2")
        logger.info("response: %s", response_obj)
    return response_obj



def contact_update(req_data):
    response_obj = None
    logger.info("service_request: %s", req_data)
    try:
        logger.info("request_service: %s", req_data)
        if req_data:
            customer = None
            if hasattr(req_data, 'customer'):
                customer = req_data.customer
                logger.info("get_response: %s", req_data.customer)
                contact_id = get_value(customer, 'contact_id')
                customer_id = get_value(customer, 'customer_id')
                contact = get_value(customer, 'contacts')

                if contact_id and customer_id:
                    if type(contact_id) == int and type(customer_id) == int:
                        if not Contact.objects.filter(id=contact_id, customer_id=customer_id).exists():
                            response_obj = get_response("id_error")
                            return response_obj
                        contact_id = contact_id
                    else:
                        response_obj = get_response("check_numeric")
                        return response_obj
                else:
                    response_obj = get_response("customer_id_not_exist")
                    return response_obj
                get_contact = Contact.objects.filter(id=contact_id)
                if contact:
                    for i in contact:
                        type_val = get_value(i, "type")
                        value = get_value(i, "value")
                        value_extra_1 = get_value(i, "value_extra_1")
                        country_code = get_value(i, "country_code")
                        logger.info("type_val: %s", type_val)

                        # validation
                        type_val = validate_dict(type_val, LosDictionary.type)
                        if type_val == dict():
                            response_obj = get_response("type")
                            return response_obj

                        if type_val == 10:
                            check_mob = validate_mob(value)
                            if check_mob == str():
                                response_obj = get_response("mob_validate")
                                return response_obj
                            if country_code is None:
                                response_obj = get_response("check_country_code")
                                return response_obj

                        if type_val == 11:
                            check_email = validate_email(value)
                            if check_email == str():
                                response_obj = get_response("email_validate")
                                return response_obj

                        if type_val is None:
                            type_val = fetch_value(contact, get_contact, 'type')

                        if value is None:
                            value = fetch_value(contact, get_contact, 'value')

                        if country_code is None:
                            country_code = fetch_value(contact, get_contact, 'country_code')

                        if value_extra_1 is None:
                            value_extra_1 = fetch_value(contact, get_contact, 'value_extra_1')

                        logger.info("dict_type: %s", type_val)
                        logger.info("get_id: %s", type_val)
                        current_time = django.utils.timezone.now()
                        logger.debug("current_time india: %s", current_time)

                        # update
                        contact = Contact.objects.get(pk=contact_id)
                        contact.type = type_val
                        contact.value = value
                        contact.value_extra_1 = value_extra_1
                        contact.status = 1
                        contact.updation_date = current_time
                        contact.updation_by = "System"
                        contact.customer_id = customer_id
                        contact.save()
                        contact_log = ContactLog(
                            type=type_val,
                            value=value,
                            value_extra_1=value_extra_1,
                            country_code=country_code,
                            status=1,
                            creation_date=current_time,
                            creation_by="System",
                            customer_id=customer_id)
                        contact_log.save()
                        logger.info("inserted in contact audit table")
                        response_obj = get_response("success")
                else:
                    response_obj = get_response("check_parameter")
                    return response_obj
            else:
                response_obj = get_response("check_parameter")
        else:
            response_obj = get_response("generic_error_1")
    except Exception as e:
        logger.exception("Exception: ")
        response_obj = get_response("generic_error_2")
        logger.info("response: %s", response_obj)
    return response_obj