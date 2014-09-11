from app import app
from flask import render_template , jsonify, request,json


import test


@app.route('/')
@app.route('/index')
def index():
	return render_template("index.html")

@app.route('/crypto', methods = ['POST'])
def crypto():
	jm = request.json
	m = int(jm['messaggio'])
	chk = jm['attributi']
	att = []
	for x in chk:
		att.append(int(x))
	
	E = test.cry.encrypto(m,att)

	alb1 = test.decrypt1(E, test.pk1)
	alb2 = test.decrypt2(E, test.pk2)

	lis = {'messaggio' : test.encrypt(m,att) , 'alb1' : alb1 , 'alb2' : alb2 }
	return jsonify(lis)