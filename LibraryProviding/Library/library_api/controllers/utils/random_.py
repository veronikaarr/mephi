from library_api.models.reader import Reader
from library_api.models.order_book import OrderBook
from library_api.models.literature import Literature
from library_api.models.tasks import Tasks
from library_api.models.ticket import Ticket
from faker import Faker
import datetime
faker = Faker()

phone_number = '8(932)441-22-98', '8(971)565-56-89', '8(964)408-40-71'


def random_reader():
    return Reader(email= faker.email(), first_name = faker.first_name(), id = faker.random_digit(),
                             last_name= faker.last_name(), pasport_id= faker.postcode(), pasport_series = faker.postcode(),
                             patronymic = faker.first_name(), phone_number=faker.random_element(phone_number))


def random_material_literature():
    literatures = []
    for _ in range(5):
        literature = Literature(id=faker.random_digit(), title=faker.name(), author=faker.first_name(),
                            publishing_house=faker.company(), year_publishing=faker.year())
        literature.number_literature = faker.random_digit()
        literatures.append(literature)
    return literatures


def random_electronic_literature():
    literatures = []
    for _ in range(5):
        literature = Literature(id=faker.random_digit(), title=faker.name(), author=faker.first_name(),
                            publishing_house=faker.company(), year_publishing=faker.year())
        literature.electronic_address=faker.email()
        literatures.append(literature)
    return literatures

def random_electronic_literature_():
    literatures = []
    for _ in range(10):
        literature = Literature(id=faker.random_digit(), title=faker.name(), author=faker.first_name(),
                            publishing_house=faker.company(), year_publishing=faker.year())
        literature.electronic_address=faker.email()
        literatures.append(literature)
    return literatures


def random_material_literature_():
    literatures = []
    for _ in range(5):
        literature = Literature(id=faker.random_digit(), title=faker.name(), author=faker.first_name(),
                            publishing_house=faker.company(), year_publishing=faker.year())
        literature.number_literature = faker.random_digit()
        literatures.append(literature)
    return literatures


def random_order_book(literature = random_material_literature(), status=0):
    order_books = []
    for z, i in enumerate(literature):
        order_book = OrderBook(id_literature=i)
        order_book.status = status
        order_books.append(order_book)
    return order_books


def random_order_book_(literature = random_material_literature_(), status=0):
    order_books = []
    for z, i in enumerate(literature):
        order_book = OrderBook(id_literature=i)
        order_book.status = status
        order_books.append(order_book)
    return order_books


def random_tasks(order_book_es=random_order_book(), days=10):
    tasks = Tasks()
    tasks.order_book_list = order_book_es
    tasks.registration_date = datetime.date.today() - datetime.timedelta(days=days)
    return tasks


def random_storage_of_book(mat=random_material_literature(), el=random_electronic_literature()):
    storage = []
    storage.extend(mat)
    storage.extend(el)
    return storage


def random_ticket(reader=random_reader(), tasks=random_tasks()):
    ticket = Ticket(date_of_registration=datetime.date.today() - datetime.timedelta(days=60), reader=reader)
    ticket.unique_key = reader.id  # TODO: всё сделать uuid и в swagger, перенести в post, подумать над uuid
    ticket.tasks = [tasks]
    return ticket


def random_ticket_(reader=random_reader(), tasks=random_tasks()):
    ticket = Ticket(date_of_registration=datetime.date.today() - datetime.timedelta(days=60), reader=reader)
    ticket.unique_key = reader.id  # TODO: всё сделать uuid и в swagger, перенести в post, подумать над uuid
    ticket.tasks = []
    for i in range(10):
        ticket.tasks.append(random_tasks())
    return ticket


reader_to_register = []
for _ in range(20):
    reader = random_reader()
    reader_to_register.append(reader)

tickets_in_database = [i for i in range(100)]
storages = []
'читатели с книгами на руках'
literature = random_material_literature()
storage = random_storage_of_book(mat=literature)
storages.extend(storage)
tasks = random_tasks(order_book_es=random_order_book(literature=literature))
ticket = random_ticket(reader=reader_to_register[0], tasks=tasks)
tickets_in_database[0] = ticket

'сданы книги, непросрочены'
literature = random_electronic_literature()
storage = random_storage_of_book(mat=literature)
storages.extend(storage)
tasks = random_tasks(order_book_es=random_order_book(literature=literature, status=1), days=12)
ticket = random_ticket(reader=reader_to_register[1], tasks=tasks)
tickets_in_database[1] = ticket

'книги просрочены'
literature = random_electronic_literature()
storage = random_storage_of_book(mat=literature)
storages.extend(storage)
tasks = random_tasks(order_book_es=random_order_book(literature=literature), days=22)
ticket = random_ticket(reader=reader_to_register[2], tasks=tasks)
tickets_in_database[2] = ticket

"""без книг"""
ticket = random_ticket(reader=reader_to_register[3])
tickets_in_database[3] = ticket


literature = random_electronic_literature()
storage = random_storage_of_book(mat=literature)
storages.extend(storage)
tasks = random_tasks(order_book_es=random_order_book_(literature=literature), days=5)
ticket = random_ticket_(reader=reader_to_register[4], tasks=tasks)
tickets_in_database[4] = ticket

literature = random_electronic_literature_()
storage = random_storage_of_book(mat=literature)
storages.extend(storage)
tasks = random_tasks(order_book_es=random_order_book_(literature=literature), days=5)
ticket = random_ticket(reader=reader_to_register[5], tasks=tasks)
tickets_in_database[5] = ticket