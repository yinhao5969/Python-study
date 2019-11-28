#9-1
class Restaurant():
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
    def des(self):
        print('Restaurant', self.name.title(), 'has cuisine', self.cuisine.title())
    def open(self):
        print('We are open')

#9-2
cangying = Restaurant('Shit', 'chuan')
print('\n',cangying.name)
print(cangying.cuisine)
cangying.des()
cangying.open()

luxury = Restaurant('Hong', 'yue')
print('\n',luxury.name)
print(luxury.cuisine)
luxury.des()
luxury.open()

quick = Restaurant('longjiang', 'zhujiao')
print('\n',quick.name)
print(quick.cuisine)
quick.des()
quick.open()

paidang = Restaurant('Kao', 'barbecue')
print('\n',paidang.name)
print(paidang.cuisine)
paidang.des()
paidang.open()

#9-3
class User():
    def __init__(self, first_name, last_name, gender='male', education='master'):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.education = education
    def des(self):
        print('\n'+self.first_name,self.last_name,self.gender,self.education)
    def greetings(self):
        print('\n'+'Hello '+self.first_name.title()+self.last_name.title())

yinhao = User('yin', 'hao')
yinhao.des()
yinhao.greetings()

yingyi = User('ying', 'yi', 'female', 'banchelor')
yingyi.des()
yingyi.greetings()

yinyifan = User('yin', 'yifan', 'female', 'kindgarden')
yinyifan.des()
yinyifan.greetings()

#9-4
class Restaurant():
    def __init__(self, name, cuisine, servered=0):
        self.name = name
        self.cuisine = cuisine
        self.servered = servered
    def des(self):
        print('Restaurant', self.name.title(), 'has cuisine', self.cuisine.title(), 'and has servered', str(self.servered)+' people')
    def open(self):
        print('We are open')

kfc = Restaurant('KFC', 'quick', 35)
kfc.des()

kfc.servered = 12222
kfc.des()

#9-5
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

access = User('passenger', 'one')
access.inc_cnt();
access.desc();
access.inc_cnt();
access.desc();
access.inc_cnt();
access.desc();
access.inc_cnt();
access.desc();
access.inc_cnt();
access.desc();
access.reset_cnt();
access.desc();

#9-6
class IceCreamShop(Restaurant):
    def __init__(self, name, cuisine, servered=0, flavor=['strawberry']):
        super().__init__(name, cuisine, servered)
        self.flavor = flavor
    def showtype(self):
        print(self.flavor)

cold = IceCreamShop('ice', 'sweet', 50, ['shit' ,'pee', 'puff'])
cold.open()
cold.des()
cold.showtype()

#9-7
class Admin(User):
    def __init__(self, first_name, last_name, gender='male', education='master', login_attempts=0, privileges='super'):
        super().__init__(first_name, last_name, gender, education, login_attempts)
        self.privileges = privileges

    def show_privileges(self):
        print(self.privileges)

God = Admin('jesus', 'christ', 'god', 'none', 57, 'top')
God.desc()
God.greetings()
God.inc_cnt()
God.reset_cnt()
God.show_privileges()

#9-8
class Privileges():
    def __init__(self, privileges):
        self.privileges = privileges
    def show_privileges(self):
        print('can '+self.privileges)

class Admin(User):
    def __init__(self, first_name, last_name, privileges, gender='male', education='master', login_attempts=0):
        super().__init__(first_name, last_name, gender, education, login_attempts)
        self.privileges = privileges

superman = Admin('clark', 'kent', Privileges('fly'))
superman.desc()
superman.greetings()
superman.inc_cnt()
superman.reset_cnt()
superman.privileges.show_privileges()

        
