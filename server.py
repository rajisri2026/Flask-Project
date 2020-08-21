from flask import Flask
import csv

app = Flask(__name__)

#@app.route("/")

@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "GET":
        return redirect(url_for('index'))
    elif request.method == "POST":
        userdata = dict(request.form)
        id = userdata["sid"][0]
        name = userdata["sname"][0]
        gender = userdata["gender"][0]
        dob = userdata["sdob"][0]
        city = userdata["scity"][0]
        state = userdata["sstate"][0]
        email = userdata["smail"][0]
        qualification = userdata["squal"][0]
        stream = userdata["sstream"][0]
        with open('students.csv', mode='a') as csv_file:
            data = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            data.writerow([id,name,gender,dob,city,state,email,qualification,stream])
    return "Thank you!"

if __name__ == "__main__":
  app.run()
