#6-1
people = {'firstname': 'Yin',
          'secondname': 'Xiaoer',
          'age': 18,
          'city': 'Hefei'}
print(people)
for key, value in people.items():
    print(key, "is", value)

#6-2
luck_number = {'a': 1,
               'b': 2,
               'c': 3,
               'd': 4,
               'e': 5}
print('a\'s favourit number is '+str(luck_number['a']))
print('b\'s favourit number is '+str(luck_number['b']))
print('c\'s favourit number is '+str(luck_number['c']))
print('d\'s favourit number is '+str(luck_number['d']))
print('e\'s favourit number is '+str(luck_number['e']))

#6-3
vocabulary = {'for': 'loop',
              'if': 'condition',
              '+': 'puls',
              '-': 'minus',
              '*': 'multiple'}
print(vocabulary)

#6-4
for key, value in vocabulary.items():
    print(key,"means", value)

vocabulary['print'] = 'show in screen'
for key, value in vocabulary.items():
    print(key,"means", value)

#6-5
rivers = {'Nile': 'Egypt',
          'Amazon': 'Brazil',
          'Yangtze': 'China'}
for river, country in rivers.items():
    print(river, 'runs through', country)

for river in rivers.keys():
    print(river)

for value in rivers.values():
    print(value)    

#6-6
favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'}
for key, value in favourite_languages.items():
    print(key,"\'s favourite language is", value)

invest = ['zhangsan','lisi','edward']
for item in invest:
    if item in favourite_languages.keys():
        print("Thank you!",item)
    else:
        print("Please join the investigation,",item)

#6-7
zhangsan = {
    'firstname': 'Zhang',
    'secondname': 'San',
    'age': 18,
    'city': 'Hefei'}

lisi = {
    'firstname': 'Li',
    'secondname': 'Si',
    'age': 29,
    'city': 'Dongguan'}

ermazi = {
    'firstname': 'Wang',
    'secondname': 'Mazi',
    'age': 30,
    'city': 'Ningxia'}

peoples =[zhangsan, lisi, ermazi]
print(peoples)

for people in peoples:
    print("\n")
    for key, value in people.items():
        print(key,"is",value)

#6-8
dog = {
    "owner": "zhangsan",
    "type": "canine"}

cat = {
    "type": "cat",
    "owner": "lisi",
    "food": "fish"}

parrot = {
    "type": "bird",
    "owner": "mazi"}

pets = [dog, cat, parrot]
for pet in pets:
    print("\n")
    for key, value in sorted(pet.items()):
        print(key+":"+value)

#6-9
fun_places = {
    "zhangsan": ["quanjiao","chuzhou","nanjing"],
    "lisi": ["paris", "tokyo", "new york"],
    "mazi": ["chengdu", "beijing", "zanbiya"]}
for people, places in fun_places.items():
    print("\n"+people+"\'s favourite places are:")
    for place in places:
        print(place)

#6-10
luck_number = {'a': [1, 18, 41],
               'b': [2,1589,5674,7777],
               'c': [3],
               'd': [4],
               'e': [5,887]}
for people, numbers in luck_number.items():
    numstr = ""
    cnt = len(numbers)
    if cnt > 1:
        loopcnt = cnt
        for number in numbers:
            numstr += str(number)
            #print("before:",loopcnt)
            if loopcnt != 1:
                numstr += ","
                
            else:
                numstr +="."
            loopcnt -= 1
            #print("after:",loopcnt)
        print(people+"\'s favourite numbers are",numstr)
        
    else:
        numstr = str(numbers[0])
        print(people+"\'s favourite numbers is",numstr+".")

#6-11
hangzhou = {
    "country": "china",
    "population": 1200,
    "fact": "xihu is great"}

paris = {
    "country": "french",
    "population": 3200,
    "fact": "romantic"}

tokyo = {
    "country": "japan",
    "population": 1200,
    "fact": "triditional"}

cities = {
    "hangzhou": hangzhou,
    "paris": paris,
    "tokyo": tokyo}

print(cities)

for city, dec in cities.items():
    print("\n"+city,"as followings:")
    for item, content in dec.items():
        print(item,":",content)

#6-12
for city, dec in cities.items():
    print("\n"+city.title(),"as followings:")
    for item, content in dec.items():
        print(item.title(),":",str(content).title())        
