
from time import sleep
from flask import *
from database import *
import uuid

api=Blueprint('api',__name__)

@api.route('/login')
def login():
    data={}
    un=request.args['username']
    pwd=request.args['password']
    print(un,pwd)
    z="select * from `login` where user_name='%s' and password='%s' "%(un,pwd)
    res=select(z)

    if res:
        data['status']='success'
        data['data']=res
    else:
        data['status']='failed'
    return str(data)

@api.route('/viewsubjects')
def viewsubjects():
    data={}
    # logid=request.args['log_id']
    q="select * from subjects inner join courses using (course_id)"

    res=select(q) 
    if res:
        data['status']='success'
        data['data']=res
    return str(data)

@api.route('/viewfaculties')
def viewfaculties():
    data={}
    # logid=request.args['log_id']
    q="select * from faculty"

    res=select(q) 
    if res:
        data['status']='success'
        data['data']=res
    return str(data)

@api.route('/viewnotes')
def viewnotes():
    data={}
    # logid=request.args['log_id']
    q="SELECT * FROM notes INNER JOIN faculty USING (faculty_id) INNER JOIN courses USING (course_id) "

    res=select(q) 
    if res:
        data['status']='success'
        data['data']=res
    return str(data)

@api.route("/managedoubts")
def managedoubts():
    data={}
    doubt=request.args['doubt']
    lid=request.args['log_id']
    noteid=request.args['note_id']

    q="insert into doubts values(null,(select student_id from students where login_id='%s'),'%s','%s','pending',curdate())"%(lid,noteid,doubt)
    rs=insert(q)
    if rs:
        data['method']='managedoubts'
        data['status']='success'
    return str(data)

@api.route('/viewdoubts')
def viewdoubts():
    data={}
    # logid=request.args['log_id']
    lid=request.args['log_id']
    noteid=request.args['note_id']
    q="SELECT * FROM doubts where student_id=(select student_id from students where login_id='%s') and note_id='%s' "%(lid,noteid)
    print(q)
    res=select(q) 
    if res:
        data['method']='viewdoubts'
        data['status']='success'
        data['data']=res
    return str(data)

@api.route('/viesassignments')
def viesassignments():
    data={}

    q="SELECT * FROM assignments inner join faculty using (faculty_id) inner join courses using (course_id) "
    print(q)
    res=select(q) 
    if res:
        # data['method']='viesassignments'
        data['status']='success'
        data['data']=res
    return str(data)


@api.route('/vewassignmarks')
def vewassignmarks():
    data={}
    logid=request.args['log_id']
    assignid=request.args['assignid']

    q="SELECT * FROM submissions inner join assignments using (assignment_id) where student_id=(select student_id from students where login_id='%s') and assignment_id='%s' "%(logid,assignid)

    print(q)
    res=select(q) 
    if res:
        # data['method']='viesassignments'
        data['status']='success'
        data['data']=res
    return str(data)


@api.route('/viewquiz')
def viewquiz():
    data={}
    # logid=request.args['log_id']
    q="select * from subjects inner join courses using (course_id)"

    res=select(q) 
    if res:
        data['status']='success'
        data['data']=res
    return str(data)


# @api.route('/startexam')
# def startexam():
#     data={}
#     sub_id=request.args['sub_id']
#     q="select * from exercise inner join exerciseoptions on exercise.correct_option_id = exerciseoptions.exercise_id where subject_id='%s' "%(sub_id)

#     res=select(q) 
#     eid=res[0]['exercise_id']

#     q="select count(exercise_id) as count from exerciseoptions where exercise_id='%s' "%(eid)
#     cval = select(q)

#     q="select option_description as opt from exerciseoptions where exercise_id='%s' "%(eid)
#     mainvalue = select(q)
    
    

#     # print(res)
#     if res:
#         data['status']='success'
#         data['data']=res[0]['exercise_question']
#         data['radio'] = cval[0]['count']
#         data['mval'] = mainvalue
#         # qstn=res['exercise_question']
#         # data['qstn']=qstn
#         print(data['data'])
#     else:
#         data['status']='failed'
#         data['data']="no questions"

#     # if res:
#     #     data['status']='success'
#     #     data['data']=res
#     return str(data)


@api.route('/addassignmentspost',methods=['get','post'])
def addassignmentspost():
    data={}
    assign_id=request.form['assign_id']
    log_id=request.form['log_id']
    img=request.files['image']
    image="static/assets/img/"+str(uuid.uuid4())+img.filename
    img.save(image)

    q="insert into submissions values(null,(select student_id from students where login_id='%s'),'%s','%s','pending','pending',curdate())"%(log_id,assign_id,image)
    res=insert(q)
    if res:
        data['status']='success'

    return str(data)

@api.route('/user_view_qstn')
def user_view_qstn():
    data={}
    sub_id=request.args['sub_id']
    log_id=request.args['log_id']
    q="SELECT * FROM `exercise` WHERE `exercise_id`  NOT IN(SELECT `exercise_id` FROM `studentssubmissions` WHERE `student_id`=(SELECT `student_id` FROM `students` WHERE `login_id`='%s')) AND `subject_id`='%s'"%(log_id,sub_id)
    # print(q)
    res=select(q)
    # print(res)

    if res:
       
        data['data']=res
        data['status']='success'
    else:
        data['status']='Already Attend'
    
    data['method']='user_view_qstn'

    return str(data)

@api.route('/user_view_options')
def user_view_options():
    data={}
    sub_id=request.args['sub_id']
    log_id=request.args['log_id']
    qust_id=request.args['q_id']
    q="SELECT * FROM `exercise` INNER JOIN `exerciseoptions` on `exercise`.`correct_option_id`=`exerciseoptions`.`exercise_id`  WHERE exerciseoptions.`exercise_id`  NOT IN(SELECT `exercise_id` FROM `studentssubmissions` WHERE `student_id`=(SELECT `student_id` FROM `students` WHERE `login_id`='%s')) AND `subject_id`='%s'"%(log_id,sub_id)
    res=select(q)
    # print(res)
    if res:
        q='select * from exercise where exercise_id="%s"'%(qust_id)
        val=select(q)

        if val:
            data['status']='success'
            data['data1']=val

            q1="select * from exerciseoptions where exercise_id='%s' "%(qust_id)
            v=select(q1)
            data['data2'] = v
        else:
            data['status']='failed'
    else:
        data['status']='Already Attend'
    data['method']='user_view_options'


    return str(data)

@api.route('/user_answer')
def user_answer():
    data={}
    val=request.args['val']
    ans_id=request.args['ans_id']
    mark=request.args['mark']
    lid=request.args['log_id']
    q_id=request.args['q_id']
    
    q="insert into studentssubmissions values(null,(SELECT `student_id` FROM `students` WHERE `login_id`='%s'),'%s','%s','%s')"%(lid,q_id,ans_id,mark)
    insert(q)
    data['status']='success'
    data['method']='user_answer'
    return str(data)

@api.route('/user_view_result')
def user_view_result():
    data={}
    lid=request.args['log_id']
    sub_id=request.args['sub_id'] 

    q="select *,SUM('mark') from studentssubmissions inner join exercise using (exercise_id) where subject_id='%s' and student_id=(SELECT `student_id` FROM `students` WHERE `login_id`='%s')"%(sub_id,lid)
    res=select(q)
    # print(res)
    if res:
        data['mark'] = res[0]['mark']
        data['status']='success' 
    else:
        data['status']='failed' 
    
    data['method']='user_view_result'

    
    return str(data)