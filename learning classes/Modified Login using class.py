class User():
    def __init__(self, first_name, last_name):
        self.fname = first_name
        self.lname = last_name
        self.login_attempts=0

    def describe_user(self):

        print("First name: " + self.fname)
        print("Last name: " + self.lname)

    def increment_loginn_attempts(self):
        self.login_attempts+=1

    def loginattempts(self):
        self.login_attempts=str(self.login_attempts)
        print("login attempts "+self.login_attempts)

    def greet_users(self):

        print("Greetings ALIEN: " + self.fname + " " + self.lname)

    def reset_loginattempts(self):
        self.login_attempts=0
        self.login_attempts=str(self.login_attempts)
        print("Login attemps(after reset)"+self.login_attempts)



all_users = {}

while True:

    enter_user_name = input("Do u want to  enter alien's credentials?(yes or no)")

    if enter_user_name == "no":
        break

    if enter_user_name == "yes":

        user_fname = input("enter alien first  name: ")
        user_lname = input("enter alien last namme: ")

        all_users.update({user_fname: user_lname})

        u = User(user_fname, user_lname)
        for i in range(len(all_users)):
            u.increment_loginn_attempts()

        u.describe_user()
        u.greet_users()
        u.loginattempts()
        u. reset_loginattempts()
            