import random
randnumber=random.randint(1,50)
print(randnumber)
userinput=None
guesses=0
while(userinput != randnumber):
    userinput=int(input("Enter Your Number"))
    guesses += 1
    if userinput==randnumber:
        print("You guessed it right!, Congratulations")
print(f"You Guessed the number in {guesses} guesses ")