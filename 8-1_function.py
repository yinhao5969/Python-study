#8-1
def show_message():
    print("\nI will learn how to use funciton in python in this paragraph.")

show_message()

#8-2
def favourite_book(title):
    print("\nMy favourite book is "+title+".")

favourite_book("hongloumeng".title())

#8-3
def make_shirt(size, logo):
    print('T-shirt with size '+str(size)+' shows '+str(logo))

make_shirt(12, "shabi")
make_shirt(logo='oye', size=30)
    
8-4
def make_shirt(size, logo='I love Python'):
    print('T-shirt with size '+str(size)+' show '+str(logo))

make_shirt(54)
make_shirt(42)
make_shirt(21, 'ssfdff')

#8-5
def desc_city(city, country='China'):
    print(('\nCity '+city+' is in '+country+'. ').strip())

desc_city('chengdu')
desc_city('quanjiao')
desc_city('tokyo', 'Japan')

#8-6
def city_country(city, country='China'):
    return city+', '+country

print('\n'+city_country('nanjing'))
print('\n'+city_country('beijing'))
print('\n'+city_country('tokyo', 'Japan'))

#8-7
def make_album(singer, album, song_cnt=0):
    item = {'singer': singer,
            'album': album}
    if song_cnt:
        item['cnt'] = song_cnt
    return item
        
MJ = make_album('Machel Jackson', 'Thriller')
Jay = make_album('Jay chou', 'Fantasy')
oye = make_album('oye', 'shuang')
print(MJ)
print(Jay)
print(oye)
liudehua = make_album('liudehua', 'zhenyongyuan', 44)
print(liudehua)

print('\n')
albums = []
while True:
    singer = input('Input singer:\n')
    album = input('Input album:\n')
    example = make_album(singer.upper(), album.title())
    albums.append(example)
    print(example)

    quit_flag = input('Quit now?')
    if (quit_flag == 'yes') or (quit_flag == 'y'):
        break
    else:
        print('********************************')

print('\n')
for item in albums:
    for key, value in item.items():
        print(key+':'+value)
        
