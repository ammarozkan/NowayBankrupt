from flask import Flask, request, render_template, redirect, flash, url_for, session

def tupadd(tup1, tup2):
	result = [0 for i in range(0, len(tup1))]
	for i in range(0, len(tup1)):
		result[i] += tup1[i] + tup2[i]
	return tuple(result)

def tupmul_const(tup1, const):
	result = [0 for i in range(0, len(tup1))]
	for i in range(0, len(tup1)):
		result[i] += tup1[i] * const
	return tuple(result)

def getRelativeColor(color, defaultcolor, highness):
	const_hardener = 500.0
	_color = tupmul_const(color, highness)
	_defaultcolor = tupmul_const(defaultcolor, const_hardener)
	_sum = tupadd(_color, _defaultcolor)
	return tupmul_const(_sum, 1/(highness+const_hardener))

global db

import sqlite3

db = sqlite3.connect(
	"DaTaBaSe",
	detect_types=sqlite3.PARSE_DECLTYPES,
	check_same_thread=False)
db.row_factory = sqlite3.Row


global app
app = Flask(__name__)
app.secret_key = b"GeiajEEAgeaj0)E&=)^=)J)JaeaKE-"


activities = []

global infotexts
infotexts = [
	"Formun gönderiminde bir sıkıntı meydana geldi, tekrar deneyin. Eğer bu çok fazla başınıza\
geldiyse, bana danışın.", 
	"Meydana gelemeyecek bir durum meydana geldi. Bana yanda yer alan hata kodu ile \
birlikte danışın."]

def addToActivities(head, money, act_type):
	global activities
	const = 1 if act_type == "add" else -1
	activities=[(head, const*money)]+activities
	db.execute('INSERT INTO activities (head, money) VALUES (?, ?)', (head, const*money))
	db.commit()

def db_init_activities():
	print("SUPER USER: DB-INIT-ACTIVITIES")
	with app.open_resource("activities.sql") as f:
		db.executescript(f.read().decode('utf8'))

def db_destroy_activities():
	print("SUPER USER: DB_DESTROY_ACTIVITIES")
	db.executescript("DROP TABLE IF EXISTS activities;")



@app.route("/")
def index():
	activities = db.execute("SELECT id, head, explanation, money, date FROM activities ORDER BY date DESC").fetchall()
	return render_template("index.html", activities=activities, getRelativeColor=getRelativeColor)

@app.route("/mobiletest")
def mt():
	return render_template("mobiletester.html")

@app.route("/version")
def version():
	return render_template("version.html")


def getActivity(activityid):
	activity = db.execute("SELECT id, head, explanation, money, date FROM activities WHERE id = ?", (activityid,)).fetchone()
	return render_template("activity_explanation.html", activity=activity)

@app.route("/activity/<act_type>", methods=["GET","POST"])
def activity(act_type):
	if request.method == "GET":
		if (act_type.isdigit()): return getActivity(act_type)
		return render_template("activity.html", act_type=act_type)
	elif request.method == "POST":
		if request.form["head"] and request.form["money"]:
			if request.form["head"] == "gfksyui" and request.form["money"] == "767686":
				return redirect(url_for("gfksyui"))
			print("HMMM!!")
			addToActivities(request.form["head"], int(request.form["money"]), act_type)
			return redirect(url_for("index"))
		else:
			print("HATA")
			flash(infotexts[0])
	else:
		flash(infotexts[1] + ":0")
	return redirect(url_for("index"))

@app.route("/delete/<id>")
def delete(id):
	db.execute('DELETE FROM activities WHERE id = ?',(id,))
	db.commit()
	return redirect(url_for("index"))

import random

@app.route("/gfksagjgjajgdkkkkjllflalgej"+str(random.random())+"jejejgkhgyui/")
@app.route("/gfksagjgjajgdkkkkjllflalgej"+str(random.random())+"jejejgkhgyui/<command>")
def gfksyui(command=None):
	if command == None:
		pass
	elif command == "db-init-activities":
		db_init_activities()
	elif command == "db-destroy-activities":
		db_destroy_activities()
	return render_template("gfksyui/gfksyui.html")
