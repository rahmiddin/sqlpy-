import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship
import pandas as pd

Base = declarative_base()


class Publisher(Base):

    __tablename__ = 'Publisher'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.Text, unique=True)

    def __str__(self):
        return f'{self.id}:{self.name}'


class Book(Base):

    __tablename__ = 'Book'

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.Text, unique=True)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey("Publisher.id"), nullable=False)

    publisher = relationship(Publisher, backref='Book')



class Stock(Base):

    __tablename__ = 'Stock'

    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey("Book.id"), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey("Shop.id"), nullable=False)
    count = sq.Column(sq.Integer)

    book = relationship(Book, backref='Stock')


class Shop(Base):
    __tablename__ = 'Shop'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.Text, unique=True)

    stock = relationship(Stock, backref='Shop')


class Sale(Base):

    __tablename__ = 'Sale'

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Integer)
    date_sale = sq.Column(sq.DATE)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey("Stock.id"), nullable=False)
    count = sq.Column(sq.Integer)

    stock = relationship(Stock, backref='Sale')


def create_tables(engine):
    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


