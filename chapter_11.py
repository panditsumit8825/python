# Problem no.1
# class twoDvector:
#     def __init__(self,i,j):
#         self.i=i
#         self.j=j

#     def show(self):
#         print(f"The vector is {self.i}i + {self.j}j ")

# class threeDvector(twoDvector):
#     def __init__(self,i,j,k):
#         super().__init__(i,j)
#         self.k=k
#     def show(self):
#         print(f"The vector is {self.i}i + {self.j}j + {self.k}k")
# a=twoDvector(1,2)
# a.show()
# b=threeDvector(1,2,3)
# b.show()

# Problem no.2
# class Animals:
#     pass

# class Pets(Animals):
#     pass

# class Dog(Pets):
#     @staticmethod
#     def bark():
#         print("Boww Boww !")
# d = Dog()
# d.bark()

# Problem no.2
# class Employee:
#     salary=540
#     increment=20
#     @property
#     def salaryafterIncrement(self):
#         return (self.salary + self.salary * (self.increment/100))
#     @salaryafterIncrement.setter
#     def salaryafterIncrement(self,salary):
#         self.increment = ((salary/self.salary)-1)*100
# e =Employee()
# # print(e.salaryafterIncrement)
# e.salaryafterIncrement=1000
# print(e.increment)

# Problem no.4
# class complex:
#     def __init__(self,r,i):
#         self.i=i
#         self.r=r

#     def __add__(self,c2):
#         return complex(self.r + c2.r,self.i + c2.i)
#     def __str__(self):
#         return(f"{self.r} + {self.i}i")

# c1=complex(2,3)
# c2=complex(4,5)
# print(c1 + c2)

# Problem no.5
# class vector:
#     def __init__(self,x,y,z):
#         self.x=x
#         self.y=y
#         self.z=z
#     def __add__(self, other):
#         result=vector(self.x+other.x,self.y+other.y,self.z+other.z)
#         return result

#     def __mul__(self, other):
#             result=self.x*other.x+self.y*other.y+self.z*other.z
#             return result

#     def __str__(self):
#         return f"vector({self.x},{self.y},{self.z})"

# v1=vector(1,2,3)
# v2=vector(4,5,6)
# v3=vector(7,8,9)

# print(v1+v2)
# print(v1*v2)

# print(v1+v3)
# print(v1*v3)

# Problem no.6
# class vector:
#     def __init__(self,x,y,z):
#         self.x=x
#         self.y=y
#         self.z=z
#     def __add__(self, other):
#         result=vector(self.x+other.x,self.y+other.y,self.z+other.z)
#         return result

#     def __mul__(self, other):
#             result=self.x*other.x+self.y*other.y+self.z*other.z
#             return result

#     def __str__(self):
#         return f"({self.x}i+{self.y}j+{self.z}k)"

# v1=vector(1,2,3)
# v2=vector(4,5,6)
# v3=vector(7,8,9)

# print(v1+v2)
# print(v1*v2)

# print(v1+v3)
# print(v1*v3)

# Problem no.7
class vector:
    def __init__(self,l):
        self.l=l

    def __len__(self):
        return len(self.l)
v1=vector([1,2,3])
print(len(v1))