from flask import Flask, render_template, request, redirect, url_for, session, flash, g
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from flask import jsonify
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = 'S\xe7\xf0H\xa8Q\x96\x9b\xa1I\xc7\xf3\xcc\xa2g\xa7\x0e\xb3\xfa=n\xf9\x87\xc5\x0e'

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('data5.db')
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE ,
            password TEXT,
            thername TEXT UNIQUE,
            thpasswd TEXT
        )       
        ''')
        db.commit()

        cursor.execute('''
            CREATE TABLE  IF NOT EXISTS student_score (
                student_id INTEGER PRIMARY KEY,
                student_name TEXT NOT NULL,
                student_class TEXT ,
                gender TEXT NOT NULL,
                student_phone INTEGER NOT NULL,
                student_bedroom INTEGER NOT NULL,
                student_age INTEGER NOT NULL,
                student_address TEXT NOT NULL
            )
        ''')
        db.commit()

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS score (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            chinese INTEGER,
            math INTEGER,
            english INTEGER,
            major INTEGER
        )       
        ''')
        db.commit()

if __name__ == '__main__':
    init_db()
    app.run(debug=True)