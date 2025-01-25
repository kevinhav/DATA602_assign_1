#Q1 Fix all the syntax and logical errors in the given source code 
#add comments to explain your reasoning

# This program gets three test scores and displays their average.  It congratulates the user if the 
# average is a high score. The high score variable holds the value that is considered a high score.

HIGH_SCORE = 95
 
# Get the test scores.
# Converted string inputs to integers
test1 = int(input('Enter the score for test 1: '))
test2 = int(input('Enter the score for test 2: '))
test3 = int(input('Enter the score for test 3: ')) # Added input to get third test score
# Calculate the average test score.
average = (test1 + test2 + test3) / 3  # Fixed order of operations
# Print the average.
print(f'The average score is {average}')
# If the average is a high score,
# congratulate the user.
if average >= HIGH_SCORE: # Updated reference to the defined constant, fixed syntax
    print('Congratulations!\n') # Added line break for style points
    print('That is a great average!') # Moved into IF statement for correct context

#Q2
#The area of a rectangle is the rectangle’s length times its width. Write a program that asks for the length and width of two rectangles and prints to the user the area of both rectangles. 
def rectangle_area()->None:
 '''Prompts the user for the length and width of two rectangles, then calculates and prints the area of each'''

 try:
  # Get inputs for rectangle A
  A_width = int(input("What is the width of rectangle A?\n")) # Convert string input to integer
  A_length = int(input("What is the length of rectangle A?\n"))
 
  # Get inputs for rectangle B
  B_width = int(input("What is the width of rectangle B?\n")) # Convert string input to integer
  B_length = int(input("What is the length of rectangle B?\n"))
 
  A_area = A_width * A_length
  B_area = B_width * B_length

  # Print the areas to the user
  print(f'The area of rectangle A is: {A_area}\n')
  print(f'The area of rectangle B is: {B_area}\n')

 except ValueError:
  print("Please enter valid numbers as your inputs")
 
 return None

#Q3 
#Ask a user to enter their first name and their age and assign it to the variables name and age. 
#The variable name should be a string and the variable age should be an int.  

#Using the variables name and age, print a message to the user stating something along the lines of:
# "Happy birthday, name!  You are age years old today!"

def happy_birthday()->None:
 '''Request the name and age of the user and wish them a happy birthday'''

 # Get name and age from user
 name = input("What is your name?\n") # Is already a string 
 
 try:
  age = int(input("How old are you?\n")) # Convert string input to integer
  
  # Return message to user
  print(f'Congratulations! You are {age} years old today, {name}!')
  
 except ValueError:
  print("Please input a number for age")
  
 return None
