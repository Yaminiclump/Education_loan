import logging

import django.utils.timezone
from django.core.exceptions import ObjectDoesNotExist

from los.custom_helper import get_string_lower, get_value, validate_numeric, validate_dict, validate_date, \
    set_db_attr_request
from los.los_dict import LosDictionary
from los.models.customer_auditlog_model import Customerauditlog
from los.models.customer_model import Customer
from los.models.empty_class import EmptyClass
from los.status_code import get_response

logger = logging.getLogger("django")


def create_service(req_data):
    response_obj = None

    try:
        logger.info("request: %s", req_data)

        if req_data:
            customer = None
            if hasattr(req_data, 'customer'):
                customer = req_data.customer

                salutation = get_string_lower(customer, 'salutation')
                first_name = get_string_lower(customer, 'first_name')
                middle_name = get_string_lower(customer, 'middle_name')
                last_name = get_string_lower(customer, 'last_name')
                gender = get_string_lower(customer, 'gender')
                date_of_birth = get_string_lower(customer, 'date_of_birth')

                relation_with_applicant = get_string_lower(customer, 'relation_with_applicant')
                marital_status = get_string_lower(customer, 'marital_status')
                father_first_name = get_string_lower(customer, 'father_first_name')
                father_middle_name = get_string_lower(customer, 'father_middle_name')
                father_last_name = get_string_lower(customer, 'father_last_name')

                mother_first_name = get_string_lower(customer, 'mother_first_name')
                mother_middle_name = get_string_lower(customer, 'mother_middle_name')
                mother_last_name = get_string_lower(customer, 'mother_last_name')

                spouse_first_name = get_string_lower(customer, 'spouse_first_name')
                spouse_middle_name = get_string_lower(customer, 'spouse_middle_name')
                spouse_last_name = get_string_lower(customer, 'spouse_last_name')

                no_of_family_members = get_value(customer, 'no_of_family_members')
                household_income_monthly = get_value(customer, 'household_income_monthly')

                salutation_val = validate_dict(salutation, LosDictionary.salutation)
                gender_val = validate_dict(gender, LosDictionary.gender)
                marital_status_val = validate_dict(marital_status, LosDictionary.marital_status)
                relation_with_applicant_val = validate_dict(relation_with_applicant, LosDictionary.relation_with_applicant)

                #
                no_of_family_members = validate_numeric(no_of_family_members)
                household_income_monthly = validate_numeric(household_income_monthly)

                if first_name is None:
                    response_obj = get_response("first_name")
                    return response_obj

                if salutation_val == dict():
                    response_obj = get_response("salutation")
                    return response_obj

                if gender_val == dict():
                    response_obj = get_response("gender")
                    return response_obj

                if marital_status_val == dict():
                    response_obj = get_response("marital_status")
                    return response_obj

                if relation_with_applicant_val == dict():
                    response_obj = get_response("relation_with_applicant")
                    return response_obj

                date_of_birth = validate_date(date_of_birth)
                if date_of_birth == "ERROR_DATE":
                    response_obj = get_response("check_dob")
                    return response_obj

                if no_of_family_members == int():
                    response_obj = get_response("check_numeric_family")
                    return response_obj

                if household_income_monthly == int():
                    response_obj = get_response("check_numeric_income")
                    return response_obj

                current_time = django.utils.timezone.now()
                logger.debug("current_time india: %s", current_time)
                customer = Customer(
                    salutation=salutation_val,
                    first_name=first_name,
                    middle_name=middle_name,
                    last_name=last_name,
                    gender=gender_val,
                    date_of_birth=date_of_birth,
                    relation_with_applicant=relation_with_applicant_val,
                    marital_status=marital_status_val,
                    father_first_name=father_first_name,
                    father_middle_name=father_middle_name,
                    father_last_name=father_last_name,
                    mother_first_name=mother_first_name,
                    mother_middle_name=mother_middle_name,
                    mother_last_name=mother_last_name,
                    spouse_first_name=spouse_first_name,
                    spouse_middle_name=spouse_middle_name,
                    spouse_last_name=spouse_last_name,
                    no_of_family_members=no_of_family_members,
                    household_income_monthly=household_income_monthly,
                    status=1,
                    creation_date=current_time, creation_by="System")
                customer.save()
                logger.info("inserted in customer table")

                if customer.id:
                    customer_audit = Customerauditlog(
                        salutation=salutation_val,
                        first_name=first_name,
                        middle_name=middle_name,
                        last_name=last_name,
                        gender=gender_val,
                        date_of_birth=date_of_birth,
                        relation_with_applicant=relation_with_applicant_val,
                        marital_status=marital_status_val,
                        father_first_name=father_first_name,
                        father_middle_name=father_middle_name,
                        father_last_name=father_last_name,
                        mother_first_name=mother_first_name,
                        mother_middle_name=mother_middle_name,
                        mother_last_name=mother_last_name,
                        spouse_first_name=spouse_first_name,
                        spouse_middle_name=spouse_middle_name,
                        spouse_last_name=spouse_last_name,
                        no_of_family_members=no_of_family_members,
                        household_income_monthly=household_income_monthly,
                        status=1,
                        creation_date=current_time,
                        creation_by="System",
                        customer_id=customer.id)
                    customer_audit.save()
                    logger.info("inserted in customer audit table")
                else:
                    response_obj = get_response("customer_id")
                    return response_obj
                response_obj = get_response("success")
            else:
                response_obj = get_response("generic_error_1")
        else:
            response_obj = get_response("generic_error_1")

    except Exception as e:
        logger.exception("Exception: ")
        response_obj = get_response("generic_error_2")

    logger.info("response: %s", response_obj)
    return response_obj


