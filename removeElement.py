import random
def removeElem (lst):
    count = 0
    while(lst != []):
        r = random.randint(0, len(lst)-1)
        lst = remove(r, lst)
        print(lst)
        count = count +1
    return count
    
def remove (inx, lst):
    value = lst[inx]
    lst.pop(inx)
    check(value, lst)
    return lst
    
def check(value, lst):
    if (value+1) in lst:
        remove(lst.index(value+1), lst)
    elif (value-1) in lst:
        remove(lst.index(value-1), lst)
    else:
        return lst
        
def generateArr():
    arr  = input("Enter the elements of array separated by whitespace: \n")
    splt = arr.split(" ")
    print(splt)
    print(removeElem(splt))
    
generateArr()
