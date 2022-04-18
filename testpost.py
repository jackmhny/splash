data = {"classPeriod":"C","className":"Essay Writing","teacherName":"Mrs. Buckles","names":["AndrewBoanoh","SaraChiang","CodyGao","TurnerHamilton","EmmaKim","NoahLaubach","JalenLespinasse","JackMahoney","RoryMurphy","AlexNoviello","AlexandraSchmidt","DimitrisStefanidis","IrisWu"]}

url = "http://127.0.0.1:5000"
import requests
r = requests.post(url, json=data)
