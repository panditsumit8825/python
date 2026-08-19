# Quiz 1
# def greet():
#     name=input("Enter your name")
#     print(f"Hii {name}")

# greet()

# Problem no.1
# def greatest(a,b,c):
#     if(a>b and a>c):
#         return a
#     elif(b>c):
#         return b
#     else:
#         return c
# # greatest(7,3,9)
# print(f"The greatest number is : {greatest(7,3,9)}")

# Problem no.2
# celcius=int(input("Enter the celcius :"))
# def farenh(celcius):
#     return (celcius * 9/5) + 32
# print(f"The temp in farenheight is {farenh(celcius)}") 

# Problem no.3
# print("a")
# print("b")
# print("c",end="")
# print("d",end="")

# Problem no.4
# n=int(input("Enter a number :"))
# def sum(n):
#     if(n==1):
#         return 1
#     return n + sum(n-1)
# print(f"The sum of {n} natural number is {sum(n)}")

# Problem no.5
# n=int(input("Enter a number :"))
# def pattern(n):
#     if(n==0):
#         return
#     print("*"*n)
#     pattern(n-1)
# pattern(n)

# Problem no.6
# n=int(input("Enter the inches :"))
# def inc_to_cms(n):
#     return n*(2.54)
# print(f"value of {n} inch to {inc_to_cms(n)} cms")

# Problem no.7
# first part 
# l1=["ramesh","suresh","rajesh"]
# print(l1)
# word=input("Enter the word above the list :")
# def rem(l1):
#     l1.remove(word)
#     return l1
# print(rem(l1))
# second part
# def rem(l1,word):
#     n=[]
#     for item in l1:
#         if not(item==word):
#             n.append(item.strip(word))
#     return n
# l1=["ramesh","juresh","rajesh","kaju","barfi"]
# print(rem(l1,"sh"))

# Problem no.9
# n=int(input("Enter a number :"))
# def mul(n):
#     for i in range(1,11):
#         print(f"{n} x {i} = {n*i}")
# mul(n)
    
