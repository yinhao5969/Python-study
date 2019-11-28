#9-13
from collections import OrderedDict
dictionary = OrderedDict()
dictionary['nuli'] = 'fengdou'
dictionary['fubao'] = '996'
dictionary['zibenjia'] = 'rich people'
dictionary['future'] = 'easy'
for key, value in sorted(dictionary.items()):
    print(key,':',value)

print('\n')

for key, value in (dictionary.items()):
    print(key,':',value)


#9-14
from random import randint
class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        self.result = randint(1, self.sides)
        print('This time is', self.result)

cnt = 10
onedie = Die(cnt)
for item in range(cnt):
    onedie.roll_die()



        
        
