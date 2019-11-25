#7-4
menu = []
while True:
    top = input("\nPlease tell us what you need?\n")
    if top == "bye":
        break
    else:
        menu.append(top)
        print(top,"is added to the menu.")
        print("\ncurent menu is as following:")
        for item in menu:
            print(item)

#7-5
active = True
while True:
    agestr = input("How old are you?\n")
    agevalue = int(agestr)
    if active == True:
        if agevalue < 3:
            print("no charge.")
        elif agevalue >= 3 and agevalue < 12:
            print("tickec counts $10")
        elif agevalue >= 12 and agevalue < 15:
            print("tickec counts $15")
        else:
            active = False
            print("adult ticket")
    else:
        break;

#7-7
while True:
    print("i'm ok")
    break

#6-1
people = {'firstname': 'Yin',
          'secondname': 'Xiaoer',
          'age': 18,
          'city': 'Hefei'}
print(people)
del people["firstname"]
print(people)

    
        
    


