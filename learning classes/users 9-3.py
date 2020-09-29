class User():
    def __init__(self,first_name,last_name):
        self.fname=first_name
        self.lname=last_name

    def describe_user(self):
        print("First name: "+self.fname)
        print("Last name: "+self.lname)
    
    def greet_users(self):
            print("Greetings ALIEN: "+self.fname+" "+self.lname)
    
all_users={}

while True:
    enter_user_name=input("Do u want to  enter alien's credentials?(yes or no)")
    
    if enter_user_name=="no":
        break
    
    if enter_user_name=="yes":
        
    
        user_fname=input("enter alien first  name: ")
        user_lname=input("enter alien last namme: ")
    
        all_users.update({user_fname:user_lname})
        
        u=User(user_fname,user_lname)
        u.describe_user()
        u.greet_users()
