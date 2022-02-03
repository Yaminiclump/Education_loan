import logging
from io import BytesIO

import django.utils.timezone
import django.utils.timezone
from django.core.files.storage import default_storage

from los.error_code import errors
from los.models.customer_auditlog_model import Customerauditlog
from los.models.customer_model import Customer
from los.los_dict import LosDictionary
from django.http import JsonResponse,HttpResponse
import datetime
from datetime import datetime,date
from los.los_func import string_check
logger = logging.getLogger("django")


def create_service(req_data):
    response_obj = None

    try:
        logger.info("request: %s", req_data)

        if req_data:
            customer = None
            if hasattr(req_data, 'customer'):
                customer = req_data.customer

                salutation = customer.salutation if hasattr(customer, 'salutation') else None
                first_name = customer.first_name if hasattr(customer, 'first_name') else None
                middle_name = customer.middle_name if hasattr(customer, 'middle_name') else ""

                last_name = customer.last_name if hasattr(customer, 'last_name') else ""
                gender = customer.gender if hasattr(customer, 'gender') else ""
                date_of_birth = customer.date_of_birth if hasattr(customer, 'date_of_birth') else None

                relation_with_applicant = customer.relation_with_applicant if hasattr(customer, 'relation_with_applicant') else None
                marital_status = customer.marital_status if hasattr(customer, 'marital_status') else None
                father_first_name = customer.father_first_name if hasattr(customer, 'father_first_name') else None

                father_middle_name = customer.father_middle_name if hasattr(customer, 'father_middle_name') else None
                father_last_name = customer.father_last_name if hasattr(customer, 'father_last_name') else None
                mother_first_name = customer.mother_first_name if hasattr(customer, 'mother_first_name') else None

                mother_middle_name = customer.mother_middle_name if hasattr(customer, 'mother_middle_name') else None
                mother_last_name = customer.mother_last_name if hasattr(customer, 'mother_last_name') else None
                spouse_first_name = customer.spouse_first_name if hasattr(customer, 'spouse_first_name') else None

                spouse_middle_name = customer.spouse_middle_name if hasattr(customer, 'spouse_middle_name') else None
                spouse_last_name = customer.spouse_last_name if hasattr(customer, 'spouse_last_name') else None
                no_of_family_members = customer.no_of_family_members if hasattr(customer, 'no_of_family_members') else None
                household_income_monthly = customer.household_income_monthly if hasattr(customer, 'household_income_monthly') else None

                if first_name:
                    first_name = string_check(first_name)
                    if len(first_name.strip()) == 0:
                        response_obj = {"error_code": errors.string_blank["error_code"], "message": errors.string_blank["message"]}
                        return response_obj
                    else:
                        first_name = first_name
                else:
                    response_obj = {"error_code": errors.first_name["error_code"], "message": errors.first_name["message"]}
                    return response_obj

                if middle_name:
                    middle_name = string_check(middle_name)
                    if len(middle_name.strip()) == 0:
                        response_obj = {"error_code": errors.string_blank["error_code"], "message": errors.string_blank["message"]}
                        return response_obj
                    else:
                        middle_name = middle_name
                else:
                    middle_name = None

                if last_name:
                    last_name = string_check(last_name)
                    if len(last_name.strip()) == 0:
                        response_obj = {"error_code": errors.string_blank["error_code"], "message": errors.string_blank["message"]}
                        return response_obj
                    else:
                        last_name = last_name
                else:
                    last_name = None

                if father_first_name:
                    father_first_name = string_check(father_first_name)
                    if len(father_first_name.strip()) == 0:
                        response_obj = {"error_code": errors.string_blank["error_code"], "message": errors.string_blank["message"]}
                        return response_obj
                    else:
                        father_first_name = father_first_name
                else:
                    father_first_name = None

                if father_middle_name:
                    father_middle_name = string_check(father_middle_name)
                    if len(father_middle_name.strip()) == 0:
                        response_obj = {"error_code": errors.string_blank["error_code"], "message": errors.string_blank["message"]}
                        return response_obj
                    else:
                        father_middle_name = father_middle_name
                else:
                    father_middle_name = None

                if father_last_name:
                    father_last_name = string_check(father_last_name)
                    if len(father_last_name.strip()) == 0:
                        response_obj = {"error_code": errors.string_blank["error_code"], "message": errors.string_blank["message"]}
                        return response_obj
                    else:
                        father_last_name = father_last_name
                else:
                    father_last_name = None

                if mother_first_name:
                    mother_first_name = string_check(mother_first_name)
                    if len(mother_first_name.strip()) == 0:
                        response_obj = {"error_code": errors.string_blank["error_code"], "message": errors.string_blank["message"]}
                        return response_obj
                    else:
                        mother_first_name = mother_first_name
                else:
                    mother_first_name = None

                if mother_last_name:
                    mother_last_name = string_check(mother_last_name)
                    if len(mother_last_name.strip()) == 0:
                        response_obj = {"error_code": errors.string_blank["error_code"], "message": errors.string_blank["message"]}
                        return response_obj
                    else:
                        mother_last_name = mother_last_name
                else:
                    mother_last_name = None

                if mother_middle_name:
                    mother_middle_name = string_check(mother_middle_name)
                    if len(mother_middle_name.strip()) == 0:
                        response_obj = {"error_code": errors.string_blank["error_code"], "message": errors.string_blank["message"]}
                        return response_obj
                    else:
                        mother_middle_name = mother_middle_name
                else:
                    mother_middle_name = None

                if spouse_first_name:
                    spouse_first_name = string_check(spouse_first_name)
                    if len(spouse_first_name.strip()) == 0:
                        response_obj = {"error_code": errors.string_blank["error_code"], "message": errors.string_blank["message"]}
                        return response_obj
                    else:
                        spouse_first_name = spouse_first_name
                else:
                    spouse_first_name = None

                if spouse_last_name:
                    spouse_last_name = string_check(spouse_last_name)
                    if len(spouse_last_name.strip()) == 0:
                        response_obj = {"error_code": errors.string_blank["error_code"], "message": errors.string_blank["message"]}
                        return response_obj
                    else:
                        spouse_last_name = spouse_last_name
                else:
                    spouse_last_name = None

                if spouse_middle_name:
                    spouse_middle_name = string_check(spouse_middle_name)
                    if len(spouse_middle_name.strip()) == 0:
                        response_obj = {"error_code": errors.string_blank["error_code"], "message": errors.string_blank["message"]}
                        return response_obj
                    else:
                        spouse_middle_name = spouse_middle_name
                else:
                    spouse_middle_name = None

                if salutation:
                    if salutation not in LosDictionary.salutation.keys():
                        response_obj = {"error_code": errors.salutation["error_code"],"message": errors.salutation["message"]}
                        return response_obj
                    salutation_val = LosDictionary.salutation[salutation]
                else:
                    salutation_val = None

                if gender:
                    if gender not in LosDictionary.gender.keys():
                        response_obj = {"error_code": errors.gender["error_code"],"message": errors.gender["message"]}
                        return response_obj
                    gender_val = LosDictionary.gender[gender]

                else:
                    gender_val = None

                if marital_status:
                    if marital_status not in LosDictionary.marital_status.keys():
                        response_obj = {"error_code": errors.marital_status["error_code"],"message": errors.marital_status["message"]}
                        return response_obj
                    marital_status = LosDictionary.marital_status[marital_status]
                else:
                    marital_status = None

                if date_of_birth:
                    try:
                        formated_dob = datetime.strptime(date_of_birth, "%Y-%m-%d").date()
                        date_of_birth = formated_dob
                    except ValueError:
                        response_obj = {"error_code": errors.check_dob["error_code"], "message": errors.check_dob["message"]}
                        return response_obj
                else:
                    date_of_birth = None

                if relation_with_applicant:
                    if type(relation_with_applicant) == int:
                        relation_with_applicant = relation_with_applicant
                    else:
                        response_obj = {"error_code": errors.check_numeric["error_code"], "message": errors.check_numeric["message"]}
                        return response_obj
                else:
                    relation_with_applicant = None

                if no_of_family_members:
                    if type(no_of_family_members) == int:
                        no_of_family_members = no_of_family_members
                    else:
                        response_obj = {"error_code": errors.check_numeric["error_code"], "message": errors.check_numeric["message"]}
                        return response_obj
                else:
                    no_of_family_members = None

                if household_income_monthly:
                    if type(household_income_monthly) == int:
                        household_income_monthly = household_income_monthly
                    else:
                        response_obj = {"error_code": errors.check_numeric["error_code"], "message": errors.check_numeric["message"]}
                        return response_obj
                else:
                    household_income_monthly = None

                current_time = django.utils.timezone.now()
                logger.debug("current_time india: %s", current_time)
                customer = Customer(salutation=salutation_val,
                                    first_name=first_name,
                                    middle_name =middle_name,
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
                                    no_of_family_members = no_of_family_members,
                                    household_income_monthly=household_income_monthly,
                                    status=1,
                                    creation_date=current_time, creation_by="System")
                customer.save()
                logger.info("inserted in customer table")

                if customer.id:

                    customer_audit = Customerauditlog(salutation=salutation_val,
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
                                                      customer_id=customer.id
                                                      )
                    customer_audit.save()
                    logger.info("inserted in customer audit table")
                else:
                    response_obj = {"error_code": errors.customer_id["error_code"],"message": errors.customer_id["message"]}
                    return response_obj
                response_obj = {"error_code": errors.success["error_code"], "message": errors.success["message"],
                                "data": {
                                    "customer_id": customer.id}
                                }
            else:
                response_obj = {"error_code": errors.generic_error_1["error_code"], "message": errors.generic_error_1["message"]}
        else:
            response_obj = {"error_code": errors.generic_error_1["error_code"], "message": errors.generic_error_1["message"]}

    except Exception as e:
        logger.exception("Exception: ")
        response_obj = {"error_code": errors.generic_error_2["error_code"], "message": errors.generic_error_2["message"]}

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

            if customer and hasattr(customer, 'customer_id') and hasattr(customer, 'first_name'):
                customer_id = customer.customer_id
                salutation = customer.salutation if hasattr(customer,'salutation') else ""
                first_name = customer.first_name
                middle_name = customer.middle_name if hasattr(customer, 'middle_name') else ""

                last_name = customer.last_name if hasattr(customer, 'last_name') else ""
                gender = customer.gender if hasattr(customer, 'gender') else ""
                date_of_birth = customer.date_of_birth if hasattr(customer, 'date_of_birth') else ""

                relation_with_applicant = customer.relation_with_applicant if hasattr(customer, 'relation_with_applicant') else ""
                marital_status = customer.marital_status if hasattr(customer, 'marital_status') else ""
                father_first_name = customer.father_first_name if hasattr(customer, 'father_first_name') else ""

                father_middle_name = customer.father_middle_name if hasattr(customer, 'father_middle_name') else ""
                father_last_name = customer.father_last_name if hasattr(customer, 'father_last_name') else ""
                mother_first_name = customer.mother_first_name if hasattr(customer, 'mother_first_name') else ""

                mother_middle_name = customer.mother_middle_name if hasattr(customer, 'mother_middle_name') else ""
                mother_last_name = customer.mother_last_name if hasattr(customer, 'mother_last_name') else ""
                spouse_first_name = customer.spouse_first_name if hasattr(customer, 'spouse_first_name') else ""

                spouse_middle_name = customer.spouse_middle_name if hasattr(customer, 'spouse_middle_name') else ""
                spouse_last_name = customer.spouse_last_name if hasattr(customer, 'spouse_last_name') else ""
                no_of_family_members = customer.no_of_family_members if hasattr(customer, 'no_of_family_members') else ""
                household_income_monthly = customer.household_income_monthly if hasattr(customer, 'household_income_monthly') else ""
                # database select query
                # sal_db_val
                if len(first_name.strip()) == 0:
                    response_obj = {"error_code": errors.name["error_code"], "message": errors.name["message"]}
                    return response_obj

                if salutation:
                    # salutation_val = check_keys()
                    if salutation not in LosDictionary.salutation.keys():
                        response_obj = {"error_code": errors.salutation["error_code"], "message": errors.salutation["message"]}
                        return response_obj
                    salutation_val = LosDictionary.salutation[salutation]
                else:
                    salutation_val = None
                    # salutation_val = sal_db_val if sal_db_val else None

                if gender:
                    if gender not in LosDictionary.gender.keys():
                        response_obj = {"error_code": errors.gender["error_code"], "message": errors.gender["message"]}
                        return response_obj
                    gender_val = LosDictionary.gender[gender]

                else:
                    gender_val = None

                if marital_status:
                    if marital_status not in LosDictionary.marital_status.keys():
                        response_obj = {"error_code": errors.marital_status["error_code"], "message": errors.marital_status["message"]}
                        return response_obj
                    marital_status = LosDictionary.marital_status[marital_status]
                else:
                    marital_status = None

                if date_of_birth:
                    try:
                        formated_dob = datetime.strptime(date_of_birth, "%Y-%m-%d").date()
                        date_of_birth = formated_dob
                    except ValueError:
                        response_obj = {"error_code": errors.check_dob["error_code"], "message": errors.check_dob["message"]}
                        return response_obj
                else:
                    date_of_birth = None

                if relation_with_applicant:
                    if type(relation_with_applicant) == int:
                        relation_with_applicant = relation_with_applicant
                    else:
                        response_obj = {"error_code": errors.check_numeric["error_code"], "message": errors.check_numeric["message"]}
                        return response_obj
                else:
                    relation_with_applicant = None

                if no_of_family_members:
                    if type(no_of_family_members) == int:
                        no_of_family_members = no_of_family_members
                    else:
                        response_obj = {"error_code": errors.check_numeric["error_code"], "message": errors.check_numeric["message"]}
                        return response_obj
                else:
                    no_of_family_members = None

                if household_income_monthly:
                    if type(household_income_monthly) == int:
                        household_income_monthly = household_income_monthly
                    else:
                        response_obj = {"error_code": errors.check_numeric["error_code"], "message": errors.check_numeric["message"]}
                        return response_obj
                else:
                    household_income_monthly = None

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

                if customer_id:
                    customer_audit = Customerauditlog(salutation=salutation_val,
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
                else:
                    response_obj = {"error_code": errors.customer_id["error_code"],"message": errors.customer_id["message"]
                                    }
                    return response_obj
                response_obj = {"error_code": errors.success["error_code"],"message": errors.success["message"],
                                "data": {
                                    "customer_id": customer_id,
                                    "customer_audit_id": customer_audit.id}
                                }
            else:
                response_obj = {"error_code": errors.generic_error_1["error_code"],"message": errors.generic_error_1["message"]}

        else:
            response_obj = {"error_code": errors.generic_error_1["error_code"],"message": errors.generic_error_1["message"]}

    except Exception as e:
        logger.exception("Exception: ")
        response_obj = {"error_code": errors.generic_error_2["error_code"],"message": errors.generic_error_2["message"]}
        logger.info("response: %s", response_obj)
    return response_obj
