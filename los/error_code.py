class errors():
    success = {'error_code': 10000, 'message': "Success"}

    # business error
    generic_error_1 = {'error_code': 20001, 'message': "Invalid request details"}
    generic_error_2 = {'error_code': 20002, 'message': "There was some error while processing the request"}
    invalid_request = {'error_code': 20003, 'message': "Invalid request method (only POST method is allowed)"}

    generic_error_3 = {'error_code': 20004, 'message': "There was some error while processing the request"}

    salutation = {'error_code': 20005, 'message': "Please provide a valid first name"}
    marital_status = {'error_code': 20006, 'message': "Please provide a valid marital status"}
    gender = {'error_code': 20008, 'message': "Please provide a valid gender name"}
    customer_id = {'error_code': 20009, 'message': "Please provide a valid customer id "}