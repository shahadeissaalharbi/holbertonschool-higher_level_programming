#!/usr/bin/python3
"""
Script that adds the State "Louisiana" to the database hbtn_0e_6_usa,
using SQLAlchemy, and prints the new state's id.

Usage:
    ./11-model_state_insert.py <mysql_username> <mysql_password> <db_name>
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

    # Create a new State instance and add it to the session
    new_state = State(name="Louisiana")
    session.add(new_state)

    # Commit the transaction so the new row is written to the database
    session.commit()

    # After commit, SQLAlchemy populates new_state.id with the
    # auto-generated primary key value from the database
    print(new_state.id)

    # Clean up
    session.close()
