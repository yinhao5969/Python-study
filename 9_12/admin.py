#9_12
from user import User
class Admin(User):
    def __init__(self, first_name, last_name, privileges, gender='male', education='master', login_attempts=0):
        super().__init__(first_name, last_name, gender, education, login_attempts)
        self.privileges = privileges


