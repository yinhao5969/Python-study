#9-11
class User():
    def __init__(self, first_name, last_name, gender='male', education='master', login_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.education = education
        self.login_attempts = login_attempts

    def desc(self):
        print('\n'+self.first_name,self.last_name,self.gender,self.education,self.login_attempts)

    def greetings(self):
        print('\n'+'Hello '+self.first_name.title()+self.last_name.title())

    def inc_cnt(self):
        self.login_attempts += 1 

    def reset_cnt(self):
        self.login_attempts = 0

class Admin(User):
    def __init__(self, first_name, last_name, privileges, gender='male', education='master', login_attempts=0):
        super().__init__(first_name, last_name, gender, education, login_attempts)
        self.privileges = privileges

class Privileges():
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        for item in self.privileges:
            print('can '+ item)
