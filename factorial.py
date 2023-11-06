#!/usr/bin/env python3
# Created by: Finn Kitor
# Created on: November 6th, 2023
# This program asks the user to enter a positive number and then uses a loop to calculate and display the factorial.
# and it will not accept worded responces.
def main():
    # terminal initializations
    loop_counter = 0
    factorial_answer = 1

    # user will input the number to the terminal
    user_number_as_string = input("Enter a positive number: ")
    print("")
    # terminal will process if the number is valid or not valid from the user.
    try:
        user_number_as_int = int(user_number_as_string)
    except ValueError:
        print("{} is not a number.".format(user_number_as_string))
    else:
        if user_number_as_int > 0:
            # terminal replicates a do..while loop
            # terminal calculates the factorial of the user number using a loop
            while True:
                loop_counter = loop_counter + 1
                factorial_answer = factorial_answer * loop_counter
                print("Tracking {} times through loop.".format(loop_counter))
                if loop_counter >= user_number_as_int:
                    break
            # terminal will display what the number is or if it is not a worded responce.
            print("")
            print("{}! = {}".format(user_number_as_int, factorial_answer))
        elif user_number_as_int == 0:
            print("0! = 1")
        else:
            print("{} is not a positive number.".format(user_number_as_int))
    finally:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
