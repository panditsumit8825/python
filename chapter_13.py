# Problem no.1
# problem one is done in terminal 

# Problem no.2
# name = input("Enter your name :")
# marks=int(input("Enter your marks :"))
# phone=int(input("Enter your phone number :"))
# s="The name of the student is {},his marks are {} and phone number is {}".format(name,marks,phone)
# print(s)

# Problem no.3
# table=[str(7*i) for i in range(1,11)]
# s="\n".join(table)
# print(s)

# Problem no.4
# def divisible5(n):
#     if(n%5==0):
#         return True
#     return False
# a =[1,23,456,378415,28916871,5,10,25,78]
# f=list(filter(divisible5,a))
# print(f)

# Problem no.5
# from functools import reduce
# l =[1,23,456,415,871,5,10,25,78]

# def greater(a,b):
#     if(a>b):
#         return a
#     return b
# print(reduce(greater,l))

# Problem no.6
# done in terminal

# Problem no.7
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
app.run()
