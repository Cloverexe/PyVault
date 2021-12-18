# From what I understand right now this just imports the random function so a random whatever can be used.
# In this case, random.randint
import random    

# Main code section where everything happens
# While loop is used for repeating the code
# The condition for this loop is "True" ("(True)") so that it infinitely loops until it hits a break statement
while (True):
    # The variables parameters for num and rand are between the parentheses, although, they are changable. Think of it like x, y.
    # BUT there does still have to be a comma space between them or it wont work.
    # Selects random number for the computer to find
    num = random.randint(1000, 10000)
    # Chooses another random number and prints (displays) it
    rand = random.randint(1000, 10000)
    print(rand)
    # the if statement where it will do a task or command or even another if statement if a condition is true.
    # In this case if the random number the variable rand chooses is equal to the other random generated number from the variable num.
    if rand == num:
        print("Number ID found: " + str(num))
        # Break stops the loop and finishes any remaining lines of code if any.
        break
    # Else handles what happens if the condition from the original if statement is false.
    else:
        # Continue does what it says, continues the code from the beginning over and over.
        continue
        
# If you wanted the code to never stop and constantly generate and find a number just remove the break command from line 21
