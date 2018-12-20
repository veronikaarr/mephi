from library_api.models.literature import Literature
from library_api.models.order_book import OrderBook
from library_api.models.reader import Reader
from library_api.models.tasks import Tasks
from library_api.models.material_literature_ import MaterialLiterature
from library_api.models.ticket import Ticket
from library_api.models.electronic_literature_ import ElectronicLiterature


literature = [Literature(id=1, author="Popov", title="Romeo", publishing_house= "Astra", year_publishing = '1996'),
              Literature(id=2, author="Popov", title="Romeo", publishing_house= "Romeo", year_publishing = '1997'),
              Literature(id=3, author="Popov", title="Romeo", publishing_house= "Jully", year_publishing = '1998')]

reader = [Reader(email= 'ver@gmail.com', first_name = 'Argasova', id = 1, last_name= 'Veronika', ),
        Reader(email = 'elli@gmail.com', first_name = 'Fedorova', id = 2, last_name ='Elli'),
        Reader(email='roni@gmail.com', first_name='Koelio', id=3, last_name='Roni')]

