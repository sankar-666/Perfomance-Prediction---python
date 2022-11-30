from flask import *
from database import *
import uuid
import numpy
from core import *

student=Blueprint('student',__name__)

@student.route('/studenthome')
def studenthome():
	return render_template("student_home.html")

@student.route('/student_view_subject',methods=['get','post'])
def student_view_subject():
	data={}
	s="select * from subjects inner join courses using (course_id)"
	res=select(s)
	data['s']=res
	return render_template("student_view_subject.html",data=data)

@student.route('/student_view_faculties',methods=['get','post'])
def student_view_faculties():
	data={}
	s="select * from faculty inner join subjects using (subject_id)"
	res=select(s)
	data['s']=res
	return render_template("student_view_faculties.html",data=data)

@student.route('/student_view_notes',methods=['get','post'])
def student_view_notes():
	data={}
	s="select * from notes inner join courses using (course_id)"
	res=select(s)
	data['s']=res
	return render_template("student_view_notes.html",data=data)

@student.route('/student_view_assignment',methods=['get','post'])
def student_view_assignment():
	data={}
	b="select * from assignments inner join courses using (course_id)"
	res=select(b)
	data['b']=res
	return render_template("student_view_assignment.html",data=data)

@student.route('/student_send_doubts',methods=['get','post'])
def student_send_doubts():
	data={}
	sid=session['sid']
	note_id=request.args['note_id']
	if 'submit' in request.form:
		c=request.form['dd']
		print(c)
		q="insert into doubts values(null,'%s','%s','%s','pending',curdate())"%(sid,note_id,c,)
		insert(q)
	s="select * from doubts inner join notes using (note_id)"
	res=select(s)
	data['s']=res
	return render_template("student_send_doubts.html",data=data)

@student.route('/student_add_submission',methods=['get','post'])
def student_add_submission():
	data={}
	id=request.args['id']
	sid=session['sid']
	if 'submit'in request.form:
		fe=request.files['f']
		path='static/'+str(uuid.uuid4())+fe.filename
		fe.save(path)
		q="insert into submissions values(null,'%s','%s','%s','pending','pending',curdate())"%(sid,id,path)
		insert(q)
		return redirect (url_for('student.student_view_assignment'))

	return render_template("student_add_submission.html",data=data)


@student.route('/viewsubject',methods=['get','post'])
def viewsubject():
	data={}
	id=session['loginid']
	# q="select * from exercise"
	# res1=select(q)
	# data['a']=res1[0]['exercise_id']
	# asd=data['a']
	# data['b']=res1[0]['subject_id']
	# sbd=data['b']
	
	# data['d']=res1[0]['assignmentt_date']
	# dab=data['d']
	

	q="SELECT  DISTINCT subject_name,`assignment_date`,subject_id FROM exercise  INNER JOIN subjects USING(subject_id) ORDER BY`assignment_date` "
	res=select(q)

	data['viewsubject']=res

	# q1="SELECT * FROM studentssubmissions inner join exercise using(exercise_id) WHERE subject_id='%s' AND assignmentt_date='%s' and student_id=(select student_id from students where login_id='%s') " %(sbd,dab,id)
	
	# ress=select(q1)
	# data['att']=ress
	
	# data['j']=session.get('count1')
	
	# data['k']=session.get('count2')
	
	
		

	


	
	


	
	return render_template("selectsubject.html",data=data)

