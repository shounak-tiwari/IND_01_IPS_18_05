#Statement control the flow of execution of program based on some conditions 
# a. if
# b. if else 
# c. if elif else
# d. nested if 
# e. nested if else 
# f. match case (3.9+ version) 
# g. looping

# Data of 1000 student find out how many students have 90+ marks in mathematics , 86+ marks in chem , and 90+ marks in physics 

# (>, <, >=, <=, ==, != )

mathematics  = 91
chem = 90
physic = 93 
count = 0
if (mathematics> 90):
    if (chem > 86):
        if(physic >90):
            count +=1

print(count)