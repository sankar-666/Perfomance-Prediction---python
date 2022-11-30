from flask import *
from database import *
from core import *


admin=Blueprint('admin',__name__)


@admin.route('/adminhome')
def adminhome():
	return render_template("admin_home.html")

@admin.route('/admin_view_students',methods=['get','post'])
def admin_view_students():
	data={}
	s="select * from students inner join courses using (course_id)"
	res=select(s)
	data['b']=res
	return render_template("admin_view_students.html",data=data)

@admin.route('/admin_manage_course',methods=['get','post'])
def admin_manage_course():
	data={}
	if 'submit' in request.form:
		c=request.form['ct']
		d=request.form['cd']
		print(c,d)
		q="insert into courses values(null,'%s','%s')"%(c,d)
		insert(q)
		return redirect(url_for('admin.admin_manage_course'))
	s="select * from courses "
	res=select(s)
	data['b']=res

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None 

	if action=="delete":
		q="delete from courses where course_id='%s'"%(id)
		delete(q)
		return redirect(url_for('admin.admin_manage_course'))

	if action=="update":
		q="select * from courses where course_id='%s'"%(id)
		res=select(q)
		data['up']=res
	if 'update' in request.form:
		u=request.form['ct']
		p=request.form['cd']
		print(u,p)
		q="update courses set course_title='%s',course_description='%s'where course_id='%s'"%(u,p,id)
		update(q)
		return redirect(url_for('admin.admin_manage_course'))

	return render_template("admin_manage_course.html",data=data)

@admin.route('/admin_manage_subjects',methods=['get','post'])
def admin_manage_subjects():
	data={}
	q="select * from courses"
	res=select(q)
	data['cs']=res
	if 'submit' in request.form:
		a=request.form['cs']
		s=request.form['sn']
		de=request.form['sd']
		print(a,s,de)
		q="insert into subjects values(null,'%s','%s','%s')"%(a,s,de)
		insert(q)
	e="select * from subjects inner join courses using (course_id)"
	res=select(e)
	data['s']=res

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None 

	if action=="delete":
		q="delete from subjects where subject_id='%s'"%(id)
		delete(q)
		return redirect(url_for('admin.admin_manage_subjects'))

	if action=="update":
		q="select * from subjects where subject_id='%s'"%(id)
		res=select(q)
		data['upp']=res
	if 'update' in request.form:
		a=request.form['cs']
		u=request.form['sn']
		p=request.form['sd']
		print(a,u,p)
		q="update subjects set course_id='%s',subject_name='%s',subject_description='%s'where subject_id='%s'"%(a,u,p,id)
		update(q)
		return redirect(url_for('admin.admin_manage_subjects'))

	return render_template("admin_manage_subjects.html",data=data)




@admin.route('/admin_manage_faculties',methods=['get','post'])
def admin_manage_faculties():
	data={}
	q="select * from subjects"
	res=select(q)
	data['ss']=res
	if 'submit' in request.form:
		a=request.form['ss']
		f=request.form['fn']
		l=request.form['ln']
		p=request.form['phn']
		e=request.form['email']
		q=request.form['ql']
		u=request.form['uname']
		ps=request.form['psswd']
		print(a,f,l,p,e,q)
		r="insert into login values(null,'%s','%s','faculty')"%(u,ps)
		lid=insert(r)
		q="insert into faculty values(null,'%s','%s','%s','%s','%s','%s','%s')"%(lid,a,f,l,p,e,q)
		insert(q)
		return redirect(url_for('admin.admin_manage_faculties'))

	s="select * from faculty inner join subjects using (subject_id)"
	res=select(s)
	data['e']=res

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None 

	if action=="delete":
		q="delete from faculty where login_id='%s'"%(id)
		delete(q)
		w="delete from login where login_id='%s'"%(id)
		delete(w)
		return redirect(url_for('admin.admin_manage_faculties'))
	if action=="update":
		q="select * from faculty where login_id='%s'"%(id)
		res=select(q)
		data['upp']=res
	if 'update' in request.form:
		b=request.form['ss']
		u=request.form['fn']
		l=request.form['ln']
		n=request.form['phn']
		e=request.form['email']
		qu=request.form['ql']
		print(b,u,l,n,e,qu)
		q="update faculty set subject_id='%s',first_name='%s',last_name='%s',phone='%s',email='%s',qualification='%s'where login_id='%s'"%(b,u,l,n,e,qu,id)
		update(q)
		return redirect(url_for('admin.admin_manage_faculties'))

	return render_template("admin_manage_faculties.html",data=data)	

