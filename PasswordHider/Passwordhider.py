# Enter your the masterpassword of your choosing here.
passcode = "1123"

# This asks you to enter your passcode to access your information
while (True):
    ask_passcode = input("Enter Passcode: ")
    if ask_passcode == passcode:
        print("Passcode Correct")
        # This next segment will display all your login information and domain.
        # How you format how the information looks on the actual executable is up to you.
        # What's written is just an example.
        # To add new entries write print("") Write whatever information you want between the quotation marks.
        print("Domain: abc.com | Username: abcdefg | Password: 12345678")
    # if the passcode is incorrect it will run this line of code before restarting the loop.
    else:
        print("Try Again")


