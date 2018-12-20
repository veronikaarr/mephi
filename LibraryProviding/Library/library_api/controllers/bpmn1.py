from library_api.controllers.reader_controller import get_reader
from library_api.controllers.reader_controller import post_reader
from library_api.controllers.utils.user_interface import user_get_reader_start_data, user_get_reader_data


def bmpn1():
    lastName, phone_number = user_get_reader_start_data()
    return_reader = get_reader(lastName=lastName, phone_number=phone_number)
    if return_reader is not None:
        print("Reader already exist")
        raise ValueError("Reader already exist")
    reader = user_get_reader_data()
    ticket = post_reader(data=reader)
    return 201, ticket