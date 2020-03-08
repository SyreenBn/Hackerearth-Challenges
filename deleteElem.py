import random

def removeElem (arr):
    lst = list(arr)
    count = 0
    while(lst != []):
        r = random.randint(0, len(lst)-1)
        lst = remove(r, lst)
        count = count +1
    return count
    
def remove (inx, lst):
    value = lst[inx]
    lst.pop(inx)
    check(int(value), lst)
    return lst
    
def check(value, lst):
    if str(value+1) in lst:
        remove(lst.index(str(value+1)), lst)
    elif str(value-1) in lst:
        remove(lst.index(str(value-1)), lst)
    else:
        return lst
        

def generateArr():
    lst  = input("Enter the elements of array separated by whitespace: \n")
    splt = lst.split(" ")
    print(removeElem(splt))

generateArr()
    
#lst = [291, 292, 295, 297, 298, 299]
#print(removeElem(lst))
