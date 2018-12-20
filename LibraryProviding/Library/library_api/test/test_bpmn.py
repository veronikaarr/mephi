from library_api.controllers.bpmn1 import bmpn1
from library_api.controllers.utils.random_ import random_reader, random_ticket
from library_api.controllers.utils.inits import readers_register, reader_register, ticket_bpmn2, tickets_database
from library_api.controllers.bpmn2 import bmpn2
from library_api.controllers.bpmn3 import bmpn3
import unittest
from faker import Faker
faker = Faker()


class TestReader(unittest.TestCase):
    """
    Our basic test class
    """

    def setUp(self):
        pass

    # def test_valid(self):
    #     del readers_register[0]
    #     print("TEST1: Input:", reader_register.last_name, reader_register.phone_number)
    #     print('\n')
    #     return_code, ticket = bmpn1()
    #     self.assertEqual(return_code, 201)
    #     print("Output:", ticket)
    #     readers_register.append(reader_register)
    #     return ticket
    #
    # def test_exists_reader(self):
    #     print("TEST2: Input:", reader_register.last_name, reader_register.phone_number)
    #     print('\n')
    #     with self.assertRaises(ValueError):
    #         bmpn1()


class TestLiterature(unittest.TestCase):
    def setUp(self):
        ...

    # def test_valid(self):
    #     status, task = bmpn2()
    #     print(status)
    #     self.assertEqual(status, 406)

    def test_nonexisten_ticket(self):
        #ticket_bpmn2 = None
        with self.assertRaises(ValueError):
            bmpn2()
    #
    # def test_debt_library(self):
    #     i, status = bmpn2()
    #     print(i, status)
    #
    # def test_in_all_task_more_then_15(self):
    #     #ticket_bpmn2 = tickets_database[21].unique_key
    #     status, k = bmpn2()
    #     print("Количество книг всего:", k)
    #     self.assertEqual(status, 405)

    # def test_in_one_task_more_then_5(self):
    #     status, k = bmpn2()
    #     print("Вы пытаетесь взять {} книг".format(k))
    #     self.assertEqual(status, 406)


class TestReturnLiterature(unittest.TestCase):
    """
    Our basic test class
    """

    def setUp(self):
        ...

    #def test_valid(self):
    #    status = bmpn3()
    #    print("Книга возвращена")
    #    self.assertEqual(status, 200)

    # def test_book_in_other_reader(self):
    #     with self.assertRaises(ValueError):
    #         bmpn3()

    # def test_book_in__reader(self):
    #     with self.assertRaises(ValueError):
    #         bmpn3()
    #
    # def test_book_is_not_exist(self):
    #     with self.assertRaises(ValueError):
    #         bmpn3()


if __name__ == '__main__':
    import unittest
    unittest.main()
