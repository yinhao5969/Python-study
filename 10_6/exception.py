#10-6
def plus():
    a = input('Please input a value:\n')
    b = input('Please input another value:\n')
    quitflag = True
    if(a == 'q' or b == 'q'):
        quitflag = True
    else:
        try:
            print('The result is', int(a)+int(b),'.')
        except ValueError:
            print('Only numbers can be added!')            
        quitflag = False

    return quitflag

#10-7
while True:
    quitflag = plus()
    print('\n')
    if quitflag:
        break

