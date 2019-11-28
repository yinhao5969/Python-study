class Privileges():
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        for item in self.privileges:
            print('can '+ item)
