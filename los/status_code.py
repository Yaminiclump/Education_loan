import json
class Statuses():
    success = {'status_code': 10000, 'message': "Success"}
    # business error
    generic_error_1 = {'status_code': 20001, 'message': "Invalid request details"}
    generic_error_2 = {'status_code': 20002, 'message': "There was some error while processing the request"}
    invalid_request = {'status_code': 20003, 'message': "Invalid request method (only POST method is allowed)"}
    generic_error_3 = {'status_code': 20004, 'message': "There was some error while processing the request"}
    salutation = {'status_code': 20005, 'message': "salutation type not implemented"}
    marital_status = {'status_code': 20006, 'message': "marital type not implemented"}
    first_name = {'status_code': 20007, 'message': "first name is missing"}
    father_name = {'status_code': 20008, 'message': "Please provide a valid father name"}
    gender = {'status_code': 20009, 'message': "gender type not implemented"}
    customer_id = {'status_code': 200010, 'message': "customer id parameters might be missing"}
    mother_name = {'status_code': 200011, 'message': "Please provide a valid mother name"}
    spouse_name = {'status_code': 200012, 'message': "Please provide a valid spouse name"}
    test_get = {'status_code': 405}
    test_post = {'status_code': 200}
    check_numeric = {'status_code': 200013, 'message': "It should be numeric Value"}
    check_dob = {'status_code': 200014, 'message': "Date should be YYYY-MM-DD format"}
    string_blank = {'status_code': 200015, 'message': "value is not valid"}
    id_notexist = {'status_code': 200016, 'message': "Customer id does not exist"}
    check_parameter = {'status_code': 200017, 'message': "Some parameters might be missing or are in wrong format"}
    check_country_code = {'status_code': 200018, 'message': "country code parameters might be missing"}
    type = {'status_code': 200019, 'message': "type not implemented"}
    email_validate = {'status_code': 200020, 'message': "Invalid Email"}
    mob_validate = {'status_code': 200021, 'message': "Invalid mobile number."}
    id_error = {'status_code': 200022, 'message': "contact id and customer id are not exist."}
    id_param = {'status_code': 200023, 'message': "contact id and customer id might be missing"}



def get_response(type, data=None):
    status = getattr(Statuses, type)
    if data is None:
        return {'status': status['status_code'], 'message': status['message']}
    else:
        return{'status': status['status_code'], 'message': status['message'], 'data': json.dumps(data)}
