import json
from flask import Flask
from flask import request
from flask import g

app = Flask(__name__)

students = {}

@app.route("/", methods = ['GET', 'POST', 'DELETE'])
def main():
    
    if request.method == 'POST':
        """modify/update the information for <user_id>"""
        # you can use <user_id>, which is a str but could
        # changed to be int or whatever you want, along
        # with your lxml knowledge to make the required
        # changes
        data = request.json # a multidict containing POST data
        data_dumped = json.dumps(data)
        with open("log.json", "w") as f:
            f.write(data_dumped)
        print("SUCCESSFUL POST: " + data_dumped)
        teacher_name = data["teacherName"]
        class_name = data["className"]
        stu_names = data["names"]
        period = data["classPeriod"]
        class_info = period + " " + teacher_name
        students[class_info] = stu_names
    if request.method == 'DELETE':
        """delete user with ID <user_id>"""
