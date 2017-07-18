from flask_mysqldb import MySQL
from flask import Flask, render_template, request
import csv
import random
import time
import sys
import redis
import pickle
import hashlib


app = Flask(__name__)
app.config['MYSQL_USER'] = 'username'
app.config['MYSQL_PASSWORD'] = 'pass'
app.config['MYSQL_DB'] = 'tempdatabase'
app.config['MYSQL_HOST'] = ''
mysql = MySQL(app)

def get_user_credentials():
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM boatData;')
    data = cursor.fetchall()
    return data



@app.route('/', methods=['GET','POST'])
def show_index():
    # readCSVFile()
    # row_list = get_user_credentials()
    if request.method == 'GET':
        return render_template('index.html', time_to_execute = 0 )
    elif request.method == 'POST':
            return render_template('index.html', time_to_execute = 0)

# Added how to create a table
def create_table():
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute( '''CREATE TABLE boatData(
        pclass varchar(30),
        survived varchar(30),
        home_dest varchar(30),
        name varchar(30),
        sex varchar(30),
        age varchar(30),
        ticket varchar(30),
        fare varchar(30),
        cabin varchar(30)
    );''')
    conn.commit



if __name__ == '__main__':
    app.run()
