import logging
import django.utils.timezone
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from los.constants import STATUS_ACTIVE, CREATION_BY, UPDATION_BY
from los.custom_helper import get_string_lower, get_value, validate_dict, validate_email, validate_mob, \
    set_db_attr_request, InvalidInputException,validate_numeric,get_integer_value,get_income_value
from los.los_dict import LosDictionary
from los.models.employment_model import Employment, EmploymentLog
from los.models.customer_model import Customer
from los.models.empty_class import EmptyClass
from los.status_code import get_response, get_response_1, get_response_resp_var, Statuses

logger = logging.getLogger("django")


def employment_create(req_data):
    response_obj = None
    logger.info("service_request: %s", req_data)
    try:
        logger.info("request_service: %s", req_data)
        if req_data:
            customer = None
            if hasattr(req_data, 'customer'):
                customer = req_data.customer
                logger.info("customer_get: %s", req_data.customer)
                customer_id = get_value(customer, 'customer_id')
                employment = get_value(customer, 'employment')
                type = get_string_lower(employment,'type')
                employer_id = get_integer_value(employment, 'employer_id')
                employer_name = get_string_lower(employment, 'employer_name')
                address_id = get_integer_value(employment, 'address_id')
                designation_id = get_integer_value(employment, 'designation_id')
                designation_name = get_string_lower(employment, 'designation_name')
                retirement_age_years = get_integer_value(employment, 'retirement_age_years')
                current_employer_months = get_integer_value(employment, 'current_employer_months')
                gross_income_monthly = get_income_value(employment, 'gross_income_monthly')
                net_income_monthly = get_income_value(employment, 'net_income_monthly')
                other_income_monthly = get_integer_value(employment, 'other_income_monthly')
                work_experience_month = get_integer_value(employment, 'work_experience_month')

                type_val = validate_dict(type, LosDictionary.employment_type)

                # validation
                if customer_id:
                    if not Customer.objects.filter(id=customer_id,status=1).exists():
                        response_obj = get_response(Statuses.customer_id_not_exist)
                        return response_obj
                    customer_id = customer_id
                else:
                    response_obj = get_response(Statuses.customer_id_not_provided)
                    return response_obj

                if employment is None:
                    response_obj = get_response(Statuses.employment_not_provided)
                    return response_obj

                if type_val == dict():
                    response_obj = get_response(Statuses.employment_type)
                    return response_obj

                if employer_id == int():
                    response_obj = get_response(Statuses.employer_id)
                    return response_obj

                if address_id == int():
                    response_obj = get_response(Statuses.address_id)
                    return response_obj

                if designation_id == int():
                    response_obj = get_response(Statuses.designation_id)
                    return response_obj

                if retirement_age_years == int():
                    response_obj = get_response(Statuses.retirement_age_years)
                    return response_obj

                if current_employer_months == int():
                    response_obj = get_response(Statuses.current_employer_months)
                    return response_obj

                if gross_income_monthly is None:
                    response_obj = get_response(Statuses.gross_income_monthly)
                    return response_obj

                if net_income_monthly is None:
                    response_obj = get_response(Statuses.net_income_monthly)
                    return response_obj

                current_time = django.utils.timezone.now()
                logger.debug("current_time india: %s", current_time)
                employment = Employment(
                    type=type_val,
                    employer_id=employer_id,
                    employer_name=employer_name,
                    address_id=address_id,
                    designation_id=designation_id,
                    designation_name=designation_name,
                    retirement_age_years=retirement_age_years,
                    current_employer_months=current_employer_months,
                    gross_income_monthly=gross_income_monthly,
                    net_income_monthly=net_income_monthly,
                    other_income_monthly=other_income_monthly,
                    work_experience_month=work_experience_month,
                    status=STATUS_ACTIVE,
                    creation_date=current_time,
                    creation_by=CREATION_BY,
                    customer_id=customer_id,
                    )
                employment.save()
                employment_log = EmploymentLog()
                employment_log.__dict__ = employment.__dict__.copy()
                employment_log.id = None
                employment_log.employment = employment
                employment_log.save()
                logger.info("finished employment create service")
                response_obj = get_response_1(Statuses.success, {"employment_id": employment.id})
    except Exception as e:
        logger.exception("Exception: ")
        response_obj = get_response(Statuses.generic_error_2)
        logger.info("response: %s", response_obj)
    return response_obj


