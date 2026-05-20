# WAP to calculate the largest digit of number  
Number = 19683
largest = (Number%10)
nextNum =  (Number//10)
nextCheck = nextNum%10
largest =  largest if (largest>nextCheck) else nextCheck

nextNum =  (nextNum//10)
nextCheck = nextNum%10
largest =  largest if (largest>nextCheck) else nextCheck

nextNum =  (nextNum//10)
nextCheck = nextNum%10
largest =  largest if (largest>nextCheck) else nextCheck

nextNum =  (nextNum//10)
nextCheck = nextNum%10
largest =  largest if (largest>nextCheck) else nextCheck

print("Largest digit of number  : ",largest)