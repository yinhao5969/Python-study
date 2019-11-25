#list examples
my_friends = ["andy","jacky","tommy","sb"]

print(my_friends)

print("**********************")
print(my_friends[0].title())
print(my_friends[1].title())
print(my_friends[2].title())
print(my_friends[3].title())

print("**********************")
message = my_friends[0].title() + ' Hello'
print(message)
message = my_friends[1].title() + " Hello"
print(message)
message = my_friends[2].title() + " Hello"
print(message)
message = my_friends[3].title() + " Hello"
print(message)

#transport_means
transport_means = ['bycle','bus','train','taxi','motorbycle']
call_message = "I would like to ride a " + transport_means[0].title()
print(call_message)


#traversal
complex=["ali","baidu","zuima","joker","funny","london"]

complex.sort()
print(complex)

complex.sort(reverse=True)
print(complex)

print(sorted(complex))

print(complex)

print(sorted(complex,reverse=True))

complex.reverse()
print(complex)

print(len(complex))

print (complex[-1])

complex.remove("baidu")
print(complex)

#print(complex[100])
