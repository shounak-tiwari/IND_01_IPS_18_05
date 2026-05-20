# WAP for calculate sum of first and last digit of  5 digiy number.. 
import math
Number = int(input("Enter the five digit number : "))
LastDigit = Number%10
lenofnum = 10**math.floor(math.log10(Number))
FirstDigit = Number //lenofnum
print("First digit  : ",FirstDigit)
print("Last digit : ",LastDigit)