def update_customer(req_data):
    response_obj = None
    try:
        logger.info("request: %s", req_data)

        if req_data:
            customer = None
            if hasattr(req_data, 'customer'):
                customer = req_data.customer

                variables = EmptyClass()
                variables.customer_id = get_value(customer, 'customer_id')
                variables.salutation = get_string_lower(customer, 'salutation')
                variables.first_name = get_string_lower(customer, 'first_name')
                variables.middle_name = get_string_lower(customer, 'middle_name')
                variables.last_name = get_string_lower(customer, 'last_name')

                variables.gender = get_string_lower(customer, 'gender')
                variables.date_of_birth = get_string_lower(customer, 'date_of_birth')
                variables.relation_with_applicant = get_string_lower(customer, 'relation_with_applicant')
                variables.marital_status = get_string_lower(customer, 'marital_status')

                variables.father_first_name = get_string_lower(customer, 'father_first_name')
                variables.father_middle_name = get_string_lower(customer, 'father_middle_name')
                variables.father_last_name = get_string_lower(customer, 'father_last_name')

                variables.mother_first_name = get_string_lower(customer, 'mother_first_name')
                variables.mother_middle_name = get_string_lower(customer, 'mother_middle_name')
                variables.mother_last_name = get_string_lower(customer, 'mother_last_name')

                variables.spouse_first_name = get_string_lower(customer, 'spouse_first_name')
                variables.spouse_middle_name = get_string_lower(customer, 'spouse_middle_name')
                variables.spouse_last_name = get_string_lower(customer, 'spouse_last_name')

                variables.no_of_family_members = get_value(customer, 'no_of_family_members')
                variables.household_income_monthly = get_value(customer, 'household_income_monthly')

                # validations
                variables.salutation = validate_dict(variables.salutation, LosDictionary.salutation)
                variables.gender = validate_dict(variables.gender, LosDictionary.gender)
                variables.marital_status = validate_dict(variables.marital_status, LosDictionary.marital_status)
                variables.relation_with_applicant = validate_dict(variables.relation_with_applicant, LosDictionary.relation_with_applicant)

                variables.no_of_family_members = validate_numeric(variables.no_of_family_members)
                variables.household_income_monthly = validate_numeric(variables.household_income_monthly)

                customer_db = None
                if variables.customer_id:
                    try:
                        customer_db = Customer.objects.get(pk=variables.customer_id)
                    except ObjectDoesNotExist as e:
                        response_obj = get_response("id_not_exist")
                        return response_obj
                else:
                    response_obj = get_response("customer_id")
                    return response_obj

                logger.debug("customer_db: %s", customer_db)

                if variables.first_name is None:
                    response_obj = get_response("first_name")
                    return response_obj

                if variables.salutation == dict():
                    response_obj = get_response("salutation")
                    return response_obj

                if variables.gender == dict():
                    response_obj = get_response("gender")
                    return response_obj

                if variables.marital_status == dict():
                    response_obj = get_response("marital_status")
                    return response_obj

                if variables.relation_with_applicant == dict():
                    response_obj = get_response("relation_with_applicant")
                    return response_obj

                variables.date_of_birth = validate_date(variables.date_of_birth)
                if variables.date_of_birth == "ERROR_DATE":
                    response_obj = get_response("check_dob")
                    return response_obj

                if variables.no_of_family_members == int():
                    response_obj = get_response("check_numeric_family")
                    return response_obj

                if variables.household_income_monthly == int():
                    response_obj = get_response("check_numeric_income")
                    return response_obj

                set_db_attr_request(customer_db, customer, variables)
                logger.debug("customer_db: %s", customer_db)

                current_time = django.utils.timezone.now()
                logger.debug("current_time india: %s", current_time)
                customer_db.updation_date = current_time
                customer_db.updation_by = "System"
                customer_db.save()
                logger.info("updated id: %s", variables.customer_id)

                customer_audit = Customerauditlog()
                customer_audit.__dict__ = customer_db.__dict__.copy()
                customer_audit.id = None
                customer_audit.customer = customer_db
                customer_audit.save()

                logger.info("inserted in customer audit table")
                response_obj = get_response("success")
            else:
                response_obj = get_response("generic_error_1")
        else:
            response_obj = get_response("generic_error_1")
    except Exception as e:
        logger.exception("Exception: ")
        response_obj = get_response("generic_error_2")
        logger.info("response: %s", response_obj)
    return response_obj
