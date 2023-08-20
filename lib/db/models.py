from sqlalchemy import create_engine, MetaData, func, ForeignKey
from sqlalchemy import Column, Integer, String, Float, Table, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy

#to maintain consistency of database schema
convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)
#database connection
engine = create_engine('sqlite:///trip_records.db')
# Base = declarative_base()
#User class (table)
class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer(), primary_key=True)
    user_name = Column(String())
    Email = Column(String(),unique = True)
    Phone = Column(String())
    created_at = Column(DateTime(),server_default=func.now())
    trips = relationship("Trip", back_populates='user')
    def __repr__(self):
        return f"User {self.user_id}: " \
            + f"Name {self.user_name}, " \
            + f"Email {self.Email}" \
            + f"Phone {self.Phone}" \
            + f"at {self.created_at}"
#Trip class (table)
class Trip(Base):
    __tablename__='trips'
    trip_id = Column(Integer(),primary_key=True)
    start_place = Column(String())
    destination_place = Column(String())
    gas_cost = Column(Float())
    miles_per_gallon = Column(Float())
    user_id = Column(Integer(), ForeignKey('users.user_id'))
    expenses = relationship('Expense', back_populates='trip')
    user = relationship('User', back_populates='trips')
    def __repr__(self):
        return f"Trip {self.trip_id}: " \
            + f"From {self.start_place}, " \
            + f"To {self.destination_place}" \
            + f"Gas_price {self.gas_cost}" \
            + f"MPG {self.miles_per_gallon}"
