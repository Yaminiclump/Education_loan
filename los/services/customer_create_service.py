import logging
from io import BytesIO

import django.utils.timezone
import django.utils.timezone
from django.core.files.storage import default_storage

from los.error_code import errors
from los.models.customer_auditlog_model import Customerauditlog
from los.models.customer_model import Customer
from los.los_dict import LosDictionary

logger = logging.getLogger("django")


def create_service(req_data):
    response_obj = None

    try:
        logger.info("request: %s", req_data)

        if req_data:

            if req_data and hasattr(req_data, 'salutation') and hasattr(req_data, 'first_name') and \
                    hasattr(req_data, 'middle_name') and hasattr(req_data, 'last_name') and \
                    hasattr(req_data, 'gender') and hasattr(req_data, 'date_of_birth') and \
                    hasattr(req_data, 'relation_with_applicant') and hasattr(req_data, 'marital_status') and \
                    hasattr(req_data, 'father_first_name') and hasattr(req_data, 'father_middle_name') and \
                    hasattr(req_data, 'father_last_name') and hasattr(req_data, 'mother_first_name') and \
                    hasattr(req_data, 'mother_middle_name') and hasattr(req_data, 'mother_last_name') \
                    and hasattr(req_data, 'spouse_first_name') and hasattr(req_data, 'spouse_middle_name') and \
                    hasattr(req_data, 'spouse_last_name') and hasattr(req_data, 'no_of_family_members') \
                    and hasattr(req_data, 'household_income_monthly'):

                salutation = req_data.salutation
                first_name = req_data.first_name
                middle_name = req_data.middle_name

                last_name = req_data.last_name
                gender = req_data.gender
                date_of_birth = req_data.date_of_birth

                relation_with_applicant = req_data.relation_with_applicant
                marital_status = req_data.marital_status
                father_first_name = req_data.father_first_name

                father_middle_name = req_data.father_middle_name
                father_last_name = req_data.father_last_name
                mother_first_name = req_data.mother_first_name

                mother_middle_name = req_data.mother_middle_name
                mother_last_name = req_data.mother_last_name
                spouse_first_name = req_data.spouse_first_name

                spouse_middle_name = req_data.spouse_middle_name
                spouse_last_name = req_data.spouse_last_name
                no_of_family_members = req_data.no_of_family_members
                household_income_monthly = req_data.household_income_monthly

                if salutation not in LosDictionary.salutation.keys():
                    response_obj = {"error_code": errors.salutation["error_code"], "message": errors.salutation["message"]}
                    return response_obj

                if gender not in LosDictionary.gender.keys():
                    response_obj = {"error_code": errors.gender["error_code"], "message": errors.gender["message"]}
                    return response_obj

                if marital_status not in LosDictionary.marital_status.keys():
                    response_obj = {"error_code": errors.marital_status["error_code"], "message": errors.marital_status["message"]}
                    return response_obj

                current_time = django.utils.timezone.now()
                logger.debug("current_time india: %s", current_time)

                customer = Customer(salutation=LosDictionary.salutation[salutation],
                                    first_name=first_name,
                                    middle_name =middle_name,
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
                                    no_of_family_members = no_of_family_members,
                                    household_income_monthly=household_income_monthly,
                                    status=1,
                                    creation_date=current_time, creation_by="System")
                customer.save()

                if customer.id:

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
                                                      customer_id=customer.id
                                                      )
                    customer_audit.save()
                else:
                    response_obj = {"error_code": errors.customer_id["error_code"],
                                    "message": errors.customer_id["message"]
                                    }
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
