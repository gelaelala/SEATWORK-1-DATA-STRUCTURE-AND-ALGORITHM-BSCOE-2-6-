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

# function for the program intro
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

# function for displaying the initial array and asking for user's input for what they want to do with the given array
def randomnum ():
    initial_array = [92, 45, 27, 53, 77, 22, 77, 14, 50, 70]
    print (stylize (f"Here's your initial array: {initial_array}", colored.fg ('medium_purple_2a')))
    print ("\t")
    time.sleep (1)
    print ("Here's your menu of the options that you want to do with the given array:")
    time.sleep (2)
    print (stylize ("1 --> Add an element on the array", colored.fg ('medium_purple')))
    print (stylize ("2 --> Insert an element on the array (by index)", colored.fg ('medium_purple')))
    print (stylize ("3 --> Modify an element on the array", colored.fg ('medium_purple')))
    print (stylize ("4 --> Remove an element on the array (by index)", colored.fg ('medium_purple')))
    print (stylize ("5 --> Remove an element on the array (by element)", colored.fg ('medium_purple')))
    print (stylize ("6 --> Arrange the array in ascending order", colored.fg ('medium_purple')))
    print (stylize ("7 --> Arrange the array in descending order", colored.fg ('medium_purple')))
    print (stylize ("8 --> Reverse the array", colored.fg ('medium_purple')))
    print (stylize ("9 --> Find the smallest number on the array", colored.fg ('medium_purple')))
    print (stylize ("10 --> Find the largest number on the array", colored.fg ('medium_purple')))
    print (stylize ("11 --> Compute for the sum of all numbers included in the array", colored.fg ('medium_purple')))
    print ("\t")
    time.sleep (2) 
    user_input = input(stylize ("What do you want to do with the array? (Choose from 1-10): ", colored.fg ('medium_purple_2a')))
    print ("\t")
    time.sleep (1)
    return initial_array, user_input

# function for all the built-in functions for list that will be used in the menus provided 
def array_feature (ini_array, user):
    if user == "1": # for adding an element on the end of the array
        add_num = int(input ("Enter a number you want to add to the array: "))
        print ('\t')
        ini_array.append (add_num)
        time.sleep (1)
        print ("Element has been added to the array.")
        print ("\t")
        time.sleep (1)
        print (stylize (f"This is the new array: {ini_array}", colored.fg ('indian_red_1d')))
    elif user == "2": # for inserting an element on any of the index on the array
        index = int(input("Enter the index you want to insert your element: "))
        element_num = int(input ("Enter the element you want to insert: "))
        print ('\t')
        ini_array.insert (index, element_num)
        time.sleep (1)
        print ("Element has been inserted to the index you indicated in the array.")
        print ("\t")
        time.sleep (1)
        print (stylize (f"This is the new array: {ini_array}", colored.fg ('sandy_brown')))
    elif user == "3": # for modifying an element
        index = int(input ("Enter the index you want to modify: "))
        modify_num = int(input ("Enter the new element: "))
        print ('\t')
        ini_array [index] = modify_num
        time.sleep (1)
        print ("Element has been modified to the array.")
        print ("\t")
        time.sleep (1)
        print (stylize (f"This is the new array: {ini_array}", colored.fg ('khaki_1')))
    elif user == "4": # for removing an element by index using pop ()
        index = int(input("Enter the index you want to remove: "))
        print ('\t')
        ini_array.pop (index)
        time.sleep (1)
        print ("The element has been removed.")
        print ('\t')
        time.sleep (1)
        print (stylize (f"This is the new array: {ini_array}", colored.fg ('spring_green_2a')))
    elif user == "5": # for removing an element by choosing a specific element on the array using remove ()
        element = int(input("Enter the element you want to remove from the array: "))
        print ('\t')
        ini_array.remove (element)
        time.sleep (1)
        print ("The element has been removed.")
        print ("\t")
        time.sleep (1)
        print (stylize (f"This is the new array: {ini_array}", colored.fg ('light_sky_blue_1')))
    elif user == "6": # for sorting the array in ascending order 
        time.sleep (1)
        ini_array.sort ()
        print ("The array has been sorted in ascending order.")
        print ("\t")
        time.sleep (1)
        print (stylize (f"This is the new array: {ini_array}", colored.fg ('blue_violet')))
    elif user == "7": # for sorting the array in descending order
        time.sleep (1)
        ini_array.sort (reverse = True)
        print ("The array has been sorted in descending order")
        print ("\t")
        time.sleep (1)
        print (stylize (f"This is the new array: {ini_array}", colored.fg ('purple_4b')))
    elif user == "8": # for reversing the array
        time.sleep (1)
        ini_array.reverse ()
        print ("The array has been reversed.")
        print ("\t")
        time.sleep (1)
        print (stylize (f"This is the new array: {ini_array}", colored.fg ('wheat_1')))
    elif user == "9": # for finding the smallest number on the array using min ()
        time.sleep (1)
        smallest_num = min (ini_array)
        print ("Smallest number has been identified on the array.")
        print ("\t")
        time.sleep (1)
        print (stylize (f"The smallest number found on the array is {smallest_num}", colored.fg ('light_yellow_3')))
    elif user == "10": # for finding the largest number on the array using max ()
        time.sleep (1)
        largest_num = max (ini_array)
        print ("Largest number has been identified on the array.")
        print ("\t")
        time.sleep (1)
        print (stylize (f"The largest number found on the array is {largest_num}", colored.fg ('grey_54')))
    elif user == "11": # for calculating the total sum of all numbers on the array using sum ()
        time.sleep (1)
        total_array = sum (ini_array)
        print ("Total sum of the numbers in the array has been calculated.")
        print ("\t")
        time.sleep (1)
        print (stylize (f"The total sum of numbers in the array is {total_array}", colored.fg ('khaki_1')))

# function where the program will ask the user to either restart or end the program
def continue_program (ini_array):
    print ("\t")
    continue_user = input ("Do you want to restart the program? (yes/no): ")
    if continue_user == "yes":
        print ("\t")
        print (stylize (f"Restarting the program. Please wait.", colored.fg ('medium_purple_2a')))
        print ("\t")
        time.sleep (3)
        main () # the program will go back to randomnum () function to display the initial array and to ask the user again which feature will be used for modification
    elif continue_user == "no":
        print ("\t")
        print (stylize (f"Here's your final array after modifying: {ini_array}", colored.fg ('medium_purple_2a'))) # The program will show the final array of numbers after modifying
        time.sleep (1)
        print ("Thank you for using the program. Hope we'll see you soo again!")
        print ("\t")
        print (stylize ("Ending the program.", colored.fg ('red_3a')))
        time.sleep (3)
        sys.exit # The program will close when the user decided to not continue modifying the program

def main ():
    ini_array ,user = randomnum ()
    array_feature (ini_array, user)
    continue_program (ini_array)

intro()
main ()