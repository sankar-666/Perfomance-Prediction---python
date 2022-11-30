from flask import *
from database import *

faculty=Blueprint('faculty',__name__)

@faculty.route('/facultyhome')
def facultyhome():
	return render_template("faculty_home.html")

@faculty.route('/faculty_manage_student',methods=['get','post'])
def faculty_manage_student():
	data={}
	e="select * from courses"
	res=select(e)
	data['cs']=res
	if 'submit' in request.form:
		f=request.form['fn']
		l=request.form['ln']
		c=request.form['cs']
		p=request.form['phn']
		e=request.form['email']
		g=request.form['gn']
		d=request.form['dt']
		h=request.form['hn']
		pl=request.form['plc']
		pi=request.form['pn']
		un=request.form['un']
		ps=request.form['psw']

		print(f,l,c,p,e,g,d,h,pl,pi)
		r="insert into login values(null,'%s','%s','students')"%(un,ps)
		lid=insert(r)
		q="insert into students values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(lid,f,l,c,p,e,g,d,h,pl,pi)
		insert(q)
		return redirect(url_for('faculty.faculty_manage_student'))
	s="select * from students inner join courses using (course_id)"
	res=select(s)
	data['b']=res

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None 
	if action=="delete":
		q="delete from students where login_id='%s'"%(id)
		delete(q)
		w="delete from login where login_id='%s'"%(id)
		delete(w)
		return redirect(url_for('faculty.faculty_manage_student'))
	if action=="update":
		q="select * from students where login_id='%s'"%(id)
		res=select(q)
		data['upp']=res
	if 'update' in request.form:
		fs=request.form['fn']
		ls=request.form['ln']
		cr=request.form['cs']
		ph=request.form['phn']
		em=request.form['email']
		ge=request.form['gn']
		da=request.form['dt']
		ho=request.form['hn']
		pla=request.form['plc']
		pin=request.form['pn']
		print(fs,ls,cr,ph,em,ge,da,ho,pla,pin)
		q="update students set first_name='%s',last_name='%s',course_id='%s',phone='%s',email='%s',gender='%s',dob='%s',house_name='%s',place='%s',pincode='%s' where login_id='%s'"%(fs,ls,cr,ph,em,ge,da,ho,pla,pin,id)
		update(q)
		return redirect(url_for('faculty.faculty_manage_student'))
	return render_template("faculty_manage_student.html",data=data)

@faculty.route('/faculty_manage_notes',methods=['get','post'])
def faculty_manage_notes():
	data={}
	fid=session['fid']
	e="select * from courses"
	res=select(e)
	data['cs']=res
	if 'submit' in request.form:
		c=request.form['cs']
		ti=request.form['t']
		de=request.form['d']
		n=request.form['nd']
		print(c,ti,de,n)
		q="insert into notes values(null,'%s','%s','%s','%s','%s')"%(fid,c,ti,de,n)
		insert(q)
		return redirect(url_for('faculty.faculty_manage_notes'))
	s="select * from notes inner join courses using (course_id)"
	res=select(s)
	data['b']=res

	
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=="delete":
		q="delete from notes where note_id='%s'"%(id)
		delete(q)
		return redirect(url_for('faculty.faculty_manage_notes'))
	if action=="update":
		q="select * from notes where note_id='%s'"%(id)
		res=select(q)
		data['upp']=res
	if 'update' in request.form:
		ce=request.form['cs']
		ti=request.form['t']
		de=request.form['d']
		n=request.form['nd']
		print(ce,ti,de,n)
		q="update notes set course_id='%s',title='%s',description='%s',note_date='%s' where note_id='%s'"%(ce,ti,de,n,id)
		update(q)
		return redirect(url_for('faculty.faculty_manage_notes'))
	return render_template("faculty_manage_notes.html",data=data)

