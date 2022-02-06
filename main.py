def binary_search(list, target):
    # first and last are the number positions in the list
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last)//2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None

def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found")   

Values = [10,9,7,5,6,3,1,2,15,26,8]
result = binary_search(Values, 25)
ver = verify(result)
print(ver)