@admin.route('/admin_view_doubts',methods=['get','post'])
def admin_view_doubts():
	data={}
	s="SELECT *, CONCAT(first_name,' ',last_name)AS `name` FROM students INNER JOIN doubts USING (student_id) inner join notes using (note_id)"
	res=select(s)
	data['s']=res
	return render_template("admin_view_doubts.html",data=data)




@admin.route('/knowledgearea',methods=['get','post'])
def knowledgearea():
	data={}
	if 'action' in request.args:
		action=request.args['action']
		kid=request.args['kid']

	else:
		action=None

	if action=="update":
		q="select * from knowledgeareas where knowledge_area_id='%s'"%(kid)
		res=select(q)
		data['updatedata']=res
	if 'update' in request.form:
		k=request.form['kname']
		d=request.form['des']

		q="update knowledgeareas set knowledge_area_name='%s',description='%s' where knowledge_area_id='%s'"%(k,d,kid)
		update(q)
		flash("details updated")
		return redirect(url_for("admin.knowledgearea"))

	if action=="delete":
		
		q="delete from knowledgeareas where knowledge_area_id='%s'"%(kid)
		delete(q)
		flash("deleted successfully")
		return redirect(url_for("admin.knowledgearea"))

	if 'submit' in request.form:
		k=request.form['kname']
		d=request.form['des']

		q="insert into knowledgeareas values(null,'%s','%s')"%(k,d)
		insert(q)
		flash("subjects added successfully")

	q="select * from knowledgeareas"
	res=select(q)
	data['viewknowledges']=res
	return render_template("manage_knowledge_area.html",data=data)



@admin.route('/exercisesubject',methods=['get','post'])
def exercisesubject():
	data={}
	q="SELECT  DISTINCT subject_name,`assignment_date`,subject_id FROM exercise  INNER JOIN subjects USING(subject_id) ORDER BY assignment_date "
	res=select(q)

	data['viewsubject']=res
	return render_template("view_exercise_subject.html",data=data)


@admin.route('/submission',methods=['get','post'])
def submission():
	data={}
	ids=request.args['ids']
	data['ids']=ids
	# q1="SELECT answered_option_id,exercise_id,subject_name,correct_option_id FROM studentssubmission INNER JOIN exercise USING(exercise_id)INNER JOIN subjects USING(subject_id) WHERE subject_id='%s'"%(ids)
	# res1=select(q1)
	# a=['answered_option_id']
	# q2="SELECT answered_option_id,exercise_id,subject_name,correct_option_id,COUNT(answered_option_id=correct_option_id)AS opt FROM studentssubmission INNER JOIN exercise USING(exercise_id)INNER JOIN subjects USING(subject_id) WHERE subject_id='%s' AND answered_option_id=correct_option_id"%(ids)
	# res2=select(q2)
	# data['sub']=res2[0]['opt']
	# q3="SELECT answered_option_id,exercise_id,subject_name,correct_option_id,COUNT(answered_option_id <>correct_option_id)AS op FROM studentssubmission INNER JOIN exercise USING(exercise_id)INNER JOIN subjects USING(subject_id) WHERE subject_id='%s' AND answered_option_id<>correct_option_id"%(ids)
	# res3=select(q3)
	# data['cor']=res3[0]['op']

	
	q="SELECT *,concat(first_name,' ',last_name)as sname, subject_name AS tot FROM studentssubmissions INNER JOIN exercise USING(exercise_id) INNER JOIN subjects USING(subject_id)inner join students using(student_id) WHERE subject_id='%s' group by student_id "%(ids)
	print(q)
	res=select(q)
	data['viewsubmission']=res

	# score=0
	# s=0
	# score2=0
	# s2=0
	
	# print("a",a)
	# b=res1[0]['correct_option_id']
	# print("b",b)
	# for range in (1,len(res1)+1): 
	# 	if ['answered_option_id']==['correct_option_id']:
	# 		score+=1
	# 		print("score1",score)
	

	# 	s=score
	# 	print("s",s)
	# 	data['score']=s
		

		
	
	return render_template("view_submission.html",data=data)



