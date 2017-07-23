@app.route('/getList', methods=['GET', 'POST'])
def getList():
	start = time.time()
    if request.method == 'GET':
        mylist = courses_list ()
        return render_template ('courses.html', time=time.time () - start, course_list=row_list)
    elif request.method == 'POST':
        this_name = request.form.get ('instructors_name')
        print (this_name)
        name = '"' + this_name + '"'
        row_list = []
        row_list = on_name (name)
        return render_template ('courses.html', time=time.time () - start, course_list=row_list)
		
def on_name(name):
    conn = mysql.connection
    cursor = conn.cursor ()
    query = 'select * from classes where Instructor = ' + name + ';'
    cursor.execute (query)
    data = cursor.fetchall ()
    return data
	  