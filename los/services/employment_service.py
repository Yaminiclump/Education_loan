import logging
import django.utils.timezone
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from los.constants import STATUS_ACTIVE, CREATION_BY, UPDATION_BY
from los.custom_helper import get_string_lower, get_value, validate_dict, validate_email, validate_mob, \
    set_db_attr_request, InvalidInputException
from los.los_dict import LosDictionary
from los.models.employment_model import Employment, EmploymentLog
from los.models.customer_model import Customer
from los.models.empty_class import EmptyClass
from los.status_code import get_response, get_response_1, get_response_resp_var, Statuses


def employment_create(req_data):
    return "abcc"
