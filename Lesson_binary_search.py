def binarysearch(mylist, look_for, start, stop):
    if start > stop:
        return False
    else:
        mid = (start + stop) // 2
        if look_for == mylist[mid]:
            return mid
        elif look_for < mylist[mid]:
            return binarysearch(mylist, look_for, start, mid - 1)
        else:
            return binarysearch(mylist, look_for, mid + 1, stop)

mylist = [10, 12, 13, 33, 55, 56, 76, 78, 98, 101]
look_for = 56
start = 0
stop = len(mylist)
x = binarysearch(mylist, look_for, 0, len(mylist))

if x == False:
    print("Item", look_for, "Not Found!")
else:
    print("Item", look_for, "Found at Index", x)
