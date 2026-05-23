# if control statement 
# write a program to check name is valid or not name is taken from the and make sure the len of name is not > 8 and not < 2 
# and  the first latter is vapital and rest is small 

Name = "akash"

if ord(Name[0])>=65 and  ord(Name[0])<=90 and (2<=len(Name)<=8):
    print("Name is valid ")
else:
    print("Name is not valid")