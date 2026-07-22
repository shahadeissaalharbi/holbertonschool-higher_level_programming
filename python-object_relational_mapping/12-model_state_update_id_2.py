#!/usr/bin/python3
"""
Script that changes the name of the State with id = 2 to "New Mexico",
in the database hbtn_0e_6_usa, using SQLAlchemy.

Usage:
    ./12-model_state_update_id_2.py <mysql_username> <mysql_password> <db_name>
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

    # Fetch the state with id = 2
    state = session.query(State).filter(State.id == 2).first()

    if state is not None:
        # Update its name in the ORM object
        state.name = "New Mexico"
        # Commit the change so it's persisted to the database
        session.commit()

    # Clean up
    session.close()