@student.route('/startexercise',methods=['get','post'])
def startexercise():
	data={}
	data['flag']=0
	data['pflag']=0
	data['qstnid']=1
	if 'numofval' in request.form:
		data['numofval']=request.form['numofval']
	else:
		data['numofval']=0
	# eid=session['sub_id']
	ids=request.args['ids']
	# eid=request.args['id']
	# print("eid=",eid)
	id=session['loginid']
	q="select * from subjects where subject_id='%s'" %(ids)
	res1=select(q)
	data['subjectname']=res1
	data['ansdetails']="0"
	q="select *,concat(first_name,' ',last_name) as names from students where login_id='%s'" %(id)
	res3=select(q)
	data['sdetails']=res3
	data['check']=[{'button':"None"}]
	if 'startexam' in request.form:
		# select questions
		q="select exercise_id from exercise where subject_id='%s'" %(res1[0]['subject_id'])
		res2=select(q)
		# shuffle the questions
		a = [d.get('exercise_id', None) for d in res2]
		numpy.random.shuffle(a)
		
		print(len(a))
		data['numofval']=len(a)
		data['numofvalinc']="1"
		data['position']="0"

		# get question details
		q="select * from exercise where exercise_id='%s'" %(a[0])
		print(q)
		res=select(q)
		data['questions']=res
		# get answer details 
		q="select option_id,`option_description` from exerciseoptions where exercise_id='%s'" %(a[0])
		res=select(q)
		data['answerdetails']=res

		# check whether answered
		q="select * from studentssubmissions where exercise_id='%s' and student_id=(select student_id from students where login_id='%s')" %(a[0],id)
		print(q)
		res5=select(q)
		if res5:
			data['answered']=res5
		else:
			data['answered']=[{"option_id":""}]
		print("Haii",data['answered'])

		str1 = ""  

	# traverse in the string   
		for ele in a:
			if str1=="":
				str1=str(ele)
			else:
				str1 = str1+","+str(ele)
		print("aaaaa"+str1)
		data['a']=str1

		# for button check
		data['check']=[{'button':"Clikked"}]
		data['nextcheck']=[{'button':"NotFinished"}]
		data['previouscheck']=[{'button':"First"}]


		q="SELECT `exercise_id` FROM `studentssubmissions` WHERE student_id=(select student_id from students where login_id='%s') AND `exercise_id` IN (SELECT `exercise_id` FROM `exercise` WHERE subject_id='%s')" %(id,ids)
		res10=select(q)
		data['ansdetails']=res10
		an = [d.get('exercise_id', None) for d in res10]
		str1=""
		for ele in an:
			if str1=="":
				str1=str(ele)
			else:
				str1 = str1+","+str(ele)
		print("aaaaa"+str1)
		data['ansdetails']=str1

	# Next Button
	if 'next' in request.form:

		#for check of question number
		numofval=request.form['numofval']
		data['numofval']=numofval
		qstnid=request.form['qstnid']
		
		# check 
		if numofval==qstnid:
			data['qstnid']=numofval
		else:
			data['qstnid']=int(qstnid)+1
		# get dict value in a
		a=request.form['dict']
		a = list(a.split(","))
		print(a)
		# get position of dict
		position=request.form['dictposition']
		# get flag check
		flag=request.form['flag']
		# get question id
		sid=request.form['sid']

		if 'selanswer' in request.form:
			selanswer=request.form['selanswer']

			#insert
			q="select * from studentssubmissions where exercise_id='%s' and student_id=(select student_id from students where login_id='%s')" %(sid,id)
			res=select(q)
			if res:
				q="update studentssubmissions set answered_option_id='%s' where exercise_id='%s' and student_id=(select student_id from students where login_id='%s')" %(selanswer,sid,id)
				update(q)
			else:
				q="insert into studentssubmissions values(null,(select student_id from students where login_id='%s'),'%s','%s')" %(id,sid,selanswer)
				insert(q)
			

		# increment position
		print("f"+str(position))
		print("n"+str(int(numofval)-1))
		if int(position)==int(numofval)-1:
			position=position
		else:
			position=int(position)+1
		print("l"+str(position))
		# check flag
		# if flag=="1":
		# 	position=0
		# 	data['pflag']=0
		# else:
		# 	data['pflag']=1
		# print(position)
		data['position']=position
		print(position)
		# check whether answered
		q="select * from studentssubmissions where exercise_id='%s' and student_id=(select student_id from students where login_id='%s')" %(a[int(position)],id)
		print(q)
		res5=select(q)
		if res5:
			data['answered']=res5
		else:
			data['answered']=[{"option_id":""}]
		print("Haiissssssss",a[int(position)])
		# get question details
		q="select * from exercise where exercise_id='%s'" %(a[int(position)])
		print(q)
		res=select(q)
		data['questions']=res
		print(res)
		# get answer details 
		q="select option_id,`option_description` from exerciseoptions where exercise_id='%s'" %(a[int(position)])
		res=select(q)
		data['answerdetails']=res
		# for next button check

		data['check']=[{'button':"Clikked"}]
		if int(position)==len(a)-1:
			data['flag']=1
		# for previous button check
		data['previouscheck']=[{'button':"NotFirst"}]
		str1=""
		for ele in a:
			if str1=="":
				str1=str(ele)
			else:
				str1 = str1+","+str(ele)
		print("aaaaa"+str1)
		data['a']=str1

		q="SELECT `exercise_id` FROM `studentssubmissions` WHERE student_id=(select student_id from students where login_id='%s') AND `exercise_id` IN (SELECT `exercise_id` FROM `exercise` WHERE exercise_id='%s')" %(id,ids)
		res10=select(q)
		data['ansdetails']=res10
		an = [d.get('exercise_id', None) for d in res10]
		str1=""
		for ele in an:
			if str1=="":
				str1=str(ele)
			else:
				str1 = str1+","+str(ele)
		print("aaaaa"+str1)
		data['ansdetails']=str1

	

	j=0
	for i in range(1,int(data['numofval'])+1):
		if "selectquestion"+str(i) in request.form:

			#for check of question number
			numofval=request.form['numofval']
			data['numofval']=numofval
			# exerciseid=request.form['exercise_id']
			qstnid=request.form['qstnid']
			# check 
			data['qstnid']=i
			# get dict value in a
			a=request.form['dict']
			a = list(a.split(","))
			print(a)
			# get position of dict
			position=request.form['dictposition']
			# get flag check
			flag=request.form['flag']
			pflag=request.form['pflag']
			# get question id
			sid=request.form['sid']


			# check whether answered
			q="select * from studentssubmissions where exercise_id='%s' and student_id=(select student_id from students where login_id='%s')" %(a[j],id)
			print(q)
			res5=select(q)
			if res5:
				data['answered']=res5
			else:
				data['answered']=[{"option_id":""}]
			print("Haiissssssss",a[j])
			# get question details
			q="select * from exercise where exercise_id='%s'" %(a[j])
			print(q)
			res=select(q)
			data['questions']=res
			print(res)
			# get answer details 
			q="select option_id,`option_description` from exerciseoptions where exercise_id='%s'" %(a[j])
			res=select(q)
			data['answerdetails']=res

			data['position']=j
			# for next button check

			data['check']=[{'button':"Clikked"}]

			str1=""
			for ele in a:
				if str1=="":
					str1=str(ele)
				else:
					str1 = str1+","+str(ele)
			print("aaaaa"+str1)
			data['a']=str1

			q="SELECT `exercise_id` FROM `studentssubmissions` WHERE student_id=(select student_id from students where login_id='%s') AND `exercise_id` IN (SELECT `exercise_id` FROM `exercise` WHERE subject_id='%s')" %(id,ids)
			res10=select(q)
			data['ansdetails']=res10
			an = [d.get('exercise_id', None) for d in res10]
			str1=""
			for ele in an:
				if str1=="":
					str1=str(ele)
				else:
					str1 = str1+","+str(ele)
			print("aaaaa"+str1)
			data['ansdetails']=str1
			break
		j=j+1




	if 'finish' in request.form:
		# q11="SELECT COUNT(exercise_id) FROM exercise WHERE subject_id='%s'"%(ids)
		# res11=select(q11)
		# session['count1']=res11
		
		# q12="SELECT COUNT(exercise_id) FROM studentssubmissions INNER JOIN exercise USING(exercise_id) WHERE subject_id='%s' and student_id=(select student_id from students where login_id='%s')"%(ids,id)
		# res12=select(q12)
		# session['count2']=res12
		

		
		flash('Exam Finished')
		return redirect(url_for('student.viewsubject',data=data))
	return render_template("student_start_exercise.html",data=data)


@student.route('/studentpredictperfomanceofstudent',methods=['get','post'])
def studentpredictperfomanceofstudent():
	data={}
	q = "select * from knowledgeareas"
	res = select(q)
	data['areas']=res
	q="SELECT MAX(mycount) as counts FROM (SELECT COUNT(`knowledge_area_id`) mycount FROM `exerciseknowledges` INNER JOIN `exercise` USING(`exercise_id`) GROUP BY `knowledge_area_id`) temp"
	res=select(q)
	data['count']=res
	print(res)
	return render_template('userpredictperfomanceofstudent .html',data=data)


@student.route('/student_result',methods=['get','post'])
def student_result():
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
		return render_template('student_result.html',data = result)
	else:
		return render_template('userpredictperfomanceofstudent.html',data=data)