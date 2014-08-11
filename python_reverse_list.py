#### How to reverse a list in Python


ls = [2,1,3,5,4]

def rev(lst):
    if lst: # list is not empty
        return rev(lst[1:])+[lst[0]]
    else:   # list is empty
        return []
    print rev

rev(ls)
