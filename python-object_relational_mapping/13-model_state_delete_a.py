#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing the
letter 'a', from the database hbtn_0e_6_usa, using SQLAlchemy.

Usage:
    ./13-model_state_delete_a.py <mysql_username> <mysql_password> <db_name>
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

    # Query all states whose name contains 'a', then delete each one
    states = session.query(State).filter(State.name.like('%a%')).all()

    for state in states:
        session.delete(state)

    # Commit the deletions to the database
    session.commit()

    # Clean up
    session.close()
