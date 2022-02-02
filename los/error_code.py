class errors():
    success = {'error_code': 10000, 'message': "Success"}

    # business error
    generic_error_1 = {'error_code': 20001, 'message': "Invalid request details"}
    generic_error_2 = {'error_code': 20002, 'message': "There was some error while processing the request"}
    invalid_request = {'error_code': 20003, 'message': "Invalid request method (only POST method is allowed)"}

    generic_error_3 = {'error_code': 20004, 'message': "There was some error while processing the request"}

    salutation = {'error_code': 20005, 'message': "Please provide a valid salutation"}
    marital_status = {'error_code': 20006, 'message': "Please provide a valid marital status"}
    name = {'error_code': 20007, 'message': "Please provide a valid name"}
    father_name = {'error_code': 20008, 'message': "Please provide a valid father name"}
    gender = {'error_code': 20009, 'message': "Please provide a valid gender name"}
    customer_id = {'error_code': 200010, 'message': "Please provide a valid customer id"}
    mother_name = {'error_code': 200011, 'message': "Please provide a valid mother name"}
    spouse_name = {'error_code': 200012, 'message': "Please provide a valid spouse name"}
    test_get = {'error_code': 405}
    test_post = {'error_code': 200}
    check_numeric = {'error_code': 200013, 'message': "It should be Integer Value"}
    check_dob = {'error_code': 200014, 'message': "It should be YYYY-MM-DD format"}
