#7-1
message = input("which car do you want to rent?\n")
print("let me see if we have a",message.upper())

#7-2
ordercnt = input("How many seats do you want?\n")
cnt = int(ordercnt)
if cnt < 8:
    print("OK, resevation is successful!")
else:
    print("Sorry, we don't have engough seats for",ordercnt,"peoples.")

#7-3
value = input("Please input a value.\n")
if (int(value) % 10) == 0:
    print("The input number is an integral multiple of 10")
else:
    print("The input number is not an integral muliple of 10")
