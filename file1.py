def read_numbers():
    file_object = open('text.txt.txt', 'r')
    line = file_object.readline()
    line = line.rstrip('\n')
    while line != '':
        print(line)
        line = file_object.readline().rstrip('\n')
        line = line.rstrip('\n')
    file_object.close()
read_numbers()
