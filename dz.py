import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables
import os
from models import Stock, Sale, Publisher, Book, Shop

DSN = 'postgresql://postgres:wwefan123@localhost:5432/postgres'
engine = sqlalchemy.create_engine(DSN)
TEST_DATA_FILE = os.getcwd() + '/tests_data.json'


create_tables(engine)

Session = sessionmaker(bind=engine)

session = Session()


# def add_test_data():
#     with open(TEST_DATA_FILE) as data:
#         info = json.load(data)
#
#     for fix in info:
#         if fix['model'] == "publisher":
#             course = Publisher(name=fix['fields']['name'])
#
#             session.add_all([course])
#             session.commit()
#
#         elif fix['model'] == 'book':
#             course = Book(title=fix['fields']['title'], id_publisher=fix['fields']['publisher'])
#
#             session.add_all([course])
#             session.commit()
#
#         elif fix['model'] == 'shop':
#             course = Shop(name=fix['fields']['name'])
#
#             session.add_all([course])
#             session.commit()
#
#         elif fix['model'] == 'stock':
#             course = Stock(id_shop=fix['fields']['shop'], id_book=fix['fields']['book'], count=fix['fields']['count'])
#
#             session.add_all([course])
#             session.commit()
#
#         elif fix['model'] == 'sale':
#             course = Sale(price=int(fix['fields']['price']), date_sale=fix['fields']['date_sale'], id_stock=fix['fields']['stock'], count=fix['fields']['count'])
#
#             session.add_all([course])
#             session.commit()
# add_test_data()



def Shop_():

    publisher = (input('Введите идендификатор целевого издателя: '))

    if type(publisher) == str:

        id_data = session.query(Publisher.id).filter(
            Publisher.name == publisher
        )
        if id_data:
            for id in id_data:
                publisher_id = id

                q = session.query(Shop.name).filter(
                    Publisher.id == Book.id_publisher,
                    Book.id == Stock.id_book,
                    Stock.id_shop == Shop.id
                ).filter(Book.id_publisher == int(publisher_id[0]))

                for c in q:
                    print(c)
            else:
                print('Такого человека нет')
    else:

        q = session.query(Shop.name).filter(
            Publisher.id == Book.id_publisher,
            Book.id == Stock.id_book,
            Stock.id_shop == Shop.id
        ).filter(Book.id_publisher == publisher)

        for c in q:
            print(c)


Shop_()

session.close()