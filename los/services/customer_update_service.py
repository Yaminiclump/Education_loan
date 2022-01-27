import logging
from io import BytesIO

import django.utils.timezone
import django.utils.timezone
from django.core.files.storage import default_storage

from los.error_code import errors
from los.models.customer_auditlog_model import Customerauditlog
from los.models.customer_model import Customer
from los.los_dict import LosDictionary
from django.http import JsonResponse


logger = logging.getLogger("django")
def update_customer(req_data):
    response_obj = None

    try:
        logger.info("request: %s", req_data)

        if req_data:

            customer = None
            if hasattr(req_data, 'customer'):
                customer = req_data.customer

            if customer and hasattr(customer, 'customer_id') and hasattr(customer, 'salutation') \
                    and hasattr(customer, 'first_name') and \
                    hasattr(customer, 'middle_name') and hasattr(customer, 'last_name') and \
                    hasattr(customer, 'gender') and hasattr(customer, 'date_of_birth') and \
                    hasattr(customer, 'relation_with_applicant') and hasattr(customer, 'marital_status') and \
                    hasattr(customer, 'father_first_name') and hasattr(customer, 'father_middle_name') and \
                    hasattr(customer, 'father_last_name') and hasattr(customer, 'mother_first_name') and \
                    hasattr(customer, 'mother_middle_name') and hasattr(customer, 'mother_last_name') \
                    and hasattr(customer, 'spouse_first_name') and hasattr(customer, 'spouse_middle_name') and \
                    hasattr(customer, 'spouse_last_name') and hasattr(customer, 'no_of_family_members') \
                    and hasattr(customer, 'household_income_monthly'):

                customer_id = customer.customer_id
                salutation = customer.salutation
                first_name = customer.first_name
                middle_name = customer.middle_name

                last_name = customer.last_name
                gender = customer.gender
                date_of_birth = customer.date_of_birth

                relation_with_applicant = customer.relation_with_applicant
                marital_status = customer.marital_status
                father_first_name = customer.father_first_name

                father_middle_name = customer.father_middle_name
                father_last_name = customer.father_last_name
                mother_first_name = customer.mother_first_name

                mother_middle_name = customer.mother_middle_name
                mother_last_name = customer.mother_last_name
                spouse_first_name = customer.spouse_first_name

                spouse_middle_name = customer.spouse_middle_name
                spouse_last_name = customer.spouse_last_name
                no_of_family_members = customer.no_of_family_members
                household_income_monthly = customer.household_income_monthly


                if len(first_name.strip()) == 0:
                    response_obj = {"error_code": errors.name["error_code"],
                                    "message": errors.name["message"]
                                    }
                    return response_obj

                if salutation not in LosDictionary.salutation.keys():
                    response_obj = {"error_code": errors.salutation["error_code"],
                                    "message": errors.salutation["message"]
                                    }
                    return response_obj

                if gender not in LosDictionary.gender.keys():
                    response_obj = {"error_code": errors.gender["error_code"],
                                    "message": errors.gender["message"]
                                    }
                    return response_obj

                if marital_status not in LosDictionary.marital_status.keys():
                    response_obj = {"error_code": errors.marital_status["error_code"],
                                    "message": errors.marital_status["message"]
                                    }
                    return response_obj
                current_time = django.utils.timezone.now()
                logger.debug("current_time india: %s", current_time)
                customer_update = Customer.objects.filter(id=customer_id).update(
                    salutation=LosDictionary.salutation[salutation],
                    first_name=first_name,
                    middle_name=middle_name,
                    last_name=last_name,
                    gender=LosDictionary.gender[gender],
                    date_of_birth=date_of_birth,
                    relation_with_applicant=relation_with_applicant,
                    marital_status=LosDictionary.marital_status[marital_status],
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
                    customer_audit = Customerauditlog(salutation=LosDictionary.salutation[salutation],
                                                      first_name=first_name,
                                                      middle_name=middle_name,
                                                      last_name=last_name,
                                                      gender=LosDictionary.gender[gender],
                                                      date_of_birth=date_of_birth,
                                                      relation_with_applicant=relation_with_applicant,
                                                      marital_status=LosDictionary.marital_status[marital_status],
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
                    response_obj = {"error_code": errors.customer_id["error_code"],
                                    "message": errors.customer_id["message"]
                                    }
                    return response_obj

                response_obj = {"error_code": errors.success["error_code"],
                                "message": errors.success["message"],
                                "data": {
                                    "customer_id": customer_id,
                                    "customer_audit_id": customer_audit.id}
                                }
            else:
                response_obj = {"error_code": errors.generic_error_1["error_code"],
                                "message": errors.generic_error_1["message"]}
        else:
            response_obj = {"error_code": errors.generic_error_1["error_code"],
                            "message": errors.generic_error_1["message"]}

    except Exception as e:
        logger.exception("Exception: ")
        response_obj = {"error_code": errors.generic_error_2["error_code"],
                        "message": errors.generic_error_2["message"]}

    logger.info("response: %s", response_obj)
    return response_obj



