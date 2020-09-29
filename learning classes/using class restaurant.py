class Restaurant:

    def __init__(self, restaurant_name, restaurant_cuisine):
        self.name = restaurant_name
        self.cuisine = restaurant_cuisine
        self.number_served=0


    def take_inputs(self):
        self.cuisine = cuisine
        self.name = name

    def describe_restaurant(self):
        print("The restaurant name is " + self.name)
        print("The restaurant cuisine is " + self.cuisine)


    def print_number_served(self):
        self.number_served=str(self.number_served)
        print("Number Served "+self.number_served)

    def open_restaurant(self):
        print(self.name+" is open")

    def set_number_served(self):
        self.number_served=input("enter the no. of customers served: ")


    def run_all(self):

        info.take_inputs()
        info.set_number_served()
        info.describe_restaurant()
        info.open_restaurant()
        info.print_number_served()


def take_inputs():
    global name,cuisine
    name=input("Enter restaurant name: ")
    global cuisine
    cuisine = input("enter restaurant cuisine")


while True:
    take_inputs()
    info = Restaurant(name, cuisine)
    info.run_all()

    enter = input("Do you want to enter more restaurants (yes to enter more or else enter no):")

    if enter == 'no':
        break

    if enter == 'yes':
        continue






