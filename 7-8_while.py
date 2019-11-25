#7-8
sandwitch_orders = ['chichen', 'beef', 'pork']
finished_sandwitch = []
while sandwitch_orders:
    done = sandwitch_orders.pop()
    finished_sandwitch.append(done)
    print('I made your', done, "sandwitch")
print("All your sandwitchs are done as:")
for item in finished_sandwitch:
    print(item)

#7-9
sandwitch_orders = ['pastrami','pastrami','chichen','pastrami', 'beef', 'pork']
print("\nPastrami sandwitch is sold out.")
while "pastrami" in sandwitch_orders:
    sandwitch_orders.remove('pastrami')
for item in sandwitch_orders:
    print(item)

#7-10
places = []
while True:
    place = input("If you could visit one place in the world, where would you go?\n")
    if place == "exit":
        break
    else:
        places.append(place)
for item in places:
    print(item)



    
