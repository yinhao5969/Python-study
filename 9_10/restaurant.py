class Restaurant(object):
    """creat a class of restaurant"""
    def __init__(self, name, cuisine, servered=0):
        self.name = name
        self.cuisine = cuisine
        self.servered = servered
    def des(self):
        print('Restaurant', self.name.title(), 'has cuisine', self.cuisine.title(), 'and has servered', str(self.servered)+' people')
    def open(self):
        print('We are open')
