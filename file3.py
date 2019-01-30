def read():
    file = input('Enter the file name with exe in the last : ')
    ofile = open(file,'r')
    line = ofile.readline()
    line = line.rstrip('\n')
    count = 1
    while line != '':
        print(count,':',line)
        line = ofile.readline()
        line = line.rstrip('\n')
        count += 1
    ofile.close()
read()
        
