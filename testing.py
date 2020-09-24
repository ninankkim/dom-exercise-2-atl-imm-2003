def only_evens (evenlist):
    newlist = []
    for number in evenlist:
        if number %2 == 0:
            newlist.append(number)
    return newlist

only_evens([11, 20, 42, 97, 23, 10])
print (only_evens)