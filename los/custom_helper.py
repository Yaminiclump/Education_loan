from los.los_dict import LosDictionary
import datetime
from datetime import datetime,date
import logging
from los.status_code import get_response

logger = logging.getLogger("django")

def get_value(obj, param):
    return getattr(obj,param) if hasattr(obj,param) else None


def clean_string(str_val):
    if str_val:
        sanitized = str_val.strip()
        sanitized = sanitized if sanitized else None
        return sanitized
    else:
        return None


def lower_case_string(str_val):
    if str_val:
        sanitized = str_val.lower()
        return sanitized
    else:
        return None


def get_string_lower(obj, param):
    str_val = get_value(obj, param)
    trim_string = clean_string(str_val)
    lower_string = lower_case_string(trim_string)
    return lower_string


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
            dict_val = None
            return dict_val
    else:
        return None


