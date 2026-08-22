# Problem no.1
# class programmer:
#     company="Microsoft"
#     def __init__(self,name,salary,id):
#         self.name=name
#         self.salary=salary
#         self.id=id
# p=programmer("Harry",2000000,205)
# print(p.company,p.id,p.name,p.salary)


# Problem no.2
# class calculater:
#     def __init__(self,n):
#         self.n=n
#     def square(self):
#         print(f"The square is {self.n*self.n}")
#     def cube(self):
#         print(f"The cube is {self.n*self.n*self.n}")
#     def squareroot(self):
#         print(f"The square root is {self.n**1/2}")
# a=calculater(4)
# a.square()
# a.cube()
# a.squareroot()

# Problem no.3
# class demo:
#     a=4
# o=demo()
# print(o.a) #prints class attributes bcz instance attributes are not present
# o.a=0 #instance attributes are set
# print(o.a) #prints instance attributes bcz intance attributes are present
# print(demo.a) #prints the class attributes

# problem no.4
# class calculater:
#     def __init__(self,n):
#         self.n=n
#     def square(self):
#         print(f"The square is {self.n*self.n}")
#     def cube(self):
#         print(f"The cube is {self.n*self.n*self.n}")
#     def squareroot(self):
#         print(f"The square root is {self.n**1/2}")
#     @staticmethod
#     def hello():
#         print("Hello there !")

# a=calculater(4)
# a.square()
# a.cube()
# a.squareroot()
# a.hello()

# problem no.5

from random import randint
class train:
    def book(self,trainNo,fro,to):
        print(f"Your ticked is in train no{trainNo} from {fro} to {to}")
    def getstatus(self,trainNo):
        print(f"train no {trainNo} is running on time")
    def getfare(self,trainNo,fro,to):
        print(f"Your ticket fare from {fro} to {to} is {randint(150,790)}")