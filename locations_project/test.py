from flask_mysqldb import MySQL
from flask import Flask, render_template, request
import csv
import random
import time
import sys
import redis
import pickle
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
from pylab import figure, axes, pie, title, show
import csv
import matplotlib.pyplot as plt

app = Flask(__name__)
app.config['MYSQL_USER'] = 'username'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'tempdatabase'
app.config['MYSQL_HOST'] = 'hostname'
mysql = MySQL(app)


def part1():

    your_list = []
    with open('data2.csv', 'r') as f:
        reader = csv.reader(f)
        your_list = list(reader)

    names = your_list[:1]
    rest_data = your_list[1:]
    new1 = rest_data[:6]
    new2 = rest_data[6:12]
    new3 = rest_data[12:18]
    new4 = rest_data[18:24]
    new5 = rest_data[24:30]
    new6 = rest_data[30:]
    print (names)
    print (rest_data)
    return new1, new2, new3, new4, new5, new6, names

@app.route('/', methods=['GET','POST'])
def show_index():
    # create_table('data2')
    # readCSVFile()
    # rows = count_rows()
    # row_list = get_user_credentials()
    t1 = time.time()
    new1, new2, new3, new4, new5, new6, names = part1()
    time_to_execute , rows = copy_to_list()
    # kmeans_algo(rows)
    l1 = len(new1)
    l2 = len(new2)
    l3 = len(new3)
    l4 = len(new4)
    l5 = len(new5)
    l6 = len(new6)
    total = l1 + l2 + l3 + l4 + l5 + l6

    labels = ['C1', 'C2','C3','C4', 'C5','C6']
    sizes = [l1, l2, l3, l4, l5 , l6]
    plt.pie(sizes, labels=labels)
    plt.show()
    return render_template('index.html', new1 = new1, new2 = new2, new3=new3, new4=new4, new5=new5, new6=new6, names=names, time_to_execute = time.time()-t1)
    # return render_template('index.html', count = rows )





@app.route('/Check', methods=['GET','POST'])
def column():
    if request.method == 'GET':
        return render_template('index.html', time_to_execute = 0,row_list = [] )
    elif request.method == 'POST':
        this_column1 = request.form.get('column1')
        this_column2 = request.form.get('column2')
        c1 = '"' + this_height1 +'"'
        c2 = '"' + this_height2 +'"'
        state = '"' + this_state +'"'
        row_list = []
        # create_table('newtable')
        time_to_execute, row_list = on_column(c1,c2)
        return render_template('index.html', time_to_execute = time_to_execute, row_list = row_list )



def kmeans_algo(rows):
    kmeans = KMeans(n_clusters=6, random_state=0).fit(rows)
    print (kmeans.labels_)
    print (kmeans.cluster_centers_)
    return kmeans.cluster_centers_ , kmeans.labels_


def kmeans(tuple_row):
    c1 = []
    c2 = []


if __name__ == '__main__':
    app.run()
