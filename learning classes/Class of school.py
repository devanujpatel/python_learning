class student:

    def __init__(self , name, std , section ):
        name1 = "school"
        self.name = name
        self.my_class= std
        self.grade = section

    def print_name(self):
        print(self.name)

    def print_class(self):
        print(self.my_class)

    def print_section(self):
        print(self.grade)


obj1 = student("name1" , "10" , "A")
obj2 = student("name2", "10" , "B")

obj1.print_name()
obj2.print_section()