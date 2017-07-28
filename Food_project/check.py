import operator
import os
import csv
from os import listdir
from os.path import isfile, join
import sys

from io import StringIO
from PIL import Image
import base64
import MySQLdb
import PIL.Image

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


import MySQLdb
host = 'mysqladdherbs.mysql.database.azure.com'
user = 'addherbs@mysqladdherbs'
password = 'Haha@haha123'
dbname = 'azure'
# sqldb = MySQLdb.connect(host=host,user=user,passwd=password,db=dbname)
sqldb = MySQLdb.connect(host=host,user=user,passwd=password)
cur = sqldb.cursor()

path = 'C://Users//Cyther//Desktop//Q8//Food//Images//AlooGosht.JPG'
with open(path, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())

thedata = open(path, 'rb').read()

val1 = "'hell212ee3o212'"
query = "INSERT INTO azure.image VALUES('hey',(%s))"
cur.execute(query, (thedata,))

cursor.execute(query, (thedata,))
mydb.commit()
# cur.execute(query)
print(query)
sql1='select * from azure.image'
cursor.execute(sql1)
data=cursor.fetchall()
print(data)
# data1=base64.b64decode(data[0][0])
# file_like=StringIO(data[0][0])
# img=PIL.Image.open(data[0][1])
# img.show()
