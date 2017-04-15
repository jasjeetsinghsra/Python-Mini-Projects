class Parent():
    def __init__(self, last_name, eye_color):
        self.last_name=last_name
        self.eye_color=eye_color

    def show_info(self):
        print "Last Name: ", self.last_name
        print "Eye Color: ", self.eye_color

class Child(Parent):
    def __init__(self,last_name,eye_color, number_of_toys):
        Parent.__init__(self,last_name,eye_color)
        self.number_of_toys=number_of_toys

    #The above instance method show_info can also be inherited to class child.
    #It will display the last name and eye color of child if called with
    # childname.show_info() command
    # Now if we define a new method inside class child with thw same name as
    #in class parent that will override the command used in class parent
    # i.e- subclass method can override the class method
    # This is called Method Overriding

    def show_info(self):
        print "Last Name: ", self.last_name
        print "Eye Color: ", self.eye_color
        print "Number of toys", str(self.number_of_toys)
