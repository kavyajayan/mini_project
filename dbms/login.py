import dbconnect
#from passlib.hash import pbkdf2_sha256
from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
	if request.method== 'POST':
		if request.form['submit']=='student':
			return redirect('/loginstudent')
		if request.form['faculty']=='faculty':
			return redirect('/loginfaculty')
	else:
		return render_template('index.html')

@app.route("/loginstudent", methods=['GET','POST'])
def loginstudent():
	flag=0
	flag2=0
	if request.method == 'POST':
		datas= dbconnect.fetch()
		for row in datas:
			if request.form['studid']==row[0]:
				flag=1
				if request.form['pwd']==row[1]:
					flag2=1
				else:
					flag2=0
				break

			else:
				flag=0
		if flag==0:
			return redirect('/register')
		else:
			if flag2==0:
				return render_template('loginstudent.html', msg="Invalid password")
			else:
				return ("Successfully logged in!")
	else:
			return render_template('loginstudent.html', msg="")

@app.route('/loginstudent', methods=['GET','POST'])
def loginfaculty():
	flag=0
	flag2=0
	if request.method == 'POST':
		datas= dbconnect.fetch()
		for row in datas:
			if request.form['facid']==row[0]:
				flag=1
				if request.form['pwd']==row[1]:
					flag2=1
				else:
					flag2=0
				break

			else:
				flag=0
		if flag==0:
			return redirect('/register')
		else:
			if flag2==0:
				return render_template('loginfaculty.html', msg="Invalid password")
			else:
				return ("Successfully logged in!")
	else:
			return render_template('loginfaculty.html', msg="")

@app.route('/register', methods=['GET','POST'])
def register():
	if request.method == 'POST':
		#hash = pbkdf2_sha256.encrypt(request.form['pwd'], rounds=200000, salt_size=16)
		dbconnect.insert(request.form['uname'], request.form['pwd'])
		return redirect('/')
	else:
		return render_template('register.html')

if __name__== '__main__':
	app.run(port=3000)
