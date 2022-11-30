from flask import Flask 
from public import public
from admin import admin
from faculty import faculty
from student import student
from api import api



app=Flask(__name__)
app.secret_key="s"
app.register_blueprint(public)
app.register_blueprint(admin)
app.register_blueprint(faculty)
app.register_blueprint(student)
app.register_blueprint(api,url_prefix="/api")
app.run(debug=True,port=5010,host="0.0.0.0")