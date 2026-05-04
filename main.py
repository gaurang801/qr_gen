import random

n=random.randint(1,100)
a =-1

guess =0
while(a!=n):
    guess+=1
    a = int(input("enter the NUmber :"))
    if(a<n):
        print("enter the higher number")
    
    elif(a>n):
        print("enter the lower number")

print(f"you guessed the correct number {n} in {guess} Rounds")