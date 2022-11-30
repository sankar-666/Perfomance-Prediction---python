from flask import Flask,Blueprint,render_template,request,redirect,url_for,session
from database import *

public=Blueprint('public',__name__)


@public.route('/',methods=['post','get'])
def home():
	if 'fff' in request.form:
		return redirect(url_for('public.home'))
	return render_template("home.html")


@public.route('/login',methods=['get','post'])
def login():
	if 'submit' in request.form:
		un=request.form['uname']
		pwd=request.form['pswd']
		print(un,pwd)
		q="select * from login where user_name='%s' and password='%s'"%(un,pwd)
		res=select(q)
		print(res)
		if res:
			utype=res[0]['user_type']
			session['loginid']=res[0]['login_id']
			if utype=="admin":
				return redirect(url_for('admin.adminhome'))
			elif utype=="faculty":
				a="select * from faculty where login_id='%s'"%(session['loginid'])
				res=select(a)
				if res:
					session['fid']=res[0]['faculty_id']
				return  redirect(url_for('faculty.facultyhome'))
			elif utype=="students":
				b="select * from students where login_id='%s'"%(session['loginid'])
				res=select(b)
				if res:
					session['sid']=res[0]['student_id']
					print(session['sid'])
				return  redirect(url_for('student.studenthome'))

	return render_template("login.html")
