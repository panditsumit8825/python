# Problem no.1
# try:
#     with open("1.txt" , "r") as f:
#         print(f.read())
# except Exception as e:
#     print(e)

# try:
#     with open("1.txt" , "r") as f:
#         print(f.read())
# except Exception as e:
#     print(e)

# try:
#     with open("1.txt" , "r") as f:
#         print(f.read())
# except Exception as e:
#     print(e)

# print("Thank You!")

# Problem no.2
# l=[1,2,3,4,5,6,7,8,9]
# for i,item in enumerate(l):
#     if(i==2 or i==4 or i==6):
#         print(i)

# Problem no.3
# n=int(input("Enter a number"))
# table=[n*i for i in range(1,11)]
# # print(f"table of 5 is {n}x{i} = {table}")
# print(f"table of {n} is = {table}")

# Problem no.4
# try:
#     a=int(input("Enter a:"))
#     b=int(input("Enter b:"))
#     print(a/b)
# except ZeroDivisionError as e:
#     print("Infinte")

# Problem no.5
n=int(input("Enter a number :"))
table=[n*i for i in range(1,11)]
# print(f"table of {n} is = {table}")
# print(table)
with open("tables.txt","a") as f:
    f.write(f"Table of {str(table)} \n")