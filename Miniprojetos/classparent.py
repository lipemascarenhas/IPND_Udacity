''' class Parent
        - last_name
        - eye_color
    class child (inherits from Parent)
        - number_of_toys'''

class Parent():
    def __init__(self, last_name, eye_color):
        print ("Parent constructor called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print ("Last name - "+self.last_name)
        print ("Last name - "+self.eye_color)


class Child(Parent):
    def __init__ (self, last_name, eye_color, number_of_toys):
        Parent.__init__(self, last_name, eye_color)
        print ("Child constructor called")
        self.number_of_toys = number_of_toys

    def show_info(self):
        print ("Last name - "+self.last_name)
        print ("Last name - "+self.eye_color)
        print ("Number of toys - "+str(self.number_of_toys))

#billy_cyrus = Parent ("Cyrus", "blue")
#billy_cyrus.show_info()
miley_cyrus = Child ("Cyrus", "Blue", 5)
miley_cyrus.show_info()
