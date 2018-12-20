from library_api.models.literature import Literature
from library_api.models.order_book import OrderBook
from library_api.models.reader import Reader
from library_api.models.tasks import Tasks
from library_api.models.material_literature_ import MaterialLiterature
from library_api.models.ticket import Ticket
from library_api.models.electronic_literature_ import ElectronicLiterature
import random
from datetime import date

import unittest
from deepdiff import DeepDiff


class TestLiterature(unittest.TestCase):
    def test_init(self, id=1, author="Popov", title="Romeo", publishing_house= "Astra", year_publishing = 1997):
        literature = Literature(id, author, title, publishing_house, year_publishing)
        self.assertEqual(id, literature.id)
        self.assertEqual(author, literature.author)
        self.assertEqual(title, literature.title)
        return literature

    def test_autor(self, author="Popov"):
        literature = Literature()
        literature.author = author
        author_return = literature.author
        self.assertEqual(author, author_return)

    def test_id(self, id=1):
        literature = Literature()
        literature.id = id
        id_return = literature.id
        self.assertEqual(id, id_return)

    def test_title(self, title="Romeo"):
        literature = Literature()
        literature.title = title
        title_return = literature.title
        self.assertEqual(title, title_return)


class TestMaterialLiterature(unittest.TestCase):
    def test_init(self, number_literature=1):
        material_literature = MaterialLiterature(number_literature)
        self.assertEqual(number_literature, material_literature.number_literature)
        print(material_literature)

    def test_number_literature(self, number_literature=2):
        material_literature = MaterialLiterature(number_literature)
        material_literature.number_literature = number_literature
        self.assertEqual(2, material_literature.number_literature)


class TestElectronicLiterature(unittest.TestCase):
    def test_init(self, electronic_address='google.com'):
        electronic_literature = ElectronicLiterature(electronic_address)
        self.assertEqual(electronic_address, electronic_literature.electronic_address)
        print(electronic_literature)

    def test_electronic_literature(self, electronic_address='google.com'):
        electronic_literature = ElectronicLiterature()
        electronic_literature.electronic_address = electronic_address
        self.assertEqual(electronic_address, electronic_literature.electronic_address)

    def test_invalid_electronic_literature(self, electronic_address='googlecom'):
        electronic_literature = ElectronicLiterature()
        with self.assertRaises(ValueError):
            electronic_literature.electronic_address = electronic_address


class TestOrdrerBooks(unittest.TestCase):
    def test_init(self, status=1, fact_return_date=date(2017, 4, 13), id=1):
        id_literature = TestLiterature.test_init(self, id)
        order_book = OrderBook(status, fact_return_date, id_literature)
        self.assertEqual(status, order_book.status)
        self.assertEqual(fact_return_date, order_book.fact_return_date)
        self.assertEqual(id_literature, order_book.id_literature)
        print(order_book)
        return order_book

    def test_status(self, status=0):
        order_book = OrderBook()
        order_book.status = status
        status_return = order_book.status
        self.assertEqual(status, status_return)

    def test_date(self, fact_return_date=date(2017, 4, 13)):
        order_book = OrderBook()
        order_book.fact_return_date = fact_return_date
        date_return = order_book.fact_return_date
        self.assertEqual(fact_return_date, date_return)

    def test_id(self):
        literature = TestLiterature.test_init(self)
        order_book = OrderBook()
        order_book.id = literature.id
        data_return = order_book.id
        self.assertEqual(literature.id, data_return)


