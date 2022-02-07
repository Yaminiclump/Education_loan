def customer_contact(req_data):
    response_obj = None
    try:
        logger.info("request: %s", req_data)
        if req_data:
            customer = None
            if hasattr(req_data, 'customer'):
                customer = req_data.customer
                customer_id = customer.customer_id
                # logger.info("response_data: %s", customer.customer_id)

    except Exception as e:
        logger.exception("Exception: ")
        response_obj = get_response("generic_error_2")
        logger.info("response: %s", response_obj)
    return response_obj