#!/usr/bin/python3
"""
Script that prints the State object matching the name given as argument,
from the database hbtn_0e_6_usa, safe from SQL injection.

Usage:
    ./10-model_state_my_get.py <mysql_username> <mysql_password> <db_name> <state_name>
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Read command line arguments
    username = sys.argv[1]     # MySQL username
    password = sys.argv[2]     # MySQL password
    db_name = sys.argv[3]      # Database name
    state_name = sys.argv[4]   # State name to search for (user input)

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

    # Filter by name. Using .filter(State.name == state_name) with
    # SQLAlchemy's ORM automatically parameterizes the value, keeping
    # this safe from SQL injection.
    state = session.query(State).filter(State.name == state_name).first()

    if state is None:
        print("Not found")
    else:
        print(state.id)

    # Clean up
    session.close()
