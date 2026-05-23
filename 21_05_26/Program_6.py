# nested if else
'''
JEE 
age>=17 and age <=24 
branch == "pcsm||pcmb||pcm"
'''
age = int(input("Enter the age of candidate : "))

if 17<age<24:
    branch = input("Enter the branch (pcm||pcb || other) : ")
    if branch == "pcm" or branch == "pcb":
        print("Candidate is eligible for jee")
    else:
        print("Sorry you're branch is not matched")
else:
    print("Your age is not matched")
    