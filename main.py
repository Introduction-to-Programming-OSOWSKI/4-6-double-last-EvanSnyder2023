def doubleLast(j):
    myList = j

    myList.append(myList[-1])

    return myList

print (doubleLast([0,0,0,0,0,0,0,0,0,0,0,0,1]))