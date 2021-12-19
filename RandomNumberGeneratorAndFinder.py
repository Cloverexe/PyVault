# From what I understand right now this just imports the random function so a random whatever can be used.
# In this case, random.randint
import random    

# Below are the conditions variables for the number the program should find.

# To choose which option to find num, comment out the ones you dont want to use and uncomment the one you do want to use.

# The variable directly below this line is for a number the user would enter
# num = 3

# Below is a 2nd option for choosing num's value by letting the user choose.
#num = int(input("What is your number: "))

# The variable directly below this line is for generating a random number for the computer to find.
num = random.randint(1000, 10000)

#This variable is to find the number of times it took for the computer to find the number. Its base is zero. Line 36 shows where it's value is increased.
count = 0

# Main code section where everything happens
# While loop is used for repeating the code
# The condition for this loop is "True" ("(True)") so that it infinitely loops until it hits a break statement

while (True):
    
    # The variables parameters for num and rand are between the parentheses, although, they are changable. Think of it like x, y.
    # BUT there does still have to be a comma space between them or it wont work.
    # Selects random number for the computer to find
 
    # Chooses another random number and prints (displays) it
    rand = random.randint(1000, 10000)
    print(rand)
    
    # This adds 1 to the variable count each time a number is generated. 
    count += 1
    
    # The if statement where it will do a task or command or even another if statement if a condition is true.
    # In this case if the random number the variable rand chooses is equal to the other random generated number from the variable num.
     if rand == num:
        print("Number ID found: " + str(num))
        print("Found after " + str(count) + " tries.")
        # Break stops the loop and finishes any remaining lines of code if any.
        break
        
# If you wanted the code to never stop and constantly generate and find a number just remove the break command from line 21
