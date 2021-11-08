from random import randint
import sys
    
def game():    
    random_number=20
    n=randint(0,random_number)



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
            if 10 >= n >= 0 :
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
                prompt()


            elif guess<n:
                print("Your guess is too small. YOU FAIL! GAME OVER")
                print("N = ", n, ".")
                guess_counter+=1
                prompt()




    if guess==n:
        print("Your guess is correct! You guessed in ", guess_counter, " tries.")
        prompt()

       
    
def prompt():
    init=int(input("Type 1 and press enter to play, type 2 and press enter to exit."))
    if init==1:
        game()

    if init==2:
        sys.exit



prompt()

#guess counter
#score
#limited guesses
#lives that result in better hint (#is between this range, odds+evens)
