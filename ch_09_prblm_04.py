word="Donkey"
with open("newfile.txt" , "r") as f:
    content=f.read()
    contentnew=content.replace(word,"######")
with open("newfile.txt","w") as f:
    f.write(contentnew)
