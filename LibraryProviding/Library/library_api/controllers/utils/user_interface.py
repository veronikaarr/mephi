from faker import Faker
from library_api.controllers.utils.inits import tickets_database, readers_register, storages_database, reader_register, \
    literature_bpmn2, ticket_bpmn2, literature_bpmn3
faker = Faker()


def user_get_reader_start_data():
    return reader_register.last_name, reader_register.phone_number


def user_get_reader_data():
    return reader_register


def user_get_bpmn2():
    return ticket_bpmn2, literature_bpmn2


def user_get_bpmn3():
    return ticket_bpmn2, literature_bpmn3