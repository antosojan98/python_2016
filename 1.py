def test(data):
    if len(data) == len(set(data)):
        return True
    else:
        return False;
print(test([1,2,3,4]))
print(test([1,2,3,4]))

    
