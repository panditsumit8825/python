# Problem no.1
# num=int(input("Enter your number :"))
# for i in range(1,11):
#     print(f"table of num is ",i*num)

# Problem no.2
# l1=["Harry","Sohan","Sachin","Rahul"]
# for i in l1:
#     print("Hii ",i +"!")

# Problem no.3
# num=int(input("Enter a number :"))
# i=1
# while(i<11):
#     print("table of num is ",i*num)
#     i=i+1

# Problem no.4
# num= int(input("Enter a number :"))
# if(num<=1):
#     print("number is not prime")
# else:
#     for i in range(2,num):
#         prime=True
#         if(num%i==0):
#             prime=False
#             break
#     if(prime):
#         print("Number is prime")
#     else:
#         print("number is not prime")

# second method by using count function
# n=int(input("Enter a number :"))
# count=0
# for i in range(1,n+1):
#     if(n%i==0):
#         count +=1
# if(count==2):
#     print("number is prime")
# else:
#     print("number is not prime")

# Problem no.5
# n=int(input("Enter a number :"))
# sum=0
# i=1
# while(i<n+1):
#     sum=sum+i
#     i+=1
# print(f"sum of {n} natural number is {sum}")

# Problem no.6
# n=int(input("Enter your number :"))
# fact=1
# if(n==0):
#     print(fact)
# else:
#     for i in range(1,n+1):
#         fact=fact*i
#     print(fact)


# Problem no.7
n=int(input("Enter a number :"))
if(n<=0):
    print("please enter a natural number")
for i in range(1,n+1):
        # star=2*i+1
        # print(" "*(n-i),end="")
        # print("*"*(2*i-1),end="")
        # print("\n")
        print(" "*(n-i),end="")
        print("*"*(2*i-1),end="")
        print("\n")