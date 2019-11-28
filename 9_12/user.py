#9-12
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


