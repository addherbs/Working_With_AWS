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
app.config['MYSQL_USER'] = 'user'
app.config['MYSQL_PASSWORD'] = 'pass'
app.config['MYSQL_DB'] = 'tempdatabase'
app.config['MYSQL_HOST'] = 'host'
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
        print (request.method)
        collect_data = []
        x='mysql'
        operation_keys = request.form.keys()
        selected_operation = [i for i in operation_keys]
        print ('Selected operations are', selected_operation)
        if ('mysql' in selected_operation):
            print ('yahooo!!')
            time_to_execute, collect_data = get_Column()
            # return render_template('index.html', output_files = row_list , time_to_execute = time_to_execute)
            return render_template('index.html', time_to_execute = time_to_execute)
        elif ('redis' in selected_operation):
            time_to_execute, collect_data = connectRedis()
            # return render_template('index.html', output_files = row_list , time_to_execute = time_to_execute)
            return render_template('index.html', time_to_execute = time_to_execute)

@app.route('/home', methods=['GET','POST'])
def home():

    # row_list = get_user_credentials()
    if request.method == 'GET':
        print (request.method, 'default')
        return render_template('index.html', time_to_execute = 0 )
    elif request.method == 'POST':
        print (request.method)
        collect_data = []
        x='mysql'
        operation_keys = request.form.keys()
        selected_operation = [i for i in operation_keys]
        print ('Selected operations are', selected_operation)

        if(x=='mysql'):
            time_to_execute, collect_data = get_Column()
            # return render_template('index.html', output_files = row_list , time_to_execute = time_to_execute)
            return render_template('index.html', time_to_execute = time_to_execute)
        elif(x=='redis'):
            time_to_execute, collect_data = connectRedis()
            # return render_template('index.html', output_files = row_list , time_to_execute = time_to_execute)
            return render_template('index.html', time_to_execute = time_to_execute)




def get_Column():

    queries = ['SELECT home_dest FROM boatData' , 'SELECT name FROM boatData', 'SELECT ticket FROM boatData']
    conn = mysql.connection
    cursor = conn.cursor()
    start = time.time()
    collect_data = []

    for x in range(500):
        collect_data.append(cursor.execute(queries[random.randint(0,2)]))
    conn.commit
    end = time.time()

    print ('--------------------------------------')
    time_to_execute = end-start
    print(time_to_execute)
    print ('--------------------------------------')

    return time_to_execute, collect_data

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

def connectRedis():

    start = time.time()
    queries = ['SELECT home_dest FROM boatData' , 'SELECT name FROM boatData', 'SELECT ticket FROM boatData']
    conn = mysql.connection
    cursor = conn.cursor()
    TTL = 36
    collect_data = []
    R_SERVER = redis.Redis("adi.nbbbip.ng.0001.use2.cache.amazonaws.com", port="6379")
    for x in range(500):
        query = queries[random.randint(0,2)]
        hash = hashlib.sha224(query.encode('utf-8')).hexdigest()
        key = "sql_cache:" + hash
        if (R_SERVER.get(key)):
            data = R_SERVER.get(key)
            collect_data.append(data)
        else:
            # Do MySQL query
            data = cursor.execute(query)

            R_SERVER.set(key, data)
            R_SERVER.expire(key, TTL);
            data = R_SERVER.get(key)
            collect_data.append(data)

    end = time.time()

    print ('--------------------------------------')
    time_to_execute = end-start
    print(time_to_execute)
    print ('--------------------------------------')

    return time_to_execute, collect_data

def readCSVFile_1():
    conn = mysql.connection
    cursor = conn.cursor()
    # pclass, survived, name, sex, age, ticket, fare, cabin, home_dest = [], [], [], [], [], [], [], [], []
    with open('gg.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row_index, row in enumerate(reader):
            # pclass.append(row['pclass'])
            # survived.append(row['survived'])
            # home_dest.append(row['home.dest'])
            # name.append(row['name'])
            # sex.append(row['sex'])
            # age.append(row['age'])
            # ticket.append(row['ticket'])
            # fare.append(row['fare'])
            # home_dest.append(row['home.dest'])
            cursor.execute('''INSERT INTO boatData(pclass, survived, name, sex, age, ticket, fare, cabin, home_dest)
				              VALUES("{0}", "{1}", "{2}", "{3}", "{4}", "{5}", "{6}", "{7}", "{8}");'''.format(row['pclass'],
                                                                                                               row['survived'],
                                                                                                               row['name'].replace('"', ''),
                                                                                                               row['sex'],
                                                                                                               row['age'],
                                                                                                               row['ticket'],
                                                                                                               row['fare'],
                                                                                                               row['cabin'],
                                                                                                               row['home.dest']))

    conn.commit()

def readCSVFile():

    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute('''LOAD DATA LOCAL INFILE 'gg.csv' INTO TABLE boatData FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 LINES''')
    conn.commit()



if __name__ == '__main__':
    app.run()
