from flask_mysqldb import MySQL
from flask import Flask, render_template, request, redirect, url_for, session
import MySQLdb
from flask import Flask, render_template, request
import operator
import os
import csv
from os import listdir
from os.path import isfile, join
import random
import time

app = Flask(__name__)
HOST = 'host'
USER = 'user'
PASS= 'pass'
sql_db = MySQLdb.connect(host=HOST,user=USER,passwd=PASS)
cur = sql_db.cursor()



mydb = MySQLdb.connect(host=HOST,
    user=USER,
    passwd=PASS,
    )
cursor = mydb.cursor()


def createDatabaseAzure():
    query = "CREATE DATABASE azure"
    cur.execute (query)

def create_table():
    query_1 = """CREATE TABLE azure.main(
              file_name VARCHAR (30),
                weight INTEGER (30),
                fat INTEGER(30),
                number_of_calories INTEGER (30),
                ingredients varchar(500),
                genre varchar(30)
            );"""
    cur.execute (query_1)


def insert(filename,row1,row2,type):
    cursor = mydb.cursor ()
    ingredients = ''
    count = 1
    filename = "'"+filename +"'"
    type = "'" + type + "'"

    for each in row2:
        if (count ==1):
            count +=1
            ingredients = each
        else:
            ingredients = ingredients + ',' + each
    ingredients = "'" + ingredients + "'"
    query = "INSERT INTO azure.main VALUES(%s,%d , %d, %d, %s,%s );" % (filename,int(row1[0]),int(row1[1]),
                                                                        int(row1[2]), ingredients,type)
    print (query)
    cursor.execute(query)
    mydb.commit()
    cursor.close()

def get_records():
    cursor = mydb.cursor ()
    query= 'select * from azure.main'
    cursor.execute (query)
    data = cursor.fetchall()
    cursor.close ()
    return data

@app.route ('/', methods=['GET', 'POST'])
def show_index():
    if request.method == 'GET':
        start = time.time()
        # createDatabaseAzure()
        # create_table ()
        # # readCSVs()
        # readFiles()
        data = get_records()
        return render_template('display_records.html', time_to_execute = time.time() - start , data = data )
    elif request.method == 'POST':
        return render_template ('index.html', time_to_execute=0)

@app.route ('/listFood', methods=['GET', 'POST'])
def show():
    if request.method == 'GET':
        start = time.time()
        data = get_records()
        return render_template('display_records.html', time_to_execute = time.time() - start , data = data )
    elif request.method == 'POST':
        start = time.time ()
        this_column1 = request.form.get ('item')
        this_column2 = request.form.get ('cal')
        print(this_column1,' ' ,this_column2)
        data =calculate(this_column1, this_column2)

        return render_template ('display_records.html', time_to_execute=time.time () - start, data=data)

def calculate(this_column1, this_column2):
    cursor = mydb.cursor ()
    query = 'select * from azure.main where calories >' + this_column2 + '&&' + this_column1 in ingredients
    cursor.execute (query)
    data = cursor.fetchall ()
    cursor.close ()
    return data


def readCSVs():
    path = 'C://Users//Cyther//Desktop//Q8//Food//CSV'
    count = 0
    st = {}
    dishes = {}
    onlyfiles = [f for f in listdir (path) if isfile (join (path, f))]
    # print(onlyfiles)
    for fname in onlyfiles:
        # print (fname)
        filename = fname.split ('.')
        if filename[1] == 'csv':
            count = count + 1
            currentpath = path + '//' + fname
            # print(currentpath)
            directory = os.path.normpath (currentpath)
            with open (directory, newline='') as f:
                reader = csv.reader (f)
                countOfRowNumber = 0
                for row in reader:
                    countOfRowNumber += 1
                    row1 = []
                    row2 = []
                    row3=[]
                    for each in row:
                        if countOfRowNumber == 2:
                            if each != '':
                                currentItem = '' + each + ''
                                currentItem = currentItem.strip ()
                                if currentItem in st:
                                    value = st.get (currentItem)
                                    st[currentItem] = value + 1
                                elif currentItem not in st:
                                    st[currentItem] = 1

                                if currentItem in dishes:
                                    value = dishes.get(currentItem)
                                    dishes[currentItem] = value + ',' + fname
                                elif currentItem not in dishes:
                                    dishes[currentItem] = fname
    for dish in dishes:
        print (dish + '====>' + dishes[dish])

    sorted_x = sorted (st.items (), key=operator.itemgetter (1), reverse=True)
    print (sorted_x)

def readFiles():
    path = 'C://Users//Cyther//Desktop//Q8//Food//CSV'
    count = 0

    onlyfiles = [f for f in listdir (path) if isfile (join (path, f))]
    for fname in onlyfiles:
        filename = fname.split ('.')
        if filename[1] == 'csv':
            count = count + 1
            currentpath = path + '//' + fname
            directory = os.path.normpath (currentpath)
            with open (directory, newline='') as f:
                reader = csv.reader (f)
                countOfRowNumber = 0
                row1 = []
                row2 = []
                type=''
                for row in reader:
                    countOfRowNumber += 1
                    for each in row:
                        currentItem = '' + each + ''
                        currentItem = currentItem.strip ()
                        if currentItem != '':
                            if countOfRowNumber == 1:
                                row1.append(currentItem)
                            if countOfRowNumber == 2:
                                row2.append(currentItem)
                            if countOfRowNumber == 3:
                                type = currentItem

                insert(fname,row1,row2,type)



if __name__ == '__main__':
    app.run()
