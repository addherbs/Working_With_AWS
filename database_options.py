from boto3.session import Session
import os
import boto3
import boto
import requests
import tkinter as tk
import tkinter.filedialog as tkf
from boto.s3.connection import S3Connection
from boto.s3.connection import Location
from boto.s3.key import Key
from botocore.client import Config

AWS_ACCESS_KEY_ID = 'Access Key'
AWS_SECRET_ACCESS_KEY = 'Secret Key'

session = Session(aws_access_key_id=AWS_ACCESS_KEY_ID,
                  aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                  region_name='us-east')
conn = S3Connection(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)

s3 = boto3.resource('s3',aws_access_key_id=AWS_ACCESS_KEY_ID,
         aws_secret_access_key=AWS_SECRET_ACCESS_KEY, config=Config(signature_version='s3v4'))
bucket = s3.Bucket('Your Bucket')


# conn = S3Connection(access, secretA)
conn = S3Connection(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)

# ec2 = session.resource('ec2')
# s3=session.resource('s3')

s3 = boto3.resource('s3',aws_access_key_id=AWS_ACCESS_KEY_ID,
         aws_secret_access_key=AWS_SECRET_ACCESS_KEY, config=Config(signature_version='s3v4'))
bucket = s3.Bucket('filebucket1234')
# s3.Object('filebucket1234', 'hello.py').put(Body=open("C:\\Users\\Cyther\\Desktop\\Assignment1\\hello.py", 'rb'))

# mybucket = conn.get_bucket('filebucket1234', validate=False)
# mybucket.list()


#Deleting a bucket
def DeleteBucket():
    conn.delete_bucket('mybuckethsiaujdnqwiuskjnd')

# Listing all buckets
def List_buckets():
    rs = conn.get_all_buckets()
    print (rs)

#Creating a bucket
def CreateBucket():
    my_bucket = 'filebucket1234'
    conn.create_bucket('mybuckethsiaujdnqwiuskjnd', location=Location.EU)

def upload():
    root = tk.Tk()
    open = tkf.askopenfile(parent=root,mode='rb',title='Choose a file')
    abs_path = os.path.abspath(open.name)
    print (abs_path)
    fName = os.path.basename(abs_path)
    fContent=open.read()
    print(fName)
    s3.Bucket ('filebucket1234').upload_file (abs_path, fName)
    print ('Upload Successful')
