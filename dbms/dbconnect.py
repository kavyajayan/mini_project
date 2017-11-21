import sqlite3
DATABASE = 'database.db'

#def insertstud(rollno,name,clas):
	#con1 = sqlite3.connect(DATABASE)
	#cur1 = con1.cursor()
	#cur1.execute("INSERT INTO student (rollno,name,clas) values (?,?,?,?)", (rollno,name,clas,password))
	#con1.commit()
	#con1.close()

def fetchstud():
	con2 = sqlite3.connect(DATABASE)
	cur2 = con2.cursor()
	cur2.execute("SELECT rollno,name from student")
	data=cur2.fetchall()
	con2.close()
	return data

def insertfac(facid,password,clas):
	con3 = sqlite3.connect(DATABASE)
	cur3 = con3.cursor()
	cur3.execute("INSERT INTO faculty (facid,password,clas) values (?,?,?)", (facid,password,clas))
	con3.commit()
	con3.close()

def fetchfac():
	con4 = sqlite3.connect(DATABASE)
	cur4 = con4.cursor()
	cur4.execute("SELECT facid, password from faculty")
	data = cur4.fetchall()
	con4.close()
	return data

#def insertact(activity,activitylevel,points):
	#con5 = sqlite3.connect(DATABASE)
	#cur5 = con5.cursor()
	#cur5.execute("INSERT INTO act (aid,activity,activitylevel,points) values (?,?,?,?)", (aid,activity,activitylevel,points))
	#con5.commit()
	#con5.close()

#def fetchact():
	#con6 = sqlite3.connect(DATABASE)
	#cur6 = con6.cursor()
	#cur6.execute("SELECT aid,activity,activitylevel,points from act")
	#data=cur6.fetchall()
	#con6.close()
	#return data

def insertstudact(rollno,aid):
	con7 = sqlite3.connect(DATABASE)
	cur7 = con7.cursor()
	cur7.execute("INSERT INTO studact (rollno,aid) values (?,?)", (rollno,aid))
	con7.commit()
	con7.close()


def fetchstudact(roll):
	con8 = sqlite3.connect(DATABASE)
	cur8 = con8.cursor()
	cur8.execute("SELECT activity,activitylevel,points from act,studact where act.aid=studact.aid and rollno=roll")
	data=cur8.fetchall()
	con8.close()
	return data

def sump(roll):
	con9 = sqlite3.connect(DATABASE)
	cur9 = con9.cursor()
	cur9.execute("SELECT sum(points) as sum from studact,act where act.aid=studact.aid and rollno=roll")
	data=cur9.fetchall()
	con9.close()
	return data
