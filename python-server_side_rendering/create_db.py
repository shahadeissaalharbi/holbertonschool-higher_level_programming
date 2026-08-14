#!/usr/bin/python3
"""Script to create and populate the products.db SQLite database."""
import sqlite3


def create_database():
    """Create the Products table and insert sample data."""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    cursor.execute('DELETE FROM Products')
    cursor.execute('''
        INSERT INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99),
        (3, 'Desk Chair', 'Furniture', 129.99),
        (4, 'Notebook', 'Stationery', 4.99)
    ''')
    conn.commit()
    conn.close()


if __name__ == '__main__':
    create_database()
