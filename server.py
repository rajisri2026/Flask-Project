from flask import Flask,render_template,request,flash,redirect, url_for
from wtforms import Form, BooleanField, StringField, PasswordField, validators
import csv

app = Flask(__name__)

@app.route('/')#route for the homepage
def index():#any name can be given to this function
    return render_template('home.html')

@app.route('/addStudent')
def addStudent():
    return render_template('add-student.html')

@app.route('/searchStudent')
def searchStudent():
    return render_template('search-student.html')

@app.route('/searchById', methods=["GET", "POST"])
def searchById():
    if request.method == "POST":
        first_line = True
        students= []
        id = request.form["id"]
        with open('data/students.csv') as csv_file:
            data = csv.reader(csv_file, delimiter=',')
            for row in data:
                if not first_line:
                    if row:
                        if row[0] == id:
                            students.append(row)
                            return render_template('search-result.html',students = students)
                else:
                    first_line = False
            return redirect(url_for('searchStudent'))

@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        userdata = dict(request.form)
        id = userdata["sid"]
        name = userdata["sname"]
        gender = userdata["gender"]
        dob = userdata["sdob"]
        city = userdata["scity"]
        state = userdata["sstate"]
        email = userdata["smail"]
        qualification = userdata["squal"]
        stream = userdata["sstream"]
        if len(name) < 3 and len(email) < 10 and len(id) < 1 :
            return "Please submit valid data."
        with open('data/students.csv', mode='a') as csv_file:
            data = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            data.writerow([id,name,gender,dob,city,state,email,qualification,stream])
    return redirect(url_for('index'))

@app.route('/showStudentDetails')
def showStudentDetails():
    with open('data/students.csv') as csv_file:
        data = csv.reader(csv_file, delimiter=',',quotechar='"')
        first_line = True
        students= []
        for row in data:
            if not first_line:
                students.append(row)
            else:
                first_line = False
    return render_template("show-students-details.html",students=students)


if __name__ == '__main__':
    app.debug = True
    app.run()
