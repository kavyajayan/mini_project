import dbconnect
#from passlib.hash import pbkdf2_sha256
from flask import Flask, flash, render_template, redirect, request
app = Flask(__name__)
app.secret_key = 'random string'

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
	flagroll=0;
	if request.method == 'POST':
			rollnos = dbconnect.fetchstud()
			for rollno in rollnos:
				if request.form['rollno']==rollno[0]:
					flagroll=1
			#if(len(data)!=0):
				#return redirect("/view/"+request.form['rollno'])
			if flagroll==0:
				return render_template('loginstudent.html', msg="No such register number")
			else:
				return ("Successfully logged in!")
			#	render_template('loginstudent.html', msg="Invalid register number")
	else:
			return render_template('loginstudent.html', msg="")

#@app.route('/view/<rollno>')
#def view():
	#if request.method == 'GET':
		#datas = fetchstudact(rollno)
		#return render_template('/view'),lists=datas)

@app.route('/loginfaculty', methods=['GET','POST'])
def loginfaculty():
	flagf=0
	flagf2=0
	if request.method == 'POST':
		datas = dbconnect.fetchfac()
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
			return render_template('loginfaculty.html',msg="No such faculty ID")
		else:
			if flagf2==0:
				return render_template('loginfaculty.html', msg="Invalid password")
			else:
				facid=request.form['facid']
				return render_template('facultymain.html', facid=facid)
	else:
			return render_template('loginfaculty.html', msg="")


@app.route('/facultymain/<facid>', methods=['POST'])
def facultymain(facid):
	if request.method == 'POST':
		if 'actsubmit' in request.form:
			if facid=="1":
				return ("successfull")
		#if view in request.form:
			#return redirect("/view/"+request.form['rollno'])
		#if 'actsubmit' in request.form:
			#dbconnect.insertstudact(request.form['regno'], request.form['actid'])
			#flash('Student activity successfully inserted!')
			#return  render_template('facultymain.html')

@app.route('/facultymain', methods=['GET'])
def facultymain():
	if request.method=='GET':
		render_template('facultymain')

if __name__== '__main__':
	app.debug = True
	app.run(port=3000)
