def rand():
    file = open('random.txt','r')
    total = 0
    n = 0
    for i in file:
       i = i.rstrip('\n')
       i = int(i)
       total += i
       n += 1
    print(total,': total')
    print(n, ': number')
    file.close()
rand()
