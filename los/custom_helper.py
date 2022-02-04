from los.los_dict import LosDictionary
import datetime
from datetime import datetime,date
import logging
from los.status_code import get_response

logger = logging.getLogger("django")

def validate_string(str_val):
    if str_val:
        sanitized = str_val.strip().lower()
        sanitized = sanitized if sanitized else None
        return sanitized
    else:
        return None

def set_value(obj,param):
    return getattr(obj,param) if hasattr(obj,param) else None

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

def validate_dict(dict_val,obj):
    if dict_val:
        if obj == 'salutation':
            if dict_val in LosDictionary.salutation.keys():
                dict_val = LosDictionary.salutation[dict_val]
                return dict_val
            else:
                dict_val = dict()
                return dict_val
        if obj == 'gender':
            if dict_val in LosDictionary.gender.keys():
                dict_val = LosDictionary.gender[dict_val]
                return dict_val
            else:
                dict_val = dict()
                return dict_val
        if obj == 'marital_status':
            if dict_val in LosDictionary.marital_status.keys():
                dict_val = LosDictionary.marital_status[dict_val]
                return dict_val
            else:
                dict_val = dict()
                return dict_val
    else:
        return None





