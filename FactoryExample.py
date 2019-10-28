#Inheritance in python
# derived_class_name(base_class)

# For Example : In the below example Image inherits Button class.

# Factory Pattern the the object is created by using wrapper class and it is created using the type of string passed. 
# The client doest have access to the core logic of the class.

# class Button(object):
#    html = ""
#    def get_html(self):
#       return self.html

# Class Button is inherited by the Image class.
# class Image(Button):
#    html = "<img></img>"


# class Input(Button):
#    html = "<input></input>"

# class Flash(Button):
#    html = "<obj></obj>"

# class ButtonFactory():
#    def create_button(self, typ):
		# typ.capitalize() : Transforms the first letter to upper case.
#       targetclass = typ.capitalize()
#       #globals() - Returns a dictionary containing the variables declared in the global namespaces.
#       return globals()[targetclass]()
      

# button_obj = ButtonFactory()
# button = ['image', 'input', 'flash']
# for b in button:
#    print(button_obj.create_button(b).get_html())

a = 10
b = 10
print(globals())