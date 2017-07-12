from flask import Flask, render_template, request, redirect, make_response
app = Flask(__name__)



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















