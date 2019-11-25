#8-9
magicians = ['a', 'b ', 'c', 'd']

def show_magicians(name_list):
    for item in name_list:
        print(item)

show_magicians(magicians)    

#8-10
def make_great(need_process_name_list):
    for index in range(len(need_process_name_list)):
        need_process_name_list[index] = 'great '+need_process_name_list[index]


make_great(magicians)
print(magicians)
show_magicians(magicians)

#8-11
def make_great(name_list):
    for index in range(len(name_list)):
        name_list[index] = 'great '+name_list[index]
    return name_list

show_magicians(make_great(magicians[:]))
show_magicians(magicians)

#8-12
def make_sandwich(*source):
    print("\n",source)
    for item in source:
        print(item)

make_sandwich('pork', 'onion', 'tomato')
make_sandwich('pork', 'onion', 'tomato', 'chicken')

#8-13
def build_profile(first, last, **info):
    """make profile"""
    profile = {}
    profile['first'] = first
    profile['last'] = last
    for key, value in info.items():
        profile[key] = value
    return profile

my_profile = build_profile('Yin',
                           'Hao',
                           education='master',
                           gender='male',
                           hoby='fish')
print(my_profile)
for key, value in sorted(my_profile.items()):
    print(key.title(),'is',value.title())

#8-14
def car(vendor, model, **info):
    des = {}
    des['vendor'] = vendor
    des['model'] = model
    for key, value in sorted(info.items()):
        des[key] = value
    return des

my_car = car('bengma',
             'tuola',
             weight = 80,
             price = 150,
             age = 500)
print(my_car)
for key, value in my_car.items():
    print(key+':'+str(value))
    
