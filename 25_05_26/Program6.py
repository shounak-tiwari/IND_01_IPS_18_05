# String : string is an ordered sequence collection of char which store data inside the single double and multiple quotes  

# write a program to count the vowel in entred string and print it.. 

s1 = str(input("Enter the string : ")).lower()
lst = ['a','i','o','e','u']
vCtr = 0 
for x in s1:
    if x in lst:
        vCtr+=1
print("Total Vowels in string  : ",vCtr)