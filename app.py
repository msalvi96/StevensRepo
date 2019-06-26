import os
from TheLionKing import University
from flask import Flask, render_template

Stevens = University(r'C:\Users\mruna\Desktop\StevensRepo', web=True, pt=False)

app = Flask(__name__)

@app.route('/')
def intro():
    return render_template('index.html', title="Stevens Repository", table_title="Stevens Repository")

@app.route('/students')
def student_courses():
    return render_template('students.html', title="Stevens Repository", table_title="Student Summary", data=Stevens.student_data)

@app.route('/instructors')
def instructor_courses():
    return render_template('instructors.html', title="Stevens Repository", table_title="Professor Summary", data=Stevens.instructor_data)

app.run(debug=False)
