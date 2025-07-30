import random

def guess(randNo,i):
    num = int(input("Guess The Number: "))
    if((num<1) or (num>100)):
        print("\nNumber Should be in the range of 1-100")
    
    if(num==randNo):
        print("CONGRATULATION!!!! \n YOU GUESS THE NUMBER IN YOUR",i,"ATTEMPT")
    elif(num>randNO):
         print("Your Number is Bigger Than the Original Number")
         guess(randNO,i+1)
    else:
         print("Your Number is Smaller Than the Original Number")
         guess(randNO,i+1)



print("-----GUESS THE NUMBER-----\n")
print("NOTE - Computer Has Choose a Number Between 1-100 You Need to Guess That Number\n")
randNO = random.randint(1,100)
i=1
guess(randNO,i)

