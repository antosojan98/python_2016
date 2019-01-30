def main():
    File = open("numbers.txt","r")

    total = 0
    NumberOfLines = 0
    txt = File.readline()

    while txt != " ":
        NumberOfLines += 1
        total += int(txt)
        txt = File.readline()

    average = total/ NumberOfLines
    print("The average is ", average)

