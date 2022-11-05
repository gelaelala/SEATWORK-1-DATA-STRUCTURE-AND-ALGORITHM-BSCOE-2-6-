#   Seatwork 1
#   Write a python program that do the following:
#   - display the initial content of the array
#   - display a menu of options
#   - allow user to select item in the menu (check if valid)
#   - perform the selected option (you may prompt additional info to user when need)
#   - display the resulting values of the array

# imported modules for colored texts, timer for when the next text will appear, and for the program to exit once the user ended the program
import colored
from colored import stylize
import sys
import time

# program intro
def intro ():
    print ("Welcome to Array Modifier!")
    time.sleep (1)
    print ("Here, you'll be given an initial array with a total of 10 elements and you can modify it however you want.")
    time.sleep (1)
    print ("All you have to do is choose the option that you want from the menu and the program will do it for you.")
    time.sleep (1)
    print ("That's all and here's your array!")

# displaying the initial array and asking for user's input for what they want to do with the given array
def randomnum ():
    initial_array = [92, 45, 27, 53, 77, 22, 77, 14, 50, 70]
    print (stylize(f"Here's your initial array: {initial_array}", colored.fg ('medium_purple_2a')))
    time.sleep (1)
    print ("Here's your menu of the options that you want to do with the given array:")
    time.sleep (2)
    print (stylize ("1 --> Add an element on the array", colored.fg ('medium_purple')))
    time.sleep (1)
    print (stylize("2 --> Insert an element on the array (by index)", colored.fg ('medium_purple')))
    time.sleep (1)
    print (stylize("3 --> Modify an element on the array", colored.fg ('medium_purple')))
    time.sleep (1)
    print (stylize("4 --> Delete an element on the array (by index)", colored.fg ('medium_purple')))
    time.sleep (1)
    print (stylize("5 --> Delete an element on the array (by element)", colored.fg ('medium_purple')))
    time.sleep (1)
    print (stylize("6 --> Arrange the array in ascending order", colored.fg ('medium_purple')))
    time.sleep (1)
    print (stylize("7 --> Arrange the array in descending order)", colored.fg ('medium_purple')))
    time.sleep (1)
    print (stylize("8 --> Find the smallest number on the array", colored.fg ('medium_purple')))
    time.sleep (1)
    print (stylize("9 --> Find the largest number on the array", colored.fg ('medium_purple')))
    time.sleep (1)
    print (stylize("10 --> Compute for the sum of all numbers included in the array", colored.fg ('medium_purple')))
    time.sleep (2) 
    user_input = input(stylize ("What do you want to do with the array? (Choose from 1-10): ", colored.fg ('medium_purple_2a')))
    return initial_array, user_input

def main ():
    intro ()
    randomnum ()

main ()