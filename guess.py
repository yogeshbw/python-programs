import random
import sys

def highlow(userguess,answer):
    if(userguess>=answer):
        print("Your guess is higher than Answer")
    else:print("Your guess is smaller than answer")



def isPrime(n, i = 2): 
   
  
    # Base cases 
    if(n%2==0):
       print('Number is Prime')
    elif (n % i == 0): 
        print('Number is not Prime')
        return isPrime(n, i + 1) 
    else :print(' It is Prime')


def oddeven(no):
    if(no % 2 == 0):
        print("The number is even \n")
    else:
        print("The number is odd\n")


def guessbyuser(x):

    ran_number = random.randint(1, x)
    
    guess = int(0)

    while guess != ran_number :
    
        #sys.exit("Input is not natural number")
        guess = int(input(f"Press Zero to quit\n\tor\nGuess the number between 1 to {range1}  : "))
        
        if (guess==0): 
            print("---->>>>Bye<<<<----\n") 
            break
        elif(guess>range1):
            print("guess is out range")
            continue
        elif(guess==ran_number):
           print("Congrats you have Got it \n Thank For Your Time \n *****Bye*****\n\n ")
           break
        #print(ran_number)
        numx=random.randint(2,4)
        #if(numx==1):
        #  undefinedfunction(guess,ran_number)
        if(numx==2):
            highlow(guess,ran_number)
        elif(numx==3):
            isPrime(ran_number)
        else:
            oddeven(ran_number)

# >>>>>>Driver Code<<<<<<
range1 = int(
        input(f"\n***Welcome To Number Guessing Game***\n Enter Max limit for the number  :"))
if(range1<1):
   
    sys.exit("Input is Invalid\n---->>>>Bye<<<<----\nTry again with natural number\n")
else:
        guessbyuser(range1)