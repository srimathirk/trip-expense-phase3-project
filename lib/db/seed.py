#!/usr/bin/env python3
# seed.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Trip, Expense
import random
from datetime import datetime, timedelta

def seed_users(session):
    names = ['John', 'Evan', 'Emma', 'Ana', 'Heshan', 'Shaan', 'Zoe', 'zia', 'rani', 'nila']
    phones = ['5454545454', '3453453452', '1234123443', '6565657890']
    
    users = []
    for _ in range(10):
        user = User(
            user_name=random.choice(names),
            Email=f'{random.choice(names)}@gmail.com',
            Phone=random.choice(phones),
            created_at=datetime.now()
        )
        #session.add(user)
        users.append(user)
    #session.commit()
    return users
def add_new_user(session, user_name, email, phone):
    new_user = User(user_name=user_name, Email=email, Phone=phone, created_at=datetime.now())
    session.add(new_user)
    session.commit()
    return new_user

def add_new_trip(session, start_place, destination_place, gas_cost, mileage, user):
    new_trip = Trip(start_place=start_place, destination_place=destination_place, gas_cost=gas_cost, mileage=mileage, user=user)
    session.add(new_trip)
    session.commit()
    return new_trip

def add_new_expense(session, cost_category, amount, trip):
    new_expense = Expense(cost_category=cost_category, amount=amount, trip=trip)
    session.add(new_expense)
    session.commit()

def seed_trips(session, users):
    start_places = ["NewYork", "NewJersey", "California", "niagarafalls US"]
    destination_places = ["Chicago", "Ohio", "Connecticut","Nevada"]
    
    trips = []
    for _ in range(10):
        user = random.choice(users)
        trip = add_new_trip(
            session,
            start_place=random.choice(start_places),
            destination_place=random.choice(destination_places),
            gas_cost=random.randint(10, 555),
            mileage=random.randint(20, 65),
            user=user
        )
        trips.append(trip)
    return trips

def seed_expenses(session, trips):
    categories = ["Food", "Accommodation", "Entrance", "Parking"]
    
    for _ in range(10):
        trip = random.choice(trips)
        add_new_expense(
            session,
            cost_category=random.choice(categories),
            amount=random.randint(100, 500),
            trip=trip
        )

if __name__ == '__main__':
    engine = create_engine('sqlite:///trip_records.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    
    session.query(User).delete()
    session.query(Trip).delete()
    session.query(Expense).delete()
    print("Starting seed populates")
    session.commit()

    users = seed_users(session)
    trips = seed_trips(session, users)
    seed_expenses(session, trips)

    session.close()
