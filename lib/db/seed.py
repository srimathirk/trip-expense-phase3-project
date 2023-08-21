#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Trip, Expense
import random
from datetime import datetime, timedelta
# from geopy.geocoders import Nominatim
# from geopy.distance import geodesic
if __name__ == '__main__':
    #databasse connection
    engine = create_engine('sqlite:///trip_records.db')
    #Base.metadata.create_all(engine)

    #create a session
    Session = sessionmaker(bind=engine)
    session = Session()

#deleting old populated seed to make sure everything works fine
    session.query(User).delete()
    session.query(Trip).delete()
    session.query(Expense).delete()
    print("starting seed populates")
    session.commit()

#insert seed data
    names = ['John', 'Evan', 'Emma', 'Ana', 'Heshan', 'Shaan', 'Zoe', 'zia', 'rani', 'nila']
    #email = f'{names}@gmail.com'
    phones = ['5454545454', '3453453452', '1234123443', '6565657890','4545454545','7896541230','2589631478','7539512369','7412589654','7589547858']
    emails = ['abc@gmail.com', 'wer@gmail.com','re123@gmail.com', 'frg23@hotmail.com','wdv@gmail.com','frg@gmail.com','tre@ymail.com','srusti@gmail.com','thenn@gmail.com','ddd@gmail.com']
    #start_date = datetime(2023, 1, 1)
    #end_date = datetime(2023, 12, 31)
    #time_difference = end_date - start_date
    #random_time = random.random()* time_difference.total_seconds()
            
    users = []
    for name, phone, email in zip(names,phones,emails):
        #zip iterates through names,phones,emails lists simultaneously
        #random_seconds = random.randint(0,int(time_difference.total_seconds()))
        #random_time = start_date + timedelta(seconds=random_seconds)
        user = User(
            user_name=name,
            Email=email,
            Phone=phone,
            created_at= datetime.now()
        )
        # add and commit individually to get IDs back
        session.add(user)
        users.append(user)
    session.commit()

    start_places = ["New York City, NY", "Los Angeles, CA", "Chicago, IL", "New York City,NY","Los Angeles", "Philadelphia, PA" ,"Phoenix, AZ", "San Diego, CA", "Austin, TX","San Francisco, CA"  ]
    destination_places = ["Jersey City, NJ", "San Jose, CA", "Columbus, OH","San Antonio, TX", "San Diego, CA", "San Jose, CA","Jacksonville, FL", "San Francisco, CA","Fort Worth, TX", "Los Angeles, CA"]    
    
    trips=[]
    for start_place, destination_place in zip(start_places,destination_places):
        trip= Trip(
            start_place=start_place,
            destination_place=destination_place,
            gas_cost=random.randint(3,5),
            miles_per_gallon=random.randint(20,65),
            user=random.choice(users)            
        )
        session.add(trip)
        session.commit()
        trips.append(trip)
    categories = ["Food","Accomodation","entrance","parking"]
    expenses=[]
    for i in range (10):
        expense= Expense(
            cost_category=random.choice(categories),
            amount=random.randint(100,500),
            trip=random.choice(trips)
        )
        session.add(expense)
        session.commit()
        expenses.append(expense)
    
    #test
    user_id_to_filter = 1
    user_trips = session.query(Trip).filter_by(user_id=user_id_to_filter).all()
    for trip in user_trips:
        print(trip)
        # Access associated expenses and print their details
        for expense in trip.expenses:
            print("Expense:", expense)


    
    #import ipdb; ipdb.set_trace()
    session.close()

# delete_records()
# create_user()
# create_trips()
# create_expenses()