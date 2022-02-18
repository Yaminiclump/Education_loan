import logging

import django.utils.timezone
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction

from los.constants import STATUS_ACTIVE, CREATION_BY, UPDATION_BY
from los.custom_helper import get_string_lower, get_value, validate_dict, validate_email, validate_mob, \
    set_db_attr_request, InvalidInputException
from los.los_dict import LosDictionary
from los.models.customer_contact_model import CustomerContact, CustomerContactLog
from los.models.customer_model import Customer
from los.models.empty_class import EmptyClass
from los.status_code import get_response, get_response_1, get_response_resp_var, Statuses

logger = logging.getLogger("django")


def customer_contact_create_service(req_data):
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
                contact_list = get_value(customer, 'contacts')

                if customer_id:
                    if type(customer_id) == int:
                        if not Customer.objects.filter(id=customer_id,status=1).exists():
                            response_obj = get_response(Statuses.customer_id_not_exist)
                            return response_obj
                        customer_id = customer_id
                    else:
                        response_obj = get_response(Statuses.customer_id_invalid_format)
                        return response_obj
                else:
                    response_obj = get_response(Statuses.customer_id_not_provided)
                    return response_obj
                contact_insert_ids = []
                counter = 1

                if contact_list:
                    try:
                        with transaction.atomic():

                            for contact in contact_list:
                                type_val = get_string_lower(contact, "type")
                                value = get_string_lower(contact, "value")
                                value_extra_1 = get_string_lower(contact, "value_extra_1")
                                country_code = get_value(contact, "country_code")
                                logger.info("type_val: %s", type_val)

                                if type_val is None:
                                    logger.debug("type_val is None...")
                                    raise InvalidInputException(get_response_resp_var(Statuses.contact_type, {"sequence": counter}))

                                if value is None:
                                    logger.debug("value is None...")
                                    raise InvalidInputException(get_response_resp_var(Statuses.contact_value, {"sequence": counter}))

                                # validation
                                type_val = validate_dict(type_val, LosDictionary.contact_type)
                                if type_val == dict():
                                    raise InvalidInputException(get_response_resp_var(Statuses.contact_type, {"sequence": counter}))

                                if type_val == LosDictionary.contact_type['mob']:
                                    check_mob = validate_mob(value)
                                    if check_mob == str():
                                        raise InvalidInputException(get_response_resp_var(Statuses.mobile_number, {"sequence": counter}))

                                    if country_code is None:
                                        raise InvalidInputException(get_response_resp_var(Statuses.contact_country_code, {"sequence": counter}))

                                if type_val == LosDictionary.contact_type['email']:
                                    check_email = validate_email(value)
                                    if check_email == str():
                                        raise InvalidInputException(get_response_resp_var(Statuses.email_address, {"sequence": counter}))

                                    if country_code is not None:
                                        raise InvalidInputException(get_response_resp_var(Statuses.contact_country_code, {"sequence": counter}))

                                current_time = django.utils.timezone.now()
                                logger.debug("current_time india: %s", current_time)
                                cust_contact = CustomerContact(
                                    type=type_val,
                                    value=value,
                                    value_extra_1=value_extra_1,
                                    country_code=country_code,
                                    status=STATUS_ACTIVE,
                                    creation_date=current_time,
                                    creation_by=CREATION_BY,
                                    customer_id=customer_id)
                                cust_contact.save()

                                cust_contact_log = CustomerContactLog()
                                cust_contact_log.__dict__ = cust_contact.__dict__.copy()
                                cust_contact_log.id = None
                                cust_contact_log.customer_contact = cust_contact
                                cust_contact_log.save()

                                logger.info("finished customer contact create...")
                                logger.debug("contact_id: %s", cust_contact.id)

                                contact_insert_ids.append(cust_contact.id)
                                counter = counter + 1

                                contacts = EmptyClass()
                                contacts = contact_insert_ids
                            response_obj = get_response_1(Statuses.success, {"contacts": contact_insert_ids})
                    except InvalidInputException as e:
                        logger.debug("Exception...")
                        response_obj = eval(str(e))
                else:
                    response_obj = get_response(Statuses.generic_error_1)
            else:
                response_obj = get_response(Statuses.generic_error_1)
        else:
            response_obj = get_response(Statuses.generic_error_1)
    except Exception as e:
        logger.exception("Exception: ")
        response_obj = get_response(Statuses.generic_error_2)
        logger.info("response: %s", response_obj)
    return response_obj


