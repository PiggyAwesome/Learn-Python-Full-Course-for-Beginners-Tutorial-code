# Functions

def say_hi():
      print("Hello User") # Needs to be indented


print("Top")
say_hi()
print("bottom")


def say_hi(name):
    print("Hello " + name)  # Needs to be indented

say_hi("Mike")
say_hi("Steve")


def say_hi(name, age):
    print("Hello " + name + ", you are " + age)  # Needs to be indented

say_hi("Mike", "35")
say_hi("Steve", "70")


def say_hi(name, age):
    print("Hello " + name + ", you are " + str(age))  # Needs to be indented


say_hi("Mike", 35)
say_hi("Steve", 70)




