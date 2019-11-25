for loop in range(1,21):
    print(loop)

for loop in range(1,1000001,100000):
    print(loop)

cal_list=list(range(1,1000001))
print("min:",min(cal_list))
print("max:",max(cal_list))
print("sum:",sum(cal_list))

odd=list(range(1,21,2))
print("odd list:",odd)
for item in odd:
    print(item)
for item in range(1,21,2):
    print(item)

exact_division=list(range(3,31,3))
print("exact division:",exact_division)
for item in exact_division:
    print(item)

cube=[]
for item in range(1,11):
    cube.append(item**3)
    print(cube[item-1])
print(cube)
for item in cube:
    print("show:",item)

cube = [item**3 for item in range(1,40)]
print(cube)
for item in cube:
    print(item)
print(cube)
cube.reverse()
print(cube)
cube.remove(8)
cube.sort()
print(cube)
print(cube[2:4])
print(cube[:4])
cube.insert(1,8)
print(cube)
print(cube[-4:])


cube = [item*2 for item in range(1,10)]
print(cube)

cube2 = cube
print(cube2)

cube3 = cube2[:]
print(cube3)

cube.insert(0,1)
print(cube)
print(cube2)
print(cube3)
