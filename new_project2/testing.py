from flask_mysqldb import MySQL
from flask import Flask, render_template, request


app = Flask(__name__)
app.config['MYSQL_USER'] = 'addherbs'
app.config['MYSQL_PASSWORD'] = 'hahahehe'
app.config['MYSQL_DB'] = 'project2'
app.config['MYSQL_HOST'] = 'mydb.cicid6gi032j.us-east-2.rds.amazonaws.com'
mysql = MySQL(app)



@app.route('/', methods=['GET','POST'])
def show_index():
    readCSVFile()
    # row_list = get_user_credentials()
    if request.method == 'GET':
        return render_template('index.html', time_to_execute = 0 )

def create_table():
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute( '''CREATE TABLE dept(
        name varchar(30),
        number varchar(30),
        manager varchar(30),
        date varchar(30)        
    );''')
    conn.commit
    print('created table')


def readCSVFile():
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute('''LOAD DATA LOCAL INFILE 'dept.txt' INTO TABLE dept FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 LINES;''')
    conn.commit()


if __name__ == '__main__':
    app.run()
