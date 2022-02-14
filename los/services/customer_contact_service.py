import logging
import django.utils.timezone
from los.status_code import get_response
from los.los_dict import LosDictionary
from los.custom_helper import get_string_lower, clean_string, get_value, validate_numeric,validate_dict,fetch_value,validate_email,validate_mob, set_db_attr_request,get_attributes
from los.models.customer_model import Customer
from los.models.customer_contact_model import CustomerContact, CustomerContactLog
from django.db import transaction
from los.models.empty_class import EmptyClass
from django.core.exceptions import ObjectDoesNotExist



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
                            response_obj = get_response("type_param")
                            return response_obj

                        if value is None:
                            response_obj = get_response("value_param")
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
                else:
                    response_obj = get_response("contact_param")
                    return response_obj
                current_time = django.utils.timezone.now()
                logger.debug("current_time india: %s", current_time)
                with transaction.atomic():
                    contact = CustomerContact(
                        type=type_val,
                        value=value,
                        value_extra_1=value_extra_1,
                        country_code=country_code,
                        status=1,
                        creation_date=current_time,
                        creation_by="System",
                        customer_id=customer_id)
                    contact.save()
                    contact_log = CustomerContactLog(
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
                variables = EmptyClass()
                variables.contact_id = get_value(customer, 'contact_id')
                # variables.customer_id = get_value(customer, 'customer_id')
                variables.contact = get_value(customer, 'contacts')

                contact_db = None
                if variables.contact_id:
                    try:
                        contact_db = CustomerContact.objects.get(pk=variables.contact_id)
                    except ObjectDoesNotExist as e:
                        response_obj = get_response("customer_id_not_exist")
                        return response_obj
                else:
                    response_obj = get_response("customer_id_not_exist")
                    return response_obj
                logger.debug("customer_db: %s", contact_db)

                if variables.contact:
                    counter = 0
                    for i in variables.contact:
                        logger.info("contact_val: %s",variables.contact)
                        type_val = get_value(i, "type")
                        value = get_value(i, "value")
                        value_extra_1 = get_value(i, "value_extra_1")
                        country_code = get_value(i, "country_code")


                        # validation
                        type_val = validate_dict(type_val, LosDictionary.type)
                        logger.info("type_val: %s", type_val)
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

                        set_db_attr_request(contact_db, customer.contacts[counter], variables.contact[counter])
                        logger.debug("get_db_object: %s", get_attributes(contact_db))
                        current_time = django.utils.timezone.now()
                        logger.debug("current_time india: %s", current_time)
                        contact_db.updation_date = current_time
                        contact_db.updation_by = "System"
                        contact_db.save()

                        contact_log = CustomerContactLog()
                        contact_log.__dict__ = contact_db.__dict__.copy()
                        contact_log.id = None
                        contact_log.customer = contact_db
                        contact_log.creation_date = current_time
                        contact_log.creation_by = "System"
                        contact_log.save()
                        logger.info("finished contact update service")
                        response_obj = get_response("success")
                        counter = counter+1
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