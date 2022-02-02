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

logger = logging.getLogger("django")


def create_service(req_data):
    response_obj = None

    try:
        logger.info("request: %s", req_data)

        if req_data:
            customer = None
            if hasattr(req_data, 'customer'):
                customer = req_data.customer

            if customer and hasattr(customer, 'first_name'):

                salutation = customer.salutation if hasattr(customer, 'salutation') else ""
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

                if len(first_name.strip()) == 0:
                    response_obj = {"error_code": errors.name["error_code"],"message": errors.name["message"]}
                    return response_obj
                if salutation:
                    salutation_val = LosDictionary.salutation[salutation]
                    if salutation not in LosDictionary.salutation.keys():
                        response_obj = {"error_code": errors.salutation["error_code"],"message": errors.salutation["message"]}
                        return response_obj
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

                if len(first_name.strip()) == 0:
                    response_obj = {"error_code": errors.name["error_code"], "message": errors.name["message"]}
                    return response_obj
                if salutation:
                    salutation_val = LosDictionary.salutation[salutation]
                    if salutation not in LosDictionary.salutation.keys():
                        response_obj = {"error_code": errors.salutation["error_code"], "message": errors.salutation["message"]}
                        return response_obj
                else:
                    salutation_val = None

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
