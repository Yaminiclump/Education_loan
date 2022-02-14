import json
from string import Template


class Statuses:
    success = {'status_code': 10000, 'message': "Success"}
    # business error
    generic_error_1 = {'status_code': 200010, 'message': "Invalid request details"}
    generic_error_2 = {'status_code': 200011, 'message': "There was some error while processing the request"}
    invalid_request = {'status_code': 200012, 'message': "Invalid request method (only POST method is allowed)"}
    generic_error_3 = {'status_code': 200013, 'message': "There was some error while processing the request"}

    customer_id_not_exist = {'status_code': 200020, 'message': "Please provide a valid Customer ID"}

    first_name = {'status_code': 200110, 'message': "Please enter a valid First Name"}
    salutation = {'status_code': 200111, 'message': "Please select a valid Salutation"}
    marital_status = {'status_code': 200112, 'message': "Please select a valid Marital Status"}
    gender = {'status_code': 200113, 'message': "Please select a valid Gender option"}
    check_dob = {'status_code': 200114, 'message': "Please note that date should be in YYYY-MM-DD format"}
    relation_with_applicant = {'status_code': 200115, 'message': "Please select a valid relationship with the applicant"}
    check_numeric_family = {'status_code': 200116, 'message': "Please enter a valid number of family members"}
    check_numeric_income = {'status_code': 200117, 'message': "Please enter a valid income"}
    test_get = {'status_code': 405}
    test_post = {'status_code': 200}
    check_country_code = {'status_code': 200210, 'message': "country code parameters might be missing in sequence $no"}
    type = {'status_code': 200211, 'message': "type not implemented in sequence $no"}
    email_validate = {'status_code': 200212, 'message': "Invalid Email in sequence $no"}
    mob_validate = {'status_code': 200213, 'message': "Invalid mobile number in sequence $no"}
    id_error = {'status_code': 200214, 'message': "contact id and customer id are not exist."}
    id_param = {'status_code': 200215, 'message': "contact id and customer id might be missing"}
    type_param = {'status_code': 200216, 'message': "type parameters might be missing"}
    value_param = {'status_code': 200217, 'message': "value parameters might be missing"}
    contact_param = {'status_code': 200218, 'message': "contact parameters might be missing"}
    invalid_id = {'status_code': 200219, 'message': "customer id does not exist"}
    country_code = {'status_code': 200220, 'message': "country code does not required in sequence $no"}



def get_response(error_type, data=None):
    status = getattr(Statuses, error_type)
    if data is None:
        return {'status': status['status_code'], 'message': status['message']}
    else:
        return {'status': status['status_code'], 'message': status['message'], 'data': json.dumps(data)}

def prepare_response(status_key, key, value):
    status = getattr(Statuses, status_key)
    message = Template(status["message"])
    message = message.substitute({key: value})
    return {'status': status['status_code'], 'message': message}
