#!/usr/bin/python3
"""Flask application that displays product data from JSON, CSV, or SQL."""
import csv
import json
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json_products():
    """Read and return the list of products from products.json."""
    with open('products.json', encoding='utf-8') as json_file:
        return json.load(json_file)


def read_csv_products():
    """Read and return the list of products from products.csv."""
    products = []
    with open('products.csv', encoding='utf-8', newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price']),
            })
    return products


def read_sql_products():
    """Read and return the list of products from products.db."""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, category, price FROM Products')
    rows = cursor.fetchall()
    conn.close()
    return [
        {'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]}
        for row in rows
    ]


@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('contact.html')


@app.route('/items')
def items():
    """Render the items page with data read from items.json."""
    with open('items.json', encoding='utf-8') as items_file:
        data = json.load(items_file)
    return render_template('items.html', items=data.get('items', []))


@app.route('/products')
def products():
    """Render the products page, filtered by source and optional id."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        all_products = read_json_products()
    elif source == 'csv':
        all_products = read_csv_products()
    elif source == 'sql':
        try:
            all_products = read_sql_products()
        except sqlite3.Error:
            return render_template(
                'product_display.html', error='Database error'
            )
    else:
        return render_template('product_display.html', error='Wrong source')

    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template(
                'product_display.html', error='Product not found'
            )

        matched = [p for p in all_products if p['id'] == product_id]
        if not matched:
            return render_template(
                'product_display.html', error='Product not found'
            )
        return render_template('product_display.html', products=matched)

    return render_template('product_display.html', products=all_products)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
