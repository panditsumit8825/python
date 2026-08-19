import random
user=input("Enter your choice Snake,Water,Gun = ").lower()
choice=["snake","water","gun"]
comp=random.choice(choice)
print(f"computer choice = {comp}")
if user not in user:
    print("Invalid choice!")
else:
    print("Computer chose:", comp)
    if(user==comp):
        print("Match is draw!")
    elif(user=="snake" or comp=="water"):
        print("You Win!")
    elif(user=="water" or comp=="gun"):
        print("You Win!")
    elif(user=="gun" or comp=="snake"):
        print("You Win!")
    else:
        print("Computer Win!")