#so operation
custom_list = ["ali","laodi", "nai", "po", "gong"]
print(custom_list)
print(len(custom_list))

custom_list.reverse()
print(custom_list)

custom_list.sort(reverse= True)
print(custom_list)

custom_list.sort(reverse= False)
print(custom_list)

print(custom_list)

#custom_list.sorted(reverse= True)
print(sorted(custom_list,reverse= True))
print(custom_list)

#place to go
places=["egypt","xinjiang","sichuan","japan","europe"]
print("before:\n",places)

#sorted
sortedplaces=sorted(places,reverse= True)
print(sortedplaces)
sortedplaces=sorted(places,reverse= False)
print(sortedplaces)

print("check:\n"+str(places))

#reverse
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)







