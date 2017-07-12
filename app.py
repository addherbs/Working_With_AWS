from flask import Flask, render_template, request, redirect, make_response
app = Flask(__name__)

AWS_ACCESS_KEY_ID = 'Access Key'
AWS_SECRET_ACCESS_KEY = 'Secret Key'

session = Session(aws_access_key_id=AWS_ACCESS_KEY_ID,
                  aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                  region_name='us-east')
conn = S3Connection(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)

s3 = boto3.resource('s3',aws_access_key_id=AWS_ACCESS_KEY_ID,
         aws_secret_access_key=AWS_SECRET_ACCESS_KEY, config=Config(signature_version='s3v4'))
bucket = s3.Bucket('Your Bucket')



@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        this_username = request.form.get('uname')
        this_password = request.form.get('pass')
        if this_username == username and this_password == password:
            return redirect('/home')
        else:
            return redirect('/')


if __name__ == '__main__':
    app.run()



# Printing List of file naames that are thre in thw buckte
@app.route('/home', methods= ['GET', 'POST'])
def show_home():
    if request.method=='GET':
        list_of_filenames = []
        for key in s3.Bucket('filebucket1234').objects.all():
            list_of_filenames.append(key.key)
        return render_template('index.html', list_of_filenames = list_of_filenames)
    elif request.method == 'POST':
        this_file = request.files['filename']
        this_number = request.form['number']
        this_file_name = this_file.filename
        final_file_name = this_number + this_file_name
        this_file_contents = this_file.stream.read()
        print ('file Name = ', this_file_name)
        print ('file Contents = ', this_file_contents)
        s3.Bucket('filebucket1234').put_object(Body=this_file_contents, ContentEncoding='utf-8', Key=final_file_name)
        return redirect('/home')










