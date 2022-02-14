import logging
import django.utils.timezone
from los.status_code import get_response,prepare_response
from los.los_dict import LosDictionary
from los.custom_helper import get_string_lower, clean_string, get_value, validate_numeric,validate_dict,fetch_value,validate_email,validate_mob, set_db_attr_request, get_attributes
from los.models.customer_model import Customer
from los.models.customer_contact_model import CustomerContact, CustomerContactLog
from django.db import transaction
from los.models.empty_class import EmptyClass
from django.core.exceptions import ObjectDoesNotExist
from los.constants import STATUS_ACTIVE, CREATION_BY, UPDATION_BY


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
                contact_list = get_value(customer, 'contacts')

                if customer_id:
                    if type(customer_id) == int:
                        if not Customer.objects.filter(id=customer_id,status=1).exists():
                            response_obj = get_response("invalid_id")
                            return response_obj
                        customer_id = customer_id
                    else:
                        response_obj = get_response("invalid_id")
                        return response_obj
                else:
                    response_obj = get_response("invalid_id")
                    return response_obj
                contact_insert_ids = []
                counter = 1
                if contact_list:
                    for contact in contact_list:
                        type_val = get_string_lower(contact, "type")
                        value = get_string_lower(contact, "value")
                        value_extra_1 = get_string_lower(contact, "value_extra_1")
                        country_code = get_value(contact, "country_code")
                        logger.info("type_val: %s", type_val)

                        if type_val is None:
                            response_obj = get_response("type_param")
                            transaction.set_rollback(True)
                            return response_obj

                        if value is None:
                            response_obj = get_response("value_param")
                            transaction.set_rollback(True)
                            return response_obj

                        # validation
                        type_val = validate_dict(type_val, LosDictionary.contact_type)
                        if type_val == dict():
                            response_obj = prepare_response("type", "no", counter)
                            transaction.set_rollback(True)
                            return response_obj

                        if type_val == LosDictionary.contact_type['mob']:
                            check_mob = validate_mob(value)
                            if check_mob == str():
                                response_obj = prepare_response("mob_validate", "no", counter)
                                transaction.set_rollback(True)
                                return response_obj

                            if country_code is None:
                                response_obj = prepare_response("check_country_code", "no", counter)
                                transaction.set_rollback(True)
                                return response_obj

                        if type_val == LosDictionary.contact_type['email']:
                            check_email = validate_email(value)
                            if check_email == str():
                                response_obj = prepare_response("email_validate", "no", counter)
                                transaction.set_rollback(True)
                                return response_obj

                            if country_code is not None:
                                response_obj = prepare_response("country_code", "no", counter)
                                transaction.set_rollback(True)
                                return response_obj

                        current_time = django.utils.timezone.now()
                        logger.debug("current_time india: %s", current_time)
                        with transaction.atomic():
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

                            cust_contact_log = CustomerContactLog(
                                type=type_val,
                                value=value,
                                value_extra_1=value_extra_1,
                                country_code=country_code,
                                status=STATUS_ACTIVE,
                                creation_date=current_time,
                                creation_by=CREATION_BY,
                                customer_id=customer_id,
                                customercontact_id=cust_contact.id)
                            cust_contact_log.save()
                        logger.info("finished contact create service")
                        logger.debug("contact_id: %s", cust_contact.id)
                        contact_insert_ids.append(cust_contact.id)
                        counter = counter+1
                    response_obj = get_response("success", {"contact_id": contact_insert_ids})
                else:
                    response_obj = get_response("contact_param")
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
                customer_id = get_value(customer, 'customer_id')
                contact_list = get_value(customer, 'contacts')

                if customer_id:
                    if type(customer_id) == int:
                        if not Customer.objects.filter(id=customer_id,status=1).exists():
                            response_obj = get_response("invalid_id")
                            return response_obj
                        customer_id = customer_id
                    else:
                        response_obj = get_response("invalid_id")
                        return response_obj
                else:
                    response_obj = get_response("invalid_id")
                    return response_obj
                counter = 1
                if contact_list:
                    for contact in contact_list:
                        variables = EmptyClass()
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
                                response_obj = get_response("invalid_id")
                                return response_obj
                        else:
                            response_obj = get_response("invalid_id")
                            return response_obj

                        # validation
                        variables.type = validate_dict(variables.type, LosDictionary.contact_type)
                        logger.info("type: %s", variables.type)
                        if variables.type == dict():
                            response_obj = prepare_response("type", "no", counter)
                            return response_obj

                        if variables.type is None:
                            variables.type = customer_contact_db.type

                        if variables.type == LosDictionary.contact_type['mob']:
                            check_mob = validate_mob(variables.value)
                            if check_mob == str():
                                response_obj = prepare_response("mob_validate", "no", counter)
                                return response_obj

                            if variables.country_code is None:
                                response_obj = prepare_response("check_country_code", "no", counter)
                                return response_obj

                        if variables.type == LosDictionary.contact_type['email']:
                            check_email = validate_email(variables.value)
                            if check_email == str():
                                response_obj = prepare_response("email_validate", "no", counter)
                                return response_obj

                            if variables.country_code is not None:
                                response_obj = prepare_response("country_code", "no", counter)
                                return response_obj

                        set_db_attr_request(customer_contact_db, contact, variables)
                        current_time = django.utils.timezone.now()
                        logger.debug("current_time india: %s", current_time)
                        customer_contact_db.updation_date = current_time
                        customer_contact_db.updation_by = UPDATION_BY
                        customer_contact_db.save()

                        cust_contact_log = CustomerContactLog()
                        cust_contact_log.__dict__ = customer_contact_db.__dict__.copy()
                        cust_contact_log.id = None
                        cust_contact_log.customercontact = customer_contact_db
                        cust_contact_log.creation_date = current_time
                        cust_contact_log.creation_by = CREATION_BY
                        cust_contact_log.save()
                        logger.info("finished contact update service")
                        response_obj = get_response("success")
                        counter = counter + 1
                else:
                    response_obj = get_response("contact_param")
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