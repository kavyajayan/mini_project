import dbconnect
#from passlib.hash import pbkdf2_sha256
from flask import Flask, flash, render_template, redirect, request, make_response
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
			if flagroll==0:
				return render_template('loginstudent.html', msg="No such register number")
			else:
				roll=request.form['rollno']
				resp1 = make_response(render_template('viewstud.html', name=""))
				resp1.set_cookie('rollno',roll)
				return resp1;
			#	render_template('loginstudent.html', msg="Invalid register number")
	else:
			return render_template('loginstudent.html', msg="")

@app.route('/viewstud', methods=['GET','POST'])
def viewstud():
	rno=request.cookies.get('rollno')
	actnames = dbconnect.fetchstudactname(rno)
	actlevels = dbconnect.fetchstudactlevel(rno)
	actpoints = dbconnect.fetchstudactpoints(rno)
	if request.method == 'POST':
		return render_template('viewstud.html', names=actnames, levels=actlevels, points=actpoints)
	else:
		return render_template('viewstud.html', name="")

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
				faculty = request.form['facid']
				resp = make_response(render_template('facultymain.html', mess=""))
				resp.set_cookie('facid',faculty)
				return resp
	else:
			return render_template('loginfaculty.html', msg="")


@app.route('/facultymain', methods=['GET','POST'])
def facultymain():
	if request.method == 'POST':
		fac=request.cookies.get('facid')
		if 'actsubmit' in request.form:
				rolls=dbconnect.checkfac(fac)
				for roll in rolls:
					if request.form['regno']==roll[0]:
					#dbconnect.insertstudact(request.form['regno'], request.form['actid'])
						return  render_template('facultymain.html', mess="Succesfully inserted activity "+request.form['actid']+" of reg no "+request.form['regno'])
				else:
					return  render_template('facultymain.html', mess="No such student in your class!")
	else:
		return  render_template('facultymain.html', mess="")

if __name__== '__main__':
	app.debug = True
	app.run(port=3000)
