from random import randint
import sys
random_number=10
n=randint(0,random_number)
print(n)

guess=int(input("You have three guesses. Enter your first guess for the random number:"))
print("Your first guess is: ", guess, ".")

guess_counter=1

if guess==n:
    print("Wow! You guessed correctly on your first try!")

while (guess!=n):
    if guess_counter<3:
        if guess>n:
            print("You've guessed ", guess_counter, " times.")
            print("Your guess is too large.")
            guess=int(input("Enter your next guess:"))
            print("You guessed ", guess, ".")
            guess_counter+=1
        elif guess<n:
            print("You've guessed ", guess_counter, " times.")
            print("Your guess is too small.")
            guess=int(input("Enter your next guess:"))
            print("You guessed ", guess, ".")
            guess_counter+=1
        else:
            print("This statement should never be printed. Something is wrong.")

    elif guess_counter==3:
        print("You've guessed ", guess_counter, " times.")
        if n > 10:
                print("HINT: N is between 11 and 20")
        if n >= 0 < 11:
                print("HINT: N is between 1 and 10")
        if guess>n:
            print("Your guess is too large.")
            guess=int(input("Enter your next guess:"))
            print("You guessed ", guess, ".")
            guess_counter+=1
            
        elif guess<n:
            print("Your guess is too small.")
            guess=int(input("Enter your next guess:"))
            print("You guessed ", guess, ".")
            guess_counter+=1

    elif guess_counter==4:
        print("You've guessed ", guess_counter, " times.")
        if 20 >= n >= 16:
                print("HINT: N is between 20 and 16.")
        if 15 >= n >= 11:
                print("HINT: N is between 15 and 11.")
        if 10 >= n >= 6:
                print("HINT: N is between 10 and 6.")
        if 5 >= n >= 0:
                print("HINT: N is between 5 and 0.")

        if guess>n:
            print("Your guess is too large.")
            guess=int(input("Enter your next guess:"))
            print("You guessed ", guess, ".")
            guess_counter+=1
            
        elif guess<n:
            print("Your guess is too small.")
            guess=int(input("Enter your next guess:"))
            print("You guessed ", guess, ".")
            guess_counter+=1   



    elif guess_counter==5:
        print("You've guessed ", guess_counter, " times.")
        

        if guess>n:
            print("Your guess is too large. YOU FAIL!")
            print("N = ", n, ".")
            guess_counter+=1
            sys.exit("Game over...")

        elif guess<n:
            print("Your guess is too small. YOU FAIL! GAME OVER")
            print("N = ", n, ".")
            guess_counter+=1
            sys.exit("Game over...")



if guess==n:
    print("Your guess is correct! You guessed in ", guess_counter, " tries.")
    sys.exit("Come back soon...goodbye.")





#guess counter
#score
#limited guesses
#lives that result in better hint (#is between this range, odds+evens)
