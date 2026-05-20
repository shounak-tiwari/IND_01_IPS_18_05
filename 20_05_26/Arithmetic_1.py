# Mean calculate from the data set  
# Mode calculate from the data set  
# Median calculate from the data set
'''
1. mysql
2. json 
3. csv 
4. excel
5. input function 
6. nosql (mongodb)
+ ,- , *, /, %, //, **  
'''
# enter five subject marks and calculate average 
'''
Avg = (Sum of observation) / (Total number of observation)
'''
# Algo:
# step 1 :  Declare and take the input of 5 subject marks 
Sub1 = float(input("Enter the marks of subject 1 :"))
Sub2 = float(input("Enter the marks of subject 2 : "))
Sub3 = float(input("Enter the marks of subject 3 : "))
Sub4 = float(input("Enter the marks of subject 4 : "))
Sub5 = float(input("Enter the marks of subject 5 : ")) 
# use formula 
Avg = (Sub1+Sub2+Sub3+Sub4+Sub5)/5
# print
print("Average : ",Avg)