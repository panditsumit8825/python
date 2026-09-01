# def recur(n):
#     if(n>0):
#         return n + recur(n-1)
#     else:
#         return 0
#     # print(sum)
# res=recur(10)
# print(res)

# Practice day -28/08/2026

# Renamin function
# def display_student(name,age):
#     print(name,age)
# show_student=display_student
# display_student("Harry",35)
# show_student("Harry",27)

# using of the range()
# print(list(range(4,30,2)))

# largest element in list
# x = [4, 6, 8, 24, 12, 2]
# lagest=max(x)
# print(lagest)

# functing using key or positional argument
# str1=input("Enter animal type :")
# str2=input("Enter animal name :")
# def describe_pet(animal_type,animal_name):
#     print(animal_type,animal_name)
# describe_pet("hamster","Harry")
# describe_pet(str1,str2)

# uses of**kwargs
# def print_info(**kwargs):
#     print(kwargs)
# print_info(name="Alice",age=30,city="New York")

# def find_number(arr,k):
#     for i in arr:
#         if(i==k):
#             return "Yes"
#     return "No"
# num=[1,2,5,8,3,6,9]
# print(find_number(num,3))

# def find_num(arr, k):
#     if k in arr:
#         print("Yes")
#     else:
#         print("No")

# num = [3, 6, 1, 8, 9, 7, 2]
# find_num(num, 9)

# print(count_evens([2, 1, 2, 3, 4]))  # Expected output: 3
# print(count_evens([2, 2, 0]))        # Expected output: 3
# print(count_evens([1, 3, 5])) 
# colors = {"red", "green", "blue"}
# print("Before clear:", colors)

# colors.clear()
# print("After clear:", colors)   

# animals = {"cat", "dog", "bird", "fish"}

# count = 0
# for _ in animals:
#     count += 1

# print("Length of set:", count)

# animals = {"cat", "dog", "bird", "fish"}

# count = 0
# for _ in animals:
#     count += 1

# print("Length of set:", count)

set_a = {1, 2, 3, 4}
set_b = {3, 9, 8, 6}

sum = set_a.intersection(set_b)
print("Intersection:", sum)
