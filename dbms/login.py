import dbconnect
#from passlib.hash import pbkdf2_sha256
from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
	if request.method == 'POST':
		if 'stud' in request.form:
			return redirect('/loginstudent')
		elif 'fac' in request.form:
			return redirect('/loginfaculty')
	else:
		return render_template('index.html')

@app.route('/loginstudent', methods=['GET','POST'])
def loginstudent():
	flags=0
	flags2=0
	if request.method == 'POST':
			datas = dbconnect.fetchstudact()
			if(len(data)!=0)
				return redirect("/view/"+request.form['rollno'])
			else
				render_template('loginstudent.html', msg="Invalid register number")
	else:
			return render_template('loginstudent.html', msg="")

@app.route('/view/<rollno>')
def view():
	if request.method == 'GET'
		datas = fetchstudact(rollno);
		return render_template('/view'#pass datas)

@app.route('/loginfaculty', methods=['GET','POST'])
def loginfaculty():
	flagf=0
	flagf2=0
	if request.method == 'POST':
		datas= dbconnect.fetchfac()
		for row in datas:
			if request.form['facid']==row[0]:
				flagf=1
				if request.form['pwd']==row[1]:
					flagf2=1
				else:
					flagf2=0
				break
			else:
				flagf=0
		if flagf==0:
			return redirect('/registerfaculty')
		else:
			if flagf2==0:
				return render_template('loginfaculty.html', msg="Invalid password")
			else:
				return ("Successfully logged in!")
	else:
			return render_template('loginfaculty.html', msg="")

@app.route('/registerfaculty', methods=['GET','POST'])
def registerfaculty():
	if request.method == 'POST':
		#hash = pbkdf2_sha256.encrypt(request.form['pwd'], rounds=200000, salt_size=16)
		dbconnect.insertfac(request.form['facid'], request.form['pwd'], request.form['clas'])
		return redirect('/loginfaculty')
	else:
		return render_template('registerfaculty.html')

@app.route('/facultyhome', methods=['GET', 'POST'])
def facultyhome():
	if request.method == 'POST':
		if view in request.form:
			return redirect("/view/"+request.form['rollno'])
		if actsubmit in request.form:
			insertstudact(request.form['rollno'], request.form.['actid'])
			return render_template('/facultyhome')
	else:
		return render_template('/facultyhome')

if __name__== '__main__':
	app.run(port=3000)
