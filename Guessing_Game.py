import random
randnumber=random.randint(1,5)
userinput=None
guesses=0
while(userinput != randnumber):
    userinput=int(input("Enter Your Number"))
    guesses += 1
    if userinput==randnumber:
        print("You guessed it right!, Congratulations")
    else:
         if(userinput>randnumber):
             print("You guessed it wrong! Enter a smaller number")
         else:
              print("You guessed it wrong! Enter a larger number")  
print(f"You Guessed the number in {guesses} guesses ")