@admin.route('/viewdetailed',methods=['get','post'])
def viewdetailed():
	data={}
	ids=request.args['ids']
	id=request.args['id']
	q1="SELECT answered_option_id,exercise_id,subject_name,correct_option_id FROM studentssubmissions INNER JOIN exercise USING(exercise_id)INNER JOIN subjects USING(subject_id) WHERE subject_id='%s'"%(ids)
	res1=select(q1)
	a=['answered_option_id']
	q2="SELECT answered_option_id,exercise_id,subject_name,correct_option_id,COUNT(answered_option_id=correct_option_id)AS opt FROM studentssubmissions INNER JOIN exercise USING(exercise_id)INNER JOIN subjects USING(subject_id) WHERE subject_id='%s' AND student_id='%s' AND answered_option_id=correct_option_id"%(ids,id)
	print(q2)
	res2=select(q2)
	data['sub']=res2[0]['opt']
	q3="SELECT answered_option_id,exercise_id,subject_name,correct_option_id,COUNT(answered_option_id <>correct_option_id)AS op FROM studentssubmissions INNER JOIN exercise USING(exercise_id)INNER JOIN subjects USING(subject_id) WHERE subject_id='%s' AND student_id='%s' AND answered_option_id<>correct_option_id"%(ids,id)
	res3=select(q3)
	data['cor']=res3[0]['op']

	q="SELECT *,concat(first_name,' ',last_name)as sname, subject_name,COUNT(exercise_id)AS tot FROM studentssubmissions INNER JOIN exercise USING(exercise_id) INNER JOIN subjects USING(subject_id)inner join students using(student_id) WHERE subject_id='%s' AND studentssubmissions.student_id='%s' "%(ids,id)
	res=select(q)
	data['viewsubmission']=res


	# ///////////////////////////////////

	q="SELECT knowledge_area_id,`knowledge_area_name`,COUNT(`knowledge_area_id`) as mark FROM `exerciseknowledges` INNER JOIN `knowledgeareas` USING(`knowledge_area_id`) WHERE `exercise_id` IN (SELECT DISTINCT(exercise_id) FROM `exerciseknowledges` WHERE `exercise_id`IN(SELECT exercise_id FROM exercise INNER JOIN studentssubmissions USING(exercise_id) WHERE subject_id='%s' AND student_id='%s' AND answered_option_id=correct_option_id)) GROUP BY `knowledge_area_id`" %(ids,id)
	res=select(q)
	data['knowledge']=res
	if "upload" in request.form:
		for i in range(0,len(res)):
			q="insert into perfomance values(null,'%s','%s','%s')" %(res[i]['knowledge_area_id'],id,res[i]['mark'])
			insert(q)
		q="SELECT knowledge_area_id FROM `exerciseknowledges` WHERE `exercise_id` NOT IN (SELECT DISTINCT(exercise_id) FROM `exerciseknowledges` WHERE `exercise_id`IN(SELECT exercise_id FROM exercise INNER JOIN studentssubmissions USING(exercise_id) WHERE subject_id='%s' AND student_id='%s' AND answered_option_id=correct_option_id)) GROUP BY `knowledge_area_id`" %(ids,id)
		res1=select(q)
		for j in range(0,len(res1)):
			q="insert into perfomance values(null,'%s','%s','%s')" %(res1[j]['knowledge_area_id'],id,'0')
			insert(q)
		i=train()
		if i=="No Data":
			flash("No Perfomance Uploaded")
		else:
			flash("Upload and Trained successfully")


	return render_template('viewanswereddetailed.html',data=data)



@admin.route('/predictperfomanceofstudent',methods=['get','post'])
def predictperfomanceofstudent():
	data={}
	q = "select * from knowledgeareas"
	res = select(q)
	data['areas']=res
	q="SELECT MAX(mycount) as counts FROM (SELECT COUNT(`knowledge_area_id`) mycount FROM `exerciseknowledges` INNER JOIN `exercise` USING(`exercise_id`) GROUP BY `knowledge_area_id`) temp"
	res=select(q)
	data['count']=res
	print(res)
	return render_template('predictperfomanceofstudent.html',data=data)


@admin.route('/admin_result',methods=['get','post'])
def admin_result():
	data={}
	q="SELECT MAX(mycount) as counts FROM (SELECT COUNT(`knowledge_area_id`) mycount FROM `exerciseknowledges` INNER JOIN `exercise` USING(`exercise_id`) GROUP BY `knowledge_area_id`) temp"
	res=select(q)
	data['count']=res
	q = "select * from knowledgeareas"
	res = select(q)
	data['areas']=res
	
	input = []
	if "predict" in request.form:
		for i in range(len(res)):
			input.append(0)
		for row in res:
			name  = "knowledege_" + str(row['knowledge_area_id'])
			# print(name)
			if name in request.form:
				level = float(request.form[name])
				knowledge_id = row['knowledge_area_id']
				input[knowledge_id-1] = level
		result = predict(input,2)
		return render_template('admin_result.html',data = result)
	else:
		return render_template('predictperfomanceofstudent.html',data=data)