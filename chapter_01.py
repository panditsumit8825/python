# print("Hello, World!")

# Problem no.1
# print("Twinkle, twinkle, little star, \n" 
# "How I wonder what you are!\n" 
# "Up above the world so high,\n" 
# "Like a diamond in the sky.")

# Problem no. 3
# import pyttsx3
# engine = pyttsx3.init()
# engine.say("I will speak this text")
# engine.runAndWait()

# Problem no. 4 and 5
import os

# Specify the directry you want to list
directry_path = '/'
#  List all files and directories in the specified path
contents = os.listdir(directry_path)
# Print each file and directry name 
for item in contents:
    print(item)