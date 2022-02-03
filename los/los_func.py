from los.los_dict import LosDictionary
from los.error_code import errors
import logging
logger = logging.getLogger("django")
def string_check(string):
    string_val = string.replace(" ", "").lower()
    return string_val



