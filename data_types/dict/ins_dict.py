my_dict = {'name': 'mike', 'age': 26}
print(my_dict)
# update value
my_dict['age'] = 27
# add item
my_dict['address'] = 'SFO'
print(my_dict)
#================================================
mydict = {'a': 'hello', 'b': 'world'}
for x in mydict:
    val = mydict[x]
    mydict[x] = val.upper()
    print('Changed what', x, 'points to: from', val, 'to', mydict[x])

#================================saving student details=======================
Mike = {
    "name": "Mike",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
Max = {
    "name": "Max",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
Jhon = {
    "name": "Jhon",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

students = [Mike,Max,Jhon]
print(students[0])
print(students[0]["name"])
# for student in students:
#     print(student["name"])
#     print(student["homework"])
#     print(student["quizzes"])
#     print(student["tests"])

#===================================================
# If you use Instagram's API to fetch data about Snoop Dogg's account, the API will return a text file (in JSON format) that can be turned into a Python dictionary:
{
    "data": {
        "id": "1574083",
        "username": "snoopdogg",
        "full_name": "Snoop Dogg",
        "profile_picture": "http://distillery.s3.amazonaws.com/profiles/profile_1574083_75sq_1295469061.jpg",
        "bio": "This is my bio",
        "website": "http://snoopdogg.com",
        "counts": {
            "media": 1320,
            "follows": 420,
            "followed_by": 3410
        }
}
#============================================
datathing = {
      "data": {
          "id": "1574083",
          "username": "snoopdogg",
          "full_name": "Snoop Dogg",
          "profile_picture": "http://distillery.s3.amazonaws.com/profiles/profile_1574083_75sq_1295469061.jpg",
          "bio": "This is my bio",
          "website": "http://snoopdogg.com",
          "counts": {
              "media": 1320,
              "follows": 420,
              "followed_by": 3410
          }
  }
}
#===========================
user = datathing['data']
print("User name:", user['full_name'])
print("Bio:", user['bio'])
counts = user['counts']
print("Number of posts:", counts['media'])
print("Number of users followed:", counts['follows'])
