import random
import sys
from msvcrt import getch

#To find given value is high or low than the actual value
def highlow(userguess,answer):
    if(userguess>=answer):
        print("Your guess is higher than Answer")
    else:print("Your guess is smaller than answer")
  
#To find given value is prime or not
def isPrime(n, i = 2):  
    if(n%2==0):
       print('Number is Prime')
    elif (n % i == 0): 
        print('Number is not Prime')
        return isPrime(n, i + 1) 
    else :print(' It is Prime')

#To find given value is odd or even
def oddeven(no):
    if(no % 2 == 0):
        print("The number is even \n")
    else:
        print("The number is odd\n")


def guessbyuser(x):
    ran_number = random.randint(1, x)
    guess = int(0)
    while guess != ran_number
        guess = int(input(f"---Press Zero to quit---\nor\nGuess the number between 1 to {range1}  : "))
        if (guess==0): 
            print("---->>>>Bye<<<<----\n") 
            break
        elif(guess>range1):
            print("guess is out range")
            continue
        elif(guess==ran_number):
            print(f"\n-------->>>>\t{guess}{guess}{guess}\t<<<<--------\nCongrats {guess} is the Correct Value!!!")
            print(f"-------->>>>\t{guess}{guess}{guess}\t<<<<--------\nThank For Your Time")
            q = input('Press any key to exit') #To wait on screen 
            if q:
                print("\n---->>>>Bye<<<<----")
                exit(0)
            else:
                print("\n---->>>>Bye<<<<----")
                exit(0)
        print(ran_number)
        numx=random.randint(2,4)	    
        #if(numx==1):
        	#fib(ran_number)
        if(numx==2):
            print("Hint: ")
            highlow(guess,ran_number)
        elif(numx==3):
            print("Hint: ")
            isPrime(ran_number)
        else:
            print("Hint: ")
            oddeven(ran_number)

# >>>>>>Driver Code<<<<<<
range1 = int(input(f"\n***Welcome To Number Guessing Game***\n Enter Max limit for the number  :"))
if(range1<1):
    sys.exit("Input is Invalid\n---->>>>Bye<<<<----\nTry again with natural number\n")
else:
    guessbyuser(range1)
