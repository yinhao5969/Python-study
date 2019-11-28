#10-1
file_name = 'python do what.txt'
with open(file_name) as file_object:
    file = file_object.read()
print(file)

with open(file_name) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line)

with open(file_name) as file_object:
    for item in file_object:
        print(item)

#10-2
file_name = 'python do what.txt'
with open(file_name) as file_object:
    for line in file_object:
        print('befor',line)
        line = line.replace('python', 'c')
        print('after',line)

#10-3 10-4
while True:
    visitor = input('Please input your name\n')
    if visitor == 'q':
        break
    file_name = 'visitors.txt'
    with open(file_name, 'a') as file_object:
        file_object.write(visitor+'\n')

#10-5
while True:
    reason = input('why you like to program?\n')
    if reason == 'q':
        break
    file_name = 'reason.txt'
    with open(file_name, 'a') as file_object:
        file_object.write(reason+'\n')
        
