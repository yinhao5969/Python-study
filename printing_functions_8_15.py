#8-15
def print_modules(un, com):
    while un:
        cur = un.pop()
        print("Printing model",cur)
        com.append(cur)

def show(com):
    print("following models are printed:")
    for item in com:
        print(item)