@faculty.route('/faculty_manage_assignment',methods=['get','post'])
def faculty_manage_assignment():
	data={}
	fcid=session['fid']
	d="select * from courses"
	res=select(d)
	data['cs']=res
	if 'submit' in request.form:
		ce=request.form['cs']
		ti=request.form['tt']
		de=request.form['dc']
		m=request.form['mm']
		a=request.form['ad']
		f=request.form['fd']
		print(ce,ti,de,m,a,f)
		q="insert into assignments values(null,'%s','%s','%s','%s','%s','%s','%s')"%(fcid,ce,ti,de,m,a,f)
		insert(q)
		return redirect(url_for('faculty.faculty_manage_assignment'))
	s="select * from assignments inner join courses using (course_id)"
	res=select(s)
	data['b']=res
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=="delete":
		q="delete from assignments where assignment_id='%s'"%(id)
		delete(q)
		return redirect(url_for('faculty.faculty_manage_assignment'))
	if action=="update":
		q="select * from assignments where assignment_id='%s'"%(id)
		res=select(q)
		data['upp']=res
	if 'update' in request.form:
		c=request.form['cs']
		t=request.form['tt']
		d=request.form['dc']
		mo=request.form['mm']
		ad=request.form['ad']
		fd=request.form['fd']
		print(c,t,d,mo,ad,fd)
		q="update assignments set course_id='%s',title='%s',decription='%s',maximum_mark='%s',assignment_date='%s',fial_date_submission='%s' where assignment_id='%s'"%(c,t,d,mo,ad,fd,id)
		update(q)
		return redirect(url_for('faculty.faculty_manage_assignment'))
	return render_template("faculty_manage_assignment.html",data=data)

@faculty.route('/faculty_view_doubts',methods=['get','post'])
def faculty_view_doubts():
	data={}
	s="SELECT *, CONCAT(first_name,' ',last_name)AS `name` FROM students INNER JOIN doubts USING (student_id)"
	res=select(s)
	data['s']=res
	return render_template("faculty_view_doubts.html",data=data)

@faculty.route('/faculty_send_reply',methods=['get','post'])
def faculty_send_reply():
	data={}
	id=request.args['id']
	if 'submit' in request.form:
		re=request.form['rp']
		print(re)
		q="update doubts set reply='%s' where doubt_id='%s'"%(re,id)
		update(q)
		print(q)
		return redirect (url_for('faculty.faculty_view_doubts'))
	return render_template("faculty_send_reply.html",data=data)	

@faculty.route('/faculty_view_submission',methods=['get','post'])
def faculty_view_submission():
	data={}
	s="SELECT *, CONCAT(first_name,' ',last_name)AS `name` FROM students INNER JOIN submissions USING (student_id)"
	res=select(s)
	data['s']=res

	return render_template("faculty_view_submission.html",data=data)	

@faculty.route('/faculty_award_marks',methods=['get','post'])
def faculty_award_marks():
	data={}
	id=request.args['id']
	if 'submit' in request.form:
		f=request.form['fn']
		m=request.form['ma']
		print(f,m)
		q="update submissions set faculty_note='%s', mark_awarded='%s' where submission_id='%s'"%(f,m,id)
		update(q)
		return redirect (url_for('faculty.faculty_manage_assignment'))
	return render_template("faculty_award_marks.html",data=data)


@faculty.route('/manageexercise',methods=['get','post'])
def manageexercise():
	data={}
	q="select * from subjects"
	res=select(q)
	data['viewsub']=res
	q="select * from knowledgeareas"
	res=select(q)
	data['viewknowledge']=res
	if 'submit' in request.form:
		noofoption=request.form['noofoption']
		answersel=request.form['answersel']
		sub=request.form['sub']
		knldge=request.form['knldge']
		qstn=request.form['qstn']
		
		q="insert into exercise values(null,'%s','%s','%s',curdate())"%(sub,qstn,noofoption)
		id=insert(q)
		q1="insert into `exerciseknowledges` values(null,'%s','%s')"%(id,knldge)
		insert(q1)
		j=1
		for i in range(0,int(noofoption)):
			val=request.form['text'+str(j)]
			
			if int(j)==int(answersel):
				status="Yes"
			else:
				status="No"
			q="insert into exerciseoptions values(null,'%s','%s','%s')" %(id,val,status)
			ids=insert(q)
			j=j+1
		q="select option_id from exerciseoptions where exercise_id='%s' and status='yes'"%(id)
		res=select(q)
		print(res)
		a=res[0]['option_id']
		print(a)
		
		q="update exercise set correct_option_id='%s' where exercise_id='%s'"%(a,id)
		update(q)


			
		
	return render_template("manage_exercise.html",data=data)