def customer_contact_update_service(req_data):
    response_obj = None
    try:
        logger.info("request_service: %s", req_data)
        if req_data:
            customer = None
            if hasattr(req_data, 'customer'):
                customer = req_data.customer
                customer_id = get_value(customer, 'customer_id')
                contact_list = get_value(customer, 'contacts')

                if customer_id:
                    if type(customer_id) == int:
                        if not Customer.objects.filter(id=customer_id,status=1).exists():
                            response_obj = get_response(Statuses.customer_id_not_exist)
                            return response_obj
                        customer_id = customer_id
                    else:
                        response_obj = get_response(Statuses.customer_id_invalid_format)
                        return response_obj
                else:
                    response_obj = get_response(Statuses.customer_id_not_provided)
                    return response_obj
                counter = 1
                if contact_list:
                    try:
                        with transaction.atomic():
                            for contact in contact_list:
                                variables = EmptyClass()
                                # set_obj_attr_request(contact, variables)
                                variables.contact_id = get_string_lower(contact, "contact_id")
                                variables.type = get_string_lower(contact, "type")
                                variables.value = get_string_lower(contact, "value")
                                variables.value_extra_1 = get_string_lower(contact, "value_extra_1")
                                variables.country_code = get_value(contact, "country_code")

                                customer_contact_db = None
                                if variables.contact_id:
                                        try:
                                            customer_contact_db = CustomerContact.objects.get(pk=variables.contact_id, customer_id=customer_id, status=1)
                                        except ObjectDoesNotExist as e:
                                            raise InvalidInputException(get_response(Statuses.customer_contact_id_not_exist))
                                else:
                                    raise InvalidInputException(get_response(Statuses.customer_contact_id_not_provided))

                                # validation
                                if variables.type is None:
                                    logger.debug("type_val is None...")
                                    raise InvalidInputException(get_response_resp_var(Statuses.contact_type, {"sequence": counter}))

                                if variables.value is None:
                                    logger.debug("value is None...")
                                    raise InvalidInputException(get_response_resp_var(Statuses.contact_value, {"sequence": counter}))

                                variables.type = validate_dict(variables.type, LosDictionary.contact_type)
                                logger.info("type: %s", variables.type)
                                if variables.type == dict():
                                    raise InvalidInputException(get_response(Statuses.contact_type, {"sequence": counter}))

                                if variables.type == LosDictionary.contact_type['mob']:
                                    check_mob = validate_mob(variables.value)
                                    if check_mob == str():
                                        raise InvalidInputException(get_response_resp_var(Statuses.mobile_number, {"sequence": counter}))

                                    if variables.country_code is None:
                                        raise InvalidInputException(get_response_resp_var(Statuses.contact_country_code, {"sequence": counter}))

                                if variables.type == LosDictionary.contact_type['email']:
                                    check_email = validate_email(variables.value)
                                    if check_email == str():
                                        raise InvalidInputException(get_response_resp_var(Statuses.email_address, {"sequence": counter}))

                                    if variables.country_code is not None:
                                        raise InvalidInputException(get_response_resp_var(Statuses.contact_country_code, {"sequence": counter}))

                                set_db_attr_request(customer_contact_db, contact, variables)
                                current_time = django.utils.timezone.now()
                                logger.debug("current_time india: %s", current_time)
                                customer_contact_db.updation_date = current_time
                                customer_contact_db.updation_by = UPDATION_BY
                                customer_contact_db.save()

                                cust_contact_log = CustomerContactLog()
                                cust_contact_log.__dict__ = customer_contact_db.__dict__.copy()
                                cust_contact_log.id = None
                                cust_contact_log.customer_contact = customer_contact_db
                                cust_contact_log.creation_date = current_time
                                cust_contact_log.creation_by = CREATION_BY
                                cust_contact_log.save()
                                logger.info("finished contact update service")
                                response_obj = get_response(Statuses.success)
                                counter = counter + 1

                    except InvalidInputException as e:
                        logger.debug("Exception...")
                        response_obj = eval(str(e))
                else:
                    response_obj = get_response(Statuses.generic_error_1)
                    return response_obj
            else:
                response_obj = get_response(Statuses.generic_error_1)
        else:
            response_obj = get_response(Statuses.generic_error_1)
    except Exception as e:
        logger.exception("Exception: ")
        response_obj = get_response(Statuses.generic_error_2)
        logger.info("response: %s", response_obj)
    return response_obj