def employment_update(req_data):
    response_obj = None
    logger.info("service_request: %s", req_data)
    try:
        logger.info("request_service: %s", req_data)
        if req_data:
            customer = None
            if hasattr(req_data, 'customer'):
                customer = req_data.customer
                logger.info("customer_get: %s", req_data.customer)
                customer_id = get_value(customer, 'customer_id')
                employment = get_value(customer, 'employment')
                variables = EmptyClass()
                variables.employment_id = get_value(employment, 'employment_id')
                variables.type = get_string_lower(employment, 'type')
                variables.employer_id = get_integer_value(employment, 'employer_id')
                variables.employer_name = get_string_lower(employment, 'employer_name')
                variables.address_id = get_integer_value(employment, 'address_id')
                variables.designation_id = get_integer_value(employment, 'designation_id')
                variables.designation_name = get_string_lower(employment, 'designation_name')
                variables.retirement_age_years = get_integer_value(employment, 'retirement_age_years')
                variables.current_employer_months = get_integer_value(employment, 'current_employer_months')
                variables.gross_income_monthly = get_income_value(employment, 'gross_income_monthly')
                variables.net_income_monthly = get_income_value(employment, 'net_income_monthly')
                variables.other_income_monthly = get_integer_value(employment, 'other_income_monthly')
                variables.work_experience_month = get_integer_value(employment, 'work_experience_month')

                variables.type = validate_dict(variables.type, LosDictionary.employment_type)

                # validation
                if customer_id:
                    if not Customer.objects.filter(id=customer_id, status=1).exists():
                        response_obj = get_response(Statuses.customer_id_not_exist)
                        return response_obj
                    customer_id = customer_id
                else:
                    response_obj = get_response(Statuses.customer_id_not_provided)
                    return response_obj

                if employment is None:
                    response_obj = get_response(Statuses.employment_not_provided)
                    return response_obj

                employment_db = None
                if variables.employment_id:
                    try:
                        employment_db = Employment.objects.get(pk=variables.employment_id, customer_id=customer_id, status=1)
                    except ObjectDoesNotExist as e:
                        response_obj = get_response(Statuses.employment_id_not_exist)
                        return response_obj
                else:
                    response_obj = get_response(Statuses.employment_id_not_provided)
                    return response_obj

                if variables.type == dict():
                    response_obj = get_response(Statuses.employment_type)
                    return response_obj

                if variables.employer_id == int():
                    response_obj = get_response(Statuses.employer_id)
                    return response_obj

                if variables.address_id == int():
                    response_obj = get_response(Statuses.address_id)
                    return response_obj

                if variables.designation_id == int():
                    response_obj = get_response(Statuses.designation_id)
                    return response_obj

                if variables.retirement_age_years == int():
                    response_obj = get_response(Statuses.retirement_age_years)
                    return response_obj

                if variables.current_employer_months == int():
                    response_obj = get_response(Statuses.current_employer_months)
                    return response_obj

                set_db_attr_request(employment_db,employment,variables)
                current_time = django.utils.timezone.now()
                logger.debug("current_time india: %s", current_time)
                employment_db.updation_date = current_time
                employment_db.updation_by = UPDATION_BY
                employment_db.save()

                employment_log = EmploymentLog()
                employment_log.__dict__ = employment_db.__dict__.copy()
                employment_log.id = None
                employment_log.employment = employment_db
                employment_log.creation_date = current_time
                employment_log.creation_by = CREATION_BY
                employment_log.save()
                logger.info("finished employment update service")
                response_obj = get_response(Statuses.success)
    except Exception as e:
        logger.exception("Exception: ")
        response_obj = get_response(Statuses.generic_error_2)
        logger.info("response: %s", response_obj)
    return response_obj