def read():
    file = open('text.txt.txt','r')
    total = 0
    n = 0
    for i in file:
        i = int(i.rstrip('\n'))
        total += i
        n += 1
        print(n , ':',i)
        avg = total/n
    print('Total no is :', total)
    print('Average no is:',avg)
    file.close()
read()                
