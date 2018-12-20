from library_api.controllers.utils.inits import readers_register, tickets_database, storages
from faker import Faker
faker = Faker()


def sql_select_reader(lastName, phone_number):
    for i in readers_register:
        if i.last_name == lastName and i.phone_number == phone_number:
            return i


def sql_insert_database(ticket):
    # try:
    # except:
    ticket.unique_key = faker.random_digit()
    return ticket


def sql_select_ticket(ticket_id):
    for i, z in enumerate(tickets_database):
        print(i)
        if i.unique_key == ticket_id:
            return i


def sql_insert_task_bpmn2(return_ticket):
    ...


def sql_select_literature_bpmn2(literature_id):
    for i in storages:
        if literature_id in storages:
            if 'number_literature' in i.to_dict():
                if i.number_literate == 0:
                    return 0
            else:
                return None
        else:
            return i


def sql_get_ticket_bpmn3(return_ticket, literature_id):
    for i in storages:
        if literature_id in storages:
            return literature_id


def sql_get_bpmn3_all():
    return tickets_database[1]