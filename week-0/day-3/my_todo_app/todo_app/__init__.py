


import os

from flask import Flask
from flask import request
from flask_mysqldb import MySQL
from flask import render_template


# our fake db

todo_store = {}
todo_store['depo'] = ['Go for run', 'Listen Rock Music']
todo_store['shivang'] = ['Read book', 'Play Fifa', 'Drink Coffee']
todo_store['raj'] = ['Study', 'Brush']
todo_store['sanket'] = ['Sleep', 'Code']
todo_store['aagam'] = ['play cricket', 'have tea']

app = Flask(__name__, instance_relative_config=True)
	
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'goku1212'
app.config['MYSQL_DB'] = 'flaskapp'
mysql=MySQL(app)


	
@app.route('/add_todo', methods=['GET', 'POST'])
def add_todo():
	if request.method=='POST':
		data=request.form
		name=data['name']
		todo = data['todo']
		cur=mysql.connection.cursor()
		cur.execute("INSERT INTO users(name,todo) VALUES(%s,%s)",(name,todo))
		mysql.connection.commit()
		cur.close()
		return 'success'
	return render_template('index.html')

@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM users")
    if resultValue > 0:
        userDetails = cur.fetchall()
	return render_template('users.html',userDetails=userDetails)

if __name__ == '__main__':
	app.run(debug=True)

'''
		
def create_app(test_config=None):
	
    # create and configure the app
   	
	

	

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
	
	
	
    def select_todos(name):
        global todo_store
        return todo_store[name]

    def insert_todo(name, todo):
        global todo_store
        current_todos = todo_store[name]
        current_todos.append(todo)
        todo_store[name] = current_todos
        return

    def add_todo_by_name(name, todo):
        # call DB function
        insert_todo(name, todo)
        return

    def get_todos_by_name(name):
        try:
            return select_todos(name)
        except:
            return None
	
	
	@app.route('/index',methods=['GET','POST'])	
	def index():
		if request.method=='POST':
			data=request.form
			name=data['name']
			todo = data['todo']
			cur=mysql.connection.cursor()
			cur.execute["INSERT INTO users(name,todo) VALUES(%s,%s)",(name,todo)]
			mysql.connection.commit()
			cur.close()
			return 'success'
		return render_template('index.html')


    # http://127.0.0.1:5000/todos?name=duster
    @app.route('/todos')
    def todos():
        name = request.args.get('name')
        print('---------')
        print(name)
        print('---------')

        person_todo_list = get_todos_by_name(name)
        if person_todo_list == None:
            return render_template('404.html'), 404
        else:
            return render_template('todo_view.html',todos=person_todo_list)

	
	
	@app.route('/add_todos',methods=['GET','POST'])
	def add_todos():
		if request.method=='POST':
			data=request.form
			name=data['name']
			todo = data['todo']
			cur=mysql.connection.cursor()
			cur.execute["INSERT INTO users(name,todo) VALUES(%s,%s)",(name,todo)]
			mysql.connection.commit()
			cur.close()
			return 'success'
		return render_template('index.html')
	
    
		
    return app
'''
