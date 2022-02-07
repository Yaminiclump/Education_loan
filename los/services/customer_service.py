import logging
from io import BytesIO
import django.utils.timezone
from django.core.files.storage import default_storage
from los.status_code import get_response
from los.models.customer_auditlog_model import Customerauditlog
from los.models.customer_model import Customer
from los.los_dict import LosDictionary
from django.http import JsonResponse,HttpResponse
import datetime
from datetime import datetime,date
from los.custom_helper import get_string_lower, clean_string, get_value, validate_numeric,validate_dict,fetch_value
logger = logging.getLogger("django")


def create_service(req_data):
    response_obj = None

    try:
        logger.info("request: %s", req_data)

        if req_data:
            customer = None
            if hasattr(req_data, 'customer'):
                customer = req_data.customer

                salutation = get_value(customer, 'salutation')
                first_name = get_string_lower(customer, 'first_name')
                middle_name = get_string_lower(customer, 'middle_name')
                logger.debug("middle_name: %s", middle_name)
                last_name = get_string_lower(customer, 'last_name')
                gender = get_value(customer, 'gender')
                date_of_birth = get_string_lower(customer, 'date_of_birth')

                relation_with_applicant= get_value(customer, 'relation_with_applicant')
                logger.debug("relation_with_applicant_data: %s", relation_with_applicant)
                marital_status = get_value(customer, 'marital_status')
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
                marital_status = validate_dict(marital_status, LosDictionary.marital_status)

                relation_with_applicant = validate_numeric(relation_with_applicant)
                no_of_family_members = validate_numeric(no_of_family_members)
                household_income_monthly = validate_numeric(household_income_monthly)

                if not hasattr(customer, 'first_name'):
                    response_obj = get_response("check_parameter")
                    return response_obj

                if first_name is None:
                    response_obj = get_response("first_name")
                    return response_obj

                if salutation_val == dict():
                    response_obj = get_response("salutation")
                    return response_obj

                if gender_val == dict():
                    response_obj = get_response("gender")
                    return response_obj

                if marital_status == dict():
                    response_obj = get_response("marital_status")
                    return response_obj

                if date_of_birth:
                    try:
                        formated_dob = datetime.strptime(date_of_birth, "%Y-%m-%d").date()
                        date_of_birth = formated_dob
                    except ValueError:
                        response_obj = get_response("check_dob")
                        return response_obj

                if relation_with_applicant == int():
                    response_obj = get_response("check_numeric")
                    return response_obj

                if no_of_family_members == int():
                    response_obj = get_response("check_numeric")
                    return response_obj

                if household_income_monthly == int():
                    response_obj = get_response("check_numeric")
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
                    relation_with_applicant=relation_with_applicant,
                    marital_status=marital_status,
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
                        relation_with_applicant=relation_with_applicant,
                        marital_status=marital_status,
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

                customer_id = get_value(customer, 'customer_id')
                salutation = get_value(customer, 'salutation')
                first_name = get_string_lower(customer, 'first_name')
                middle_name = get_string_lower(customer, 'middle_name')
                last_name = get_string_lower(customer, 'last_name')

                gender = get_value(customer, 'gender')
                date_of_birth = get_value(customer, 'date_of_birth')
                relation_with_applicant = get_value(customer, 'relation_with_applicant')

                marital_status = get_value(customer, 'marital_status')
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

                # validations
                salutation_val = validate_dict(salutation, LosDictionary.salutation)
                gender_val = validate_dict(gender, LosDictionary.gender)
                marital_status = validate_dict(marital_status, LosDictionary.marital_status)
                relation_with_applicant = validate_numeric(relation_with_applicant)
                no_of_family_members = validate_numeric(no_of_family_members)
                household_income_monthly = validate_numeric(household_income_monthly)

                if customer_id:
                    if type(customer_id) == int:
                        if not Customer.objects.filter(id=customer_id).exists():
                            response_obj = get_response("id_notexist")
                            return response_obj
                        customer_id = customer_id
                    else:
                        response_obj = get_response("check_numeric")
                        return response_obj
                else:
                    response_obj = get_response("customer_id")
                    return response_obj

                get_customer = Customer.objects.filter(id=customer_id)
                logger.info("get_customer: %s", get_customer)

                if first_name is None:
                    response_obj = get_response("first_name")
                    return response_obj

                if middle_name is None:
                    middle_name = fetch_value(customer, get_customer, 'middle_name')

                if last_name is None:
                    last_name = fetch_value(customer, get_customer, 'last_name')

                if father_first_name is None:
                    father_first_name = fetch_value(customer, get_customer, 'father_first_name')

                if father_middle_name is None:
                    father_middle_name = fetch_value(customer, get_customer, 'father_middle_name')

                if father_last_name is None:
                    father_last_name = fetch_value(customer, get_customer, 'father_last_name')

                if mother_first_name is None:
                    mother_first_name = fetch_value(customer, get_customer, 'mother_first_name')

                if mother_middle_name is None:
                    mother_middle_name = fetch_value(customer, get_customer, 'mother_middle_name')

                if mother_last_name is None:
                    mother_last_name = fetch_value(customer, get_customer, 'mother_last_name')

                if spouse_first_name is None:
                    spouse_first_name = fetch_value(customer, get_customer, 'spouse_first_name')

                if spouse_last_name is None:
                    spouse_last_name = fetch_value(customer, get_customer, 'spouse_last_name')

                if spouse_middle_name is None:
                    spouse_middle_name = fetch_value(customer, get_customer, 'spouse_middle_name')

                if salutation_val == dict():
                    response_obj = get_response("salutation")
                    return response_obj
                if salutation is None:
                    salutation_val = fetch_value(customer, get_customer, 'salutation')

                if gender_val == dict():
                    response_obj = get_response("gender")
                    return response_obj
                if gender is None:
                    gender_val = fetch_value(customer, get_customer, 'gender')

                if marital_status == dict():
                    response_obj = get_response("marital_status")
                    return response_obj
                if marital_status is None:
                    marital_status = fetch_value(customer, get_customer, 'marital_status')

                if date_of_birth:
                    try:
                        formated_dob = datetime.strptime(date_of_birth, "%Y-%m-%d").date()
                        date_of_birth = formated_dob
                    except ValueError:
                        response_obj = get_response("check_dob")
                        return response_obj
                else:
                    date_of_birth = fetch_value(customer, get_customer, 'date_of_birth')

                if relation_with_applicant == int():
                    response_obj = get_response("check_numeric")
                    return response_obj
                if relation_with_applicant is None:
                    relation_with_applicant = fetch_value(customer, get_customer, 'relation_with_applicant')

                if no_of_family_members == int():
                    response_obj = get_response("check_numeric")
                    return response_obj
                if no_of_family_members is None:
                    no_of_family_members = fetch_value(customer, get_customer, 'no_of_family_members')

                if household_income_monthly == int():
                    response_obj = get_response("check_numeric")
                    return response_obj
                if household_income_monthly is None:
                    household_income_monthly = fetch_value(customer, get_customer, 'household_income_monthly')

                current_time = django.utils.timezone.now()
                logger.debug("current_time india: %s", current_time)
                customer_update = Customer.objects.filter(id=customer_id).update(
                    salutation=salutation_val,
                    first_name=first_name,
                    middle_name=middle_name,
                    last_name=last_name,
                    gender=gender_val,
                    date_of_birth=date_of_birth,
                    relation_with_applicant=relation_with_applicant,
                    marital_status=marital_status,
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
                    updation_date=current_time,
                    updation_by="System")
                logger.info("updated id: %s", customer_id)

                customer_audit = Customerauditlog(
                    salutation=salutation_val,
                    first_name=first_name,
                    middle_name=middle_name,
                    last_name=last_name,
                    gender=gender_val,
                    date_of_birth=date_of_birth,
                    relation_with_applicant=relation_with_applicant,
                    marital_status=marital_status,
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
                    customer_id=customer_id
                )
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


