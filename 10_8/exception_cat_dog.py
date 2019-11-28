#10_8
cats = ['xiaobaimao', 'pangbaimao', 'baowenmao']

dogs = ['dahuanggou', 'wangcai', 'kanmengou']

with open('cats.txt', 'w') as file_object:
    file_object.write('')
for cat in cats:
    with open('cats.txt', 'a') as file_object:
        file_object.write(cat+'\n')


with open('dogs.txt', 'w') as file_object:
    file_object.write('')

for dog in dogs:
    with open('dogs.txt', 'a') as file_object:
        file_object.write(dog+'\n')

def fileread(file_path):
    try:
        with open(file_path) as file_object:
            file = file_object.read()
            print(file)
    except FileNotFoundError:
        print('File no found!')

fileread('dogs.txt')
fileread('cats.txt')
fileread('people.txt')  

#10-9
def silentread(file_path):
    try:
        with open(file_path) as file_object:
            file = file_object.read()
            print(file)
    except FileNotFoundError:
        pass

silentread('dogs.txt')
silentread('cats.txt')
silentread('people.txt')

#10-10
def word_frequency(file):
    try:
        with open(file) as file_object:
            content = file_object.read()
    except FileNotFoundError:
        print("file not found")

    statistic = {}
    words = content.lower().split()
    for word in words:
        if word in statistic.keys():
            statistic[word] += 1
        else:
            statistic[word] = 1

    for key, value in statistic.items():
        print(key, ':', value)

file_name = 'cats.txt'
word_frequency(file_name)
        
    
