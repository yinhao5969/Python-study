#10_11
import json
file_name = 'favourite_number.json'

def get_favourite_number():
    number = input('Please input your favourite number:\n')

    if number.isdigit():
        with open(file_name, 'w') as file_object:
            json.dump(number, file_object)
    else:
        print('What you input is not a nunmber')

def read_favourite_number():
    try:
        with open(file_name) as file_object:
            #content = file_object.read()
            content = json.load(file_object)
        print(content)
    except FileNotFoundError:
        print('No favourite number is recorded.')

#get_favourite_number()
#read_favourite_number()

print('*********************************')

#10_12
def show_favourite():
    try:
        with open(file_name) as file_object:            
            content = json.load(file_object)
        print('your favourite number is', content)

    except FileNotFoundError:
         number = input('Please input your favourite number:\n')
         if number.isdigit():
             with open(file_name, 'w') as file_object:
                json.dump(number, file_object)
         else:            
             print('What you input is not a nunmber')

show_favourite()

#10_13
def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as obj:
            username = json.load(obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    filename = 'username.json'
    username = input('Please input your name:\n')
    with open(filename, 'w') as obj:
        json.dump(username, obj)
    return username

def check_username_logged(username):
    result = input('Is your name is '+username+'?\n')
    if result == 'Y' or result == 'y':
        return True
    else:
        return False
    
def greeting():
    username = get_stored_username()
    filename = 'username.json'
    if username:
        if(check_username_logged(username)):
            print('Welcome back again', username)
        else:
            username = get_new_username()
            print('Hi, nice to meet you', username)
    else:
        print('Hi, nice to meet you', username)

greeting()
    
    
                   
