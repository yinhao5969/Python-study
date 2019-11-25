#element operation
custom_list = ["laodi", "nai", "po", "gong"]
print(custom_list)

print("please come to dinner" + " " +custom_list[0].title() + " & "\
+ custom_list[1].title() + " & " \
+ custom_list[2].title() + " & " \
+ custom_list[3].title())

print(custom_list[0].title() + " can't be here!")

#replace one customer
custom_list[0] = "rap god"

#invite
print("please come to dinner" + " " +custom_list[0].title() + " & "\
+ custom_list[1].title() + " & " \
+ custom_list[2].title() + " & " \
+ custom_list[3].title())

#invide more people
print("I got a bigger box, I will invite more people")

#insert to begin
custom_list.insert(0, "andy")

#insert to middle
custom_list.insert(2, "jacky")

#append to end
custom_list.append("hutou")

#invite
print("please come to dinner" + " " +custom_list[0].title() + " & "\
+ custom_list[1].title() + " & " \
+ custom_list[2].title() + " & " \
+ custom_list[3].title() + " & " \
+ custom_list[4].title() + " & " \
+ custom_list[5].title() + " & " \
+ custom_list[6].title())

#reduce
print("\nI can only invite two peoples")
poped = custom_list.pop()
print("Hi "+ poped.title() + ",sorry, the dinner is canceled.")
print(custom_list)

print("\nI can only invite two peoples")
poped = custom_list.pop()
print("Hi "+ poped.title() + ",sorry, the dinner is canceled.")
print(custom_list)

print("\nI can only invite two peoples")
poped = custom_list.pop()
print("Hi "+ poped.title() + ",sorry, the dinner is canceled.")
print(custom_list)

print("\nI can only invite two peoples")
poped = custom_list.pop()
print("Hi "+ poped.title() + ",sorry, the dinner is canceled.")
print(custom_list)

print("\nI can only invite two peoples")
poped = custom_list.pop()
print("Hi "+ poped.title() + ",sorry, the dinner is canceled.")
print(custom_list)

print("\nplease come to dinner" + " " +custom_list[0].title() + " & "\
+ custom_list[1].title())

#del
del custom_list[0]
print(custom_list)

custom_list.remove("rap god")
print(custom_list)

custom_list.insert(10,"one")
print(custom_list)

custom_list.append("shit")

print(len(custom_list))


