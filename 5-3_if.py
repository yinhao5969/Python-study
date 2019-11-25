#5-3
alien_color = "green"

if alien_color == "green":
    print("\nThe player got 5 points.")

if alien_color == "red":
    print("\nThe player got 10 points.")

#5-4
alien_color = "green"    

if alien_color == "green":
    print("\nThe player got 5 points.")
else:
    print("\nThe player got 10 points.")

#5-5
alien_color = "red"    

if alien_color == "green":
    print("\nThe player got 5 points.")
elif alien_color == "yellow":
    print("\nThe player got 10 points.")
else:
    print("\nThe player got 15 points.")

#5-6
age = 38
print("\nHe is "+str(age)+" years old.")
if age < 2:
    print("This is a baby.")
elif age >= 2 and age < 4:
    print("he learns to walk!")
elif age >= 4 and age < 13:
    print("This is a child.")
elif age >= 13 and age < 20:
    print("This is a teenage.")
elif age >=20 and age < 65:
    print("This is a adult.")
elif age > 65:
    print("This is an old man.")

#5-7
fruits = ['watermelon', 'strawberry', 'apple', 'banana','cherry']
print("\nMy favourite fruits are:")
for item in fruits:
    print(item)
if 'watermelon' in fruits:
    print("You really like watermelon")
elif 'shit' in fruits:
    print("You really like shit")

#5-8
users = ['admin','b','c','d']
users = []
user = 'dd'
print("\nLenth of list is",str(len(users)))
if users and len(users):
    if user in users:
        if user == 'admin':
            print("\nHellow admin, you nb.")
        else:
            print("\nHello ",user)
    else:
        print("\nYou are not allowed to log in!")
else:
    print("\nWe need to find some users.")

#5-9
current_users = ['Admin','b','c','d','e']
new_users = ['admin','E','f','g','h']
current_users_lower = [item.lower() for item in current_users]
print(current_users_lower)
for item in new_users:
    if item.lower() in current_users_lower:
        print("\nYou need change user name",item,",cause it is occupied.")
    else:
        print("\n",item,"is not used.")

#5-10
ordinal = list(range(1,10))
print("\n"+ str(ordinal))
for item in ordinal:
    if item == 1 :
        print(str(item)+"st")
    elif item == 2:
        print(str(item)+"nd")
    elif item == 3:
        print(str(item)+"rd")
    else:
        print(str(item)+"th")
