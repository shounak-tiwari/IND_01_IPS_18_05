#regular expression
# akashtiwari1014@gmail
# dob
# email 
import re
namere = r"^[A-Za-z0-9]+@[a-z]{2,}$"
name = "Aka1014@gmail"
if re.match(namere,name):
    print("Valid")
else:
    print("Invalid")
