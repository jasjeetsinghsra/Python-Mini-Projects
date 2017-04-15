#A demo on how to use the built in procedure raw_input()
#to make a simple text-based user interface.  This program
#will accept a bunch of values and print the average of them.

print "Mr. Matrix's Mathemagical Mean Machine"
print "--------------------------------------"
print "Enter any number of integers to take their average!"
print "Enter q to quit or t to get the average of what you've entered so far."
total = 0
count = 0
#This loop will continue prompting users for input until
#we get a command to stop.
while True:
    #The raw_input() procedure takes a prompt string as an
    #argument and displays it to the user, and then the program
    #stops and waits for the user to write something and press
    #enter.  The text they entered is then returned as a string.
    text = raw_input("Enter a number: ")

    #If we see a quit or total command, stop the loop.
    if text == "q" or text == "t":
        break

    #try / except blocks are a way for us to try to do something
    #that we think might produce an error.  We try to use the
    #int operator on the user input which will turn the string
    #into a number if they have written an integer.  If the input
    #is not an integer in string form, the int operator will give
    #a ValueError, and Python will skip to the except block.
    try:
        number = int(text)
        total += number
        count += 1
    except ValueError:
        print "I'm sorry, I didn't understand that."

#Once the loop is done, if the user gave a total command, print
#the results.  Then the program ends!
if text == "t":
    print "Total sum: ", total
    print "Total count: " + str(count)
    print "Average: " + str(1.0 * total / count)