class TestTasks(unittest.TestCase):
    def test_init(self, id=1, registration_date=date(2018, 1, 1), expect_return_date=date(2018, 1, 1)):
        order_book_list = TestOrdrerBooks.test_init(self)
        tasks = Tasks(id, [order_book_list], registration_date, expect_return_date)
        self.assertEqual(tasks.id, id)
        self.assertEqual(tasks.order_book_list, [order_book_list])
        self.assertEqual(tasks.registration_date, registration_date)
        self.assertEqual(tasks.expect_return_date, expect_return_date)
        print(tasks)
        return tasks

    def test_id(self, id=123):
        tasks = Tasks()
        tasks.id = id
        id_return = tasks.id
        self.assertEqual(id, id_return)

    def test_literature(self):
        tasks = Tasks()
        literature = ["qwe"]
        tasks.literature = literature
        literature_return = tasks.literature
        self.assertEqual(literature, literature_return)

    def test_add_and_find_order_book_list_id(self, status=0, fact_return_date=date(2018, 2, 1), id=3):
        order_book = TestOrdrerBooks().test_init(status, fact_return_date, id)
        tasks = Tasks()
        tasks.order_book_list = []
        tasks.addOrderBooksList(order_book)
        result_find = tasks.findOrderBooksListId(value=order_book.id_literature.id)
        result = DeepDiff(order_book, result_find)
        self.assertEqual({}, result)
        return tasks

    def invalid_add_and_find_tasks_id(self, id=2, registration_date=date(2018, 2, 2), expect_return_date=date(2018, 2, 2)):
        tasks = Tasks()
        tasks.order_book_list = []
        order_books = []
        status = 0
        year = 2035
        month = 3
        numb = 3
        id = 22
        for i in range(6):
            fact_return_date = date(year, month, numb)
            order_book = TestOrdrerBooks().test_init(status, fact_return_date, id)
            order_books.append(order_book)
            year = year + 1
            month = month + 1
            numb = numb + 1
            id = id + 1
        with self.assertRaises(ValueError):
            tasks = TestTasks().test_init(id, registration_date, expect_return_date)
            tasks.addOrderBooksList(order_books)

    def test_add_and_find_order_book_list_status(self, status=1, fact_return_date=date(2018, 3, 3)):
        tasks = self.test_add_and_find_order_book_list_id(status, fact_return_date)
        order_book = TestOrdrerBooks().test_init(status, date(2025,3,3))
        tasks.addOrderBooksList(order_book)
        result_find = tasks.findOrderBooksListStatus(value=status)
        self.assertEqual(2, len(result_find))
        return tasks

    def test_delete_order_books_list(self, status=0, fact_return_date=date(2018, 4, 3), id=2):
        tasks = self.test_add_and_find_order_book_list_id(status, fact_return_date, id)
        tasks.deleteOrderBooksList(id)
        find_task = tasks.findOrderBooksListId(id)
        self.assertEqual(None, find_task)


class TestReader(unittest.TestCase):
    def test_init(self, id=1, first_name="Argasova", last_name="Veronika"):
        reader = Reader(id, first_name, last_name)
        self.assertEqual(reader.id, id)
        print(reader)
        return reader

    def test_first_name(self, first_name="Argasova"):
        reader = Reader()
        reader.first_name = first_name
        first_name_return = reader.first_name
        self.assertEqual(first_name, first_name_return)

    def test_last_name(self, last_name="Veronika"):
        reader = Reader()
        reader.last_name = last_name
        last_name_return = reader.last_name
        self.assertEqual(last_name, last_name_return)

    def test_email(self, email="ver@yandex.ru"):
        reader = Reader()
        reader.email = email
        email_return = reader.email
        self.assertEqual(email, email_return)

    def test_invalid_email(self, email="veryandex.ru"):
        reader = Reader()
        with self.assertRaises(ValueError):
            reader.email = email

    def test_id(self, id=123):
        reader = Reader()
        reader.id = id
        id_return = reader.id
        self.assertEqual(id, id_return)


class TestTicket(unittest.TestCase):
    def test_init(self, unique_key=1, date_of_registration=date(2016, 3, 3)):
        tasks = TestTasks().test_init()
        reader = TestReader().test_init()
        ticket = Ticket(unique_key, date_of_registration, [tasks], reader)
        print(ticket)
        return ticket

    def test_unique_test(self, unique_key=2):
        ticket = Ticket()
        ticket.unique_key = unique_key
        self.assertEqual(unique_key, ticket.unique_key)

    def test_data_of_registration(self, date_of_registration=date(2016, 5, 5)):
        ticket = Ticket()
        ticket.date_of_registration = date_of_registration
        self.assertEqual(date_of_registration, ticket.date_of_registration)

    def test_reader(self):
        ticket = Ticket()
        reader = TestReader().test_init()
        ticket.reader = reader
        self.assertEqual(ticket.reader, reader)

    def test_add_and_find_tasks_id(self, id=2, registration_date=date(2018, 2, 2), expect_return_date=date(2018, 2, 2)):
        tasks = TestTasks().test_init(id, registration_date, expect_return_date)
        ticket = Ticket()
        ticket.tasks = []
        ticket.addTasks(tasks)
        result_find = ticket.findTasksId(value=id)
        result = DeepDiff(tasks, result_find)
        self.assertEqual({}, result)
        return ticket

    def test_add_and_find_tasks_date(self, registration_date=date(2018, 3, 3), expect_return_date=date(2018, 3, 3)):
        ticket = self.test_add_and_find_tasks_id(3, registration_date, expect_return_date)
        tasks_added = TestTasks().test_init(4, registration_date, expect_return_date)
        ticket.addTasks(tasks_added)
        result_find = ticket.findTasksDate(value=registration_date)
        self.assertEqual(2, len(result_find))
        return ticket

    def test_delete_task(self):
        ticket = self.test_add_and_find_tasks_id(5, date(2018, 4, 4), date(2018, 4, 4))
        ticket.deleteTasks(5)
        find_task = ticket.findTasksId(5)
        self.assertEqual(None, find_task)


if __name__ == '__main__':
    import unittest
    unittest.main()

