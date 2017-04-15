#easygui is exactly what it sounds like: a module for easily making a simply
#graphical user interface.  You can do a lot in easgui.  To learn more, see
#the documentation here:

#http://easygui.sourceforge.net/tutorial.html#introduction

#We will cover a few basic ideas: displaying messages and getting user input.

#Start by importing everything from the easygui module.
from easygui import *

#Most easygui functions take a title as a second argument.  We're going to use
#the same string for every one, so let's save it in a variable.
title = "GUI DEMO"

#msgbox displays the string you give as an argument and gives the user an OK
#button.
msgbox("Welcome to the demo GUI!", title)

#You can specify the text of the OK button using the ok_button parameter.
msgbox("Are you read for some UI magic?", title, ok_button="I'm ready!")

#The ccbox asks gives the user "Contiue" and "Cancel" options, and returns
#true if they click continue and false if they click cancel.  You can put
#the function straight into a condition and decide what to do next.  In this case,
#if the function returns false, we display a quit message.
if not ccbox("Alright.  This is a ccbox.  Hit continue to continue or cancel to quit!", title):
    msgbox("Alright.  Later!", title, ok_button="Quit.")
    quit()

#By the way, the ynbox() function works the same as the ccbox() function except it
#displays Yes and No as choices instead of Continue and Cancel.

#But what if you want to give the user a custom set of choices?  Save the choices
#in a list and use the buttonbox() function!  It returns the choice they make.
choices = ["Blue", "Green", "Yellow", "Something else"]
choice = buttonbox("What is your favorite color?", title, choices)

if choice == "Something else":
    msgbox("Huh.  I guess you like a more interesting color!", title, ok_button="Yup.")
else:
    msgbox("Cool.  I like " + choice + " too!", title, ok_button="Wow, we're like twins!")

#By the way, the choicebox() function works the same as buttonbox(), but it will display the
#choices in a list rather than as buttons.  This is a good idea if you have lots of choices,
#or if the choice strings are long.

#Buttonboxes are all very well, but what if you want the user to be able to input text?
#There's a function for that! Use enterbox() to get a string from a user.  It returns the
#string.
band = enterbox("What's your favorite band?", title)
msgbox(band + "?  Never heard of them.", title, ok_button="Yeah right.")

#By the way, integerbox() works the same as enterbox() except it only lets the user input
#an integer, and returns an integer value instead of a string.

#Lastly, for super in-depth user-input gathering, you can use the multenterbox() to get
#a bunch of strings at once.  You need to give it a third argument which is a list of
#prompts for the fields the user will write in, and it returns a list of strings that
#the user types in.
fields = ["Place I want to go:", "Person I want to meet:", "Thing I want to do:"]
answers = multenterbox("If you could go anywhere, meet anyone, or do anything, where would you go, who would you meet, and what would you do?", title, fields)

message = answers[0] + "?  I bet it's really pretty there.  "
message += answers[1] + " sounds like a cool person.  I hope you get to meet them someday!  And "
message += answers[2] + "--that sounds amazing.  I may just do that myself!"
msgbox(message, title, ok_button="Quit.")

#That's it for the GUI demo!  Try copy+pasting this code into a python file and running
#it to get a feel for how easygui works.  You might find that there are some issues.
#For example, you can leave fields blank in the boxes where the user types.  And
#what happens when someone presses cancel?  For your project you will need to validate
#user input, and provide user friendly error messages when the user enters the wrong
#thing.  Hopefully this gets you started!
