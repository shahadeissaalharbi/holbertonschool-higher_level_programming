#!/usr/bin/python3
"""
Script that lists all State objects containing the letter 'a',
from the database hbtn_0e_6_usa, using SQLAlchemy.

Usage:
    ./9-model_state_filter_a.py <mysql_username> <mysql_password> <db_name>
"""
import sys
from model_state import Base, State
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

    # Filter states whose name contains the letter 'a' (case-sensitive),
    # ordered by id ascending.
    states = session.query(State).filter(
        State.name.like('%a%')
    ).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Clean up
    session.close()
