breakfast = "bing"
breakfast_big = "Bing"
lunch = "chaofan"
dinner = "noodles"

print("Is breakfast == bing? I predict True.")
print(breakfast == "bing")

print("\nIs breakfast == shit? I predict False.")
print(breakfast == "shit")

print("\nIs breakfast == breakfast_big? I predict False.")
print(breakfast == breakfast_big)

print("\nIs breakfast == breakfast_big.lower()? I predict True.")
print(breakfast == breakfast_big.lower())

print("\nIs breakfast.upper() == breakfast_big.upper? I predict True.")
print(breakfast.upper() == breakfast_big.upper())

x = 10
y = 9
print("\n"+str(x)+">"+str(y))
print(x > y)

x = 10
y = 9
print("\n"+str(x)+"<"+str(y))
print(x < y)

x = 10
y = 9
print("\n"+str(x)+">="+str(y))
print(x >= y)

x = 10
y = 9
print("\n"+str(x)+"<"+str(y))
print(x < y)

x = 10
y = 12
print("\n"+str(x)+"<="+str(y))
print(x <= y)

x = 10
y = 9
print("\n"+str(x)+"=="+str(y))
print(x == y)

x = 10
y = 9
print("\n"+str(x)+">"+str(y)+" and "+str(x)+">="+str(y))
print((x > y) and (x >= y))

x = 10
y = 9
print("\n"+str(x)+">"+str(y)+" or "+str(x)+"<="+str(y))
print((x > y) or (x <= y))

meal = [breakfast,lunch,dinner]
print("\nnormal meals are:")
for item in meal:
    print(item)

if "snack" in meal:
    print("\nsnack is normal meal")
else:
    print("\nsanck is bullshit")

meal = [breakfast,lunch,dinner]
print("\nnormal meals are:")
meal.append("snack")
for item in meal:
    print(item)
if "snack" in meal:
    print("\nsnack is normal meal")
else:
    print("\nsanck is bullshit")
if "shit" not in meal:
    print("shit is not in meal")
