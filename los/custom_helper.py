import datetime
from datetime import datetime
import inspect
import logging
import re
from datetime import datetime

logger = logging.getLogger("django")


class InvalidInputException(Exception):
    """Raised when the input is not valid"""
    pass


def get_attributes(obj):
    attribute_list = []
    for i in inspect.getmembers(obj):

        # to remove private and protected functions
        if not i[0].startswith('_'):

            # To remove other methods that doesnot start with a underscore
            if not inspect.ismethod(i[1]):
                attribute_list.append(i)

    return attribute_list


def set_db_attr_request(db_obj, req_obj, var_obj):
    attribute_list = get_attributes(req_obj)
    logger.debug("attribute_list: %s", attribute_list)
    for attr in attribute_list:
        logger.debug("attributes, name: %s, value: %s", attr[0], attr[1])
        logger.debug("value 1: %s", getattr(var_obj, attr[0], ))
        setattr(db_obj, attr[0], getattr(var_obj, attr[0]))


def get_value(obj, param):
    return getattr(obj, param) if hasattr(obj, param) else None


def clean_string(str_val):
    if str_val:
        if type(str_val) == int:
            sanitized = str_val
        else:
            sanitized = str_val.strip()
        sanitized = sanitized if sanitized else None
        return sanitized
    else:
        return None


def lower_case_string(str_val):
    if str_val:
        if type(str_val) == int:
            sanitized = str_val
        else:
            sanitized = str_val.lower()
        return sanitized
    else:
        return None


def get_string_lower(obj, param):
    str_val = get_value(obj, param)
    trim_string = clean_string(str_val)
    lower_string = lower_case_string(trim_string)
    return lower_string


def set_obj_attr_request(req_obj, var_obj):
    attribute_list = get_attributes(req_obj)
    logger.debug("attribute_list: %s", attribute_list)
    for attr in attribute_list:
        logger.debug("attributes, name: %s, value: %s", attr[0], attr[1])
        attribute_value = get_string_lower(req_obj, attr[0])
        logger.debug("attribute_value_final: %s", attribute_value)
        setattr(var_obj, attr[0], attribute_value)


def get_integer_value(obj, param):
    int_val = get_value(obj, param)
    if int_val:
        if type(int_val) == int:
            int_val = int_val
            return int_val
        else:
            int_val = int()
            return int_val
    else:
        return None


def get_income_value(obj, param):
    rupee_val = get_value(obj, param)
    regex = r'^(?!0+(?:\.0+)?$)[0-9]+(?:\.[0-9]+)?$'
    if rupee_val is not None:
        if (re.match(regex, str(rupee_val))):
            paisa_val = rupee_val * 100
            return paisa_val
        else:
            paisa_val = int()
            return paisa_val
    else:
        return None



def validate_numeric(num_val):
    if num_val:
        if type(num_val) == int:
            num_val = num_val
            return num_val
        else:
            num_val = int()
            return num_val
    else:
        return None


def fetch_value(swagger_obj, db_obj, param):
    return None if hasattr(swagger_obj, param) else getattr(db_obj[0], param)


def validate_dict(dict_val, obj):
    if dict_val:
        if dict_val in obj.keys():
            dict_val = obj[dict_val]
            return dict_val
        else:
            dict_val = dict()
            return dict_val
    else:
        return None


def validate_date(date_val):
    formated_date = None
    if date_val:
        try:
            formated_date = datetime.strptime(date_val, "%Y-%m-%d").date()
        except ValueError:
            formated_date = "ERROR_DATE"
    return formated_date


def validate_date_yyyymm(date_val):
    formated_date = None
    if date_val:
        try:
            formated_date = datetime.strptime(date_val, "%Y-%m").date()
        except ValueError:
            formated_date = "ERROR_DATE"
    return formated_date


def validate_email(email_val):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if email_val:
        email_val = clean_string(email_val)
        if email_val is not None:
            if (re.fullmatch(regex, email_val)):
                return email_val
            else:
                email_val = str()
                return email_val
        else:
            email_val = str()
            return email_val
    else:
        return None


def validate_mob(mob_val):
    regex = r'^[123456789]\d{9}$'
    if mob_val:
        mob_val = clean_string(mob_val)
        if mob_val is not None:
            if (re.fullmatch(regex, mob_val)):
                return mob_val
            else:
                mob_val = str()
                return mob_val
        else:
            mob_val = str()
            return mob_val
    else:
        return None
