import json
from string import Template


class Statuses:
    success = {'status_code': 10000, 'message': "Success"}
    # business error
    generic_error_1 = {'status_code': 200010, 'message': "Invalid request details"}
    generic_error_2 = {'status_code': 200011, 'message': "There was some error while processing the request"}
    invalid_request = {'status_code': 200012, 'message': "Invalid request method (only POST method is allowed)"}
    generic_error_3 = {'status_code': 200013, 'message': "There was some error while processing the request"}

    customer_id_not_exist = {'status_code': 200020, 'message': "Please provide a valid Customer Id"}
    customer_id_not_provided = {'status_code': 200021, 'message': "Please provide a valid Customer Id"}
    customer_id_invalid_format = {'status_code': 200022, 'message': "Please provide a valid Customer Id"}

    customer_contact_id_not_exist = {'status_code': 200020, 'message': "Please provide a valid Customer Contact Id"}
    customer_contact_id_not_provided = {'status_code': 200021, 'message': "Please provide a valid Customer Contact Id"}
    customer_contact_id_invalid_format = {'status_code': 200022, 'message': "Please provide a valid Customer Contact Id"}

    employment_id_not_exist = {'status_code': 200023, 'message': "Please enter a valid employment Id"}
    employment_id_not_provided = {'status_code': 200024, 'message': "Please enter a valid employment Id"}

    education_id_not_exist = {'status_code': 200025, 'message': "Please provide a valid Education Id"}
    education_id_not_provided = {'status_code': 200026, 'message': "Please provide a valid Education Id"}


    # customer related...
    first_name = {'status_code': 200110, 'message': "Please enter a valid First Name"}
    salutation = {'status_code': 200111, 'message': "Please select a valid Salutation"}
    marital_status = {'status_code': 200112, 'message': "Please select a valid Marital Status"}
    gender = {'status_code': 200113, 'message': "Please select a valid Gender option"}
    check_dob = {'status_code': 200114, 'message': "Please note that date should be in YYYY-MM-DD format"}
    relation_with_applicant = {'status_code': 200115,
                               'message': "Please select a valid relationship with the applicant"}
    check_numeric_family = {'status_code': 200116, 'message': "Please enter a valid number of family members"}
    check_numeric_income = {'status_code': 200117, 'message': "Please enter a valid income"}
    test_get = {'status_code': 405}
    test_post = {'status_code': 200}

    # customer contact related...
    contact_type = {'status_code': 200211, 'message': "Please enter a valid contact type at sequence no. $sequence"}
    contact_value = {'status_code': 200212,
                     'message': "Please enter a valid value for contact at sequence no. $sequence"}
    contact_value_extra_1 = {'status_code': 200213,
                             'message': "Please enter a valid extra value for contact at sequence no. $sequence"}
    contact_country_code = {'status_code': 200214,
                            'message': "Please enter a valid country code at sequence no. $sequence"}
    email_address = {'status_code': 200215, 'message': "Please enter a valid email address at sequence no. $sequence"}
    mobile_number = {'status_code': 200216, 'message': "Please enter a valid mobile number at sequence no. $sequence"}
    same_contact_id = {'status_code': 200218, 'message': "Multiple customer ids"}
    # TODO: add check for same id

    # customer employment related...
    employment_not_provided = {'status_code': 200311, 'message': "Please provide a valid employment"}
    employment_type = {'status_code': 200312, 'message': "Please enter a valid employment type"}
    employer_id = {'status_code': 200313, 'message': "Please enter a valid employment id"}
    address_id = {'status_code': 200314, 'message': "Please enter a valid address id"}
    designation_id = {'status_code': 200315, 'message': "Please enter a valid designation id"}
    retirement_age_years = {'status_code': 200316, 'message': "Please enter a valid retirement age years"}
    current_employer_months = {'status_code': 200317, 'message': "Please enter a valid current employer months"}
    gross_income_monthly = {'status_code': 200318, 'message': "Please enter a valid gross income"}
    net_income_monthly = {'status_code': 200319, 'message': "Please enter a valid net income"}
    other_income_monthly = {'status_code': 2003110, 'message': "Please enter a valid other income monthly"}
    work_experience_month = {'status_code': 2003111, 'message': "Please enter a valid work experience month"}
    customer_param = {'status_code': 2003112, 'message': "Please enter a valid customer"}

    #customer eduacation related...
    invalid_institute_id = {'status_code': 200411, 'message': "Please enter a valid value for institute id at sequence no. $sequence"}
    invalid_institute_name = {'status_code': 200412, 'message': "Please enter a valid value for institute name at sequence no. $sequence"}
    invalid_course_id = {'status_code': 200413, 'message': "Please enter a valid value for course id at sequence no. $sequence"}
    invalid_course_name = {'status_code': 200414, 'message': "Please enter a valid value for course name at sequence no. $sequence"}
    invalid_stream_id = {'status_code': 200415, 'message': "Please enter a valid value for stream id at sequence no. $sequence"}
    invalid_stream_name = {'status_code': 200416, 'message': "Please enter a valid value for stream name at sequence no. $sequence"}
    invalid_start_month_year = {'status_code': 200417, 'message': "Please enter a valid value for start month & year at sequence no. $sequence"}
    invalid_end_month_year = {'status_code': 200418, 'message': "Please enter a valid value for end month & year at sequence no. $sequence"}
    invalid_marks_type = {'status_code': 200419, 'message': "Please enter a valid value for marks type at sequence no. $sequence"}
    invalid_marks = {'status_code': 2004110, 'message': "Please enter a valid value for marks at sequence no. $sequence"}
    invalid_max_marks = {'status_code': 2004111, 'message': "Please enter a valid value for max marks at sequence no. $sequence"}
    invalid_duration_months = {'status_code': 2004112, 'message': "Please enter a valid value for duration months at sequence no. $sequence"}
    invalid_course_type = {'status_code': 2004113, 'message': "Please enter a valid value for course type at sequence no. $sequence"}

def get_response(status_attribute, data=None):
    if data is None:
        return {'status': status_attribute['status_code'], 'message': status_attribute['message']}
    else:
        return {'status': status_attribute['status_code'], 'message': status_attribute['message'],
                'data': json.dumps(data)}


def get_response_1(status_attribute, data=None):
    if data is None:
        return {'status': status_attribute['status_code'], 'message': status_attribute['message']}
    else:
        return {'status': status_attribute['status_code'], 'message': status_attribute['message'], 'data': data}


def get_response_resp_var(status_attribute, variables):
    message_template_obj = Template(status_attribute["message"])
    message_content = message_template_obj.substitute(variables)
    return {'status': status_attribute['status_code'], 'message': message_content}
