import json
from flask import Flask
from flask import request
from flask import g

app = Flask(__name__)

data = {}

data["E Voss"] = ["ThomasAtkinson","DhruvKhurjekar","JacobLee","JackMahoney","RadnaaMunkh-orgil","AndrewNoviello","KylePark","MariaSanmartin","GrantShueh","YanTsenter","SabrinaYeung"]
data["F Wilcox"] = ["JackMahoney","AlexNoviello","RiaPatel","SummerQureshi","MariaSanmartin","YanTsenter","TristanWan"]


@app.route("/", methods = ['GET', 'POST', 'DELETE'])
def main():
    if request.method == 'GET':
        students = []
        for c in data:
            for student in data[c]:
                if student not in students:
                    students.append(student)
        students.sort()
        students_links = []
        for student in students:
            students_links.append(f"<a href='./{student}'>{student}<a/>")
        return " | ".join(students_links)
        
    if request.method == 'POST':
        """modify/update the information for <user_id>"""
        # you can use <user_id>, which is a str but could
        # changed to be int or whatever you want, along
        # with your lxml knowledge to make the required
        # changes
        post = request.json # a multidict containing POST data
        # data_dumped = json.dumps(data)
        # with open("log.json", "w") as f:
        #     f.write(data_dumped)
        # print("SUCCESSFUL POST: " + data_dumped)
        teacher_name = post["teacherName"]
        class_name = post["className"]
        stu_names = post["names"]
        period = post["classPeriod"]
        class_info = period + " " + teacher_name
        data[class_info] = stu_names
        print("added " + class_info)
        return "added " + class_info
@app.route("/<student_name>")
def find(student_name):
    classes = []
    for key in data:
        if student_name in data[key]:
            classes.append(key)
    return " | ".join(sorted(classes))
            

