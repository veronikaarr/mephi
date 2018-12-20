from library_api.controllers.reader_controller import get_reader
from library_api.controllers.reader_controller import post_reader
from library_api.controllers.ticket_controller import get_ticket
from datetime import date
from library_api.controllers.order_book_controller import add_order_book
from library_api.controllers.tasks_controller import add_task
from library_api.controllers.utils.user_interface import user_get_bpmn2
from library_api.controllers.utils.sql_request import sql_insert_task_bpmn2


def bmpn2():
    ticket_id, literature_id = user_get_bpmn2()
    return_ticket = get_ticket(ticket_id)
    if return_ticket is None:
        raise ValueError("Ticket not exist")
    z = 0
    w = 1
    debt = []
    for k in return_ticket.tasks:
        for i in k.order_book_list:
            if k.expect_return_date < date.today() and i.status == 0:
                'проверять статус'
                debt.append(i.id_literature)
                z = z + 1
                if z >= 3:
                    return k.order_book_list, 404
    for k in return_ticket.tasks:
        for i in k.order_book_list:
            w = w + 1
            if w >= 15:
                return 405, w
    for k in return_ticket.tasks:
        j = 0
        for i in k.order_book_list:
            j = j + 1
            if j >= 5:
                return 406, w
    order_book = add_order_book(literature_id=literature_id)
    task = add_task(order_book_es=order_book)
    return_ticket.tasks = []
    return_ticket.tasks.append(task)
    sql_insert_task_bpmn2(return_ticket)
    return task, 201