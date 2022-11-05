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
    print ("\t")
    time.sleep (1)
    print ("Here, you'll be given an initial array with a total of 10 elements and you can modify it however you want.")
    time.sleep (1)
    print ("All you have to do is choose the option that you want from the menu and the program will do it for you.")
    time.sleep (1)
    print ("That's all and here's your array!")
    print ("\t")
    time.sleep (2)

# displaying the initial array and asking for user's input for what they want to do with the given array
def randomnum ():
    initial_array = [92, 45, 27, 53, 77, 22, 77, 14, 50, 70]
    print (stylize (f"Here's your initial array: {initial_array}", colored.fg ('medium_purple_2a')))
    print ("\t")
    time.sleep (1)
    print ("Here's your menu of the options that you want to do with the given array:")
    time.sleep (2)
    print (stylize ("1 --> Add an element on the array", colored.fg ('medium_purple')))
    time.sleep (1)
    print (stylize ("2 --> Insert an element on the array (by index)", colored.fg ('medium_purple')))
    time.sleep (1)
    print (stylize ("3 --> Modify an element on the array", colored.fg ('medium_purple')))
    time.sleep (1)
    print (stylize ("4 --> Remove an element on the array (by index)", colored.fg ('medium_purple')))
    time.sleep (1)
    print (stylize ("5 --> Remove an element on the array (by element)", colored.fg ('medium_purple')))
    time.sleep (1)
    print (stylize ("6 --> Arrange the array in ascending order", colored.fg ('medium_purple')))
    time.sleep (1)
    print (stylize ("7 --> Arrange the array in descending order)", colored.fg ('medium_purple')))
    time.sleep (1)
    print (stylize ("8 --> Find the smallest number on the array", colored.fg ('medium_purple')))
    time.sleep (1)
    print (stylize ("9 --> Find the largest number on the array", colored.fg ('medium_purple')))
    time.sleep (1)
    print (stylize ("10 --> Compute for the sum of all numbers included in the array", colored.fg ('medium_purple')))
    print ("\t")
    time.sleep (2) 
    user_input = input(stylize ("What do you want to do with the array? (Choose from 1-10): ", colored.fg ('medium_purple_2a')))
    return initial_array, user_input

# function for all the built-in functions for list that will be used in the menus provided 
def array_feature (ini_array, user):
    if user == "1": # for adding an element on the end of the array
        add_num = int(input ("Enter a number you want to add to the array: "))
        ini_array.append (add_num)
        print ("Element has been added to the array.")
        print ("\t")
        time.sleep (1)
        print (stylize (f"This is the new array: {ini_array}", colored.fg ('indian_red_1d')))
    elif user == "2": # for inserting an element on any of the index on the array
        index = int(input("Enter the index you want to insert your element: "))
        element_num = int(input ("Enter the element you want to insert: "))
        ini_array.insert (index, element_num)
        print ("Element has been inserted to the index you indicated in the array.")
        print ("\t")
        time.sleep (1)
        print (stylize (f"This is the new array: {ini_array}", colored.fg ('sandy_brown')))
    elif user == "3": # for modifying an element
        index = int(input ("Enter the index you want to modify: "))
        modify_num = int(input ("Enter the new element: "))
        ini_array [index] = modify_num
        print ("Element has been modified to the array.")
        print ("\t")
        time.sleep (1)
        print (stylize (f"This is the new array: {ini_array}", colored.fg ('khaki_1')))
    elif user == "4": # for removing an element by index using pop ()
        index = int(input("Enter the index you want to remove: "))
        ini_array.pop (index)
        print ("The element has been deleted.")
        print ('\t')
        time.sleep (1)
        print (stylize (f"This is the new array: {ini_array}", colored.fg ('spring_green_2a')))
    


def main ():
    intro ()
    ini_array ,user = randomnum ()
    array_feature (ini_array, user)

main ()