#!/usr/bin/python3
"""
Script that prints all City objects along with their state name,
from the database hbtn_0e_14_usa, using SQLAlchemy.

Usage:
    ./14-model_city_fetch_by_state.py <mysql_username> <mysql_password> <db_name>
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Read command line arguments
    username = sys.argv[1]   # MySQL username
    password = sys.argv[2]   # MySQL password
    db_name = sys.argv[3]    # Database name

    # Create the engine, connecting to localhost on port 3306
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, db_name
        ),
        pool_pre_ping=True
    )

    # Create a session bound to the engine
    Session = sessionmaker(bind=engine)
    session = Session()

    # Join City and State by querying both, filtering on the FK
    # relationship, ordered by cities.id ascending
    results = session.query(City, State).filter(
        City.state_id == State.id
    ).order_by(City.id).all()

    # Display each row in the required format
    for city, state in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Clean up
    session.close()
