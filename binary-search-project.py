
import time
import random

# In these two examples, numList is a list in ascending order, and target is something that we're looking for:
# Return -1 if not found


# Linear Search: scan entire list and ask if its equal to the target.
# If Yes, return the index
# If No, then return -1

def linearSearch(numList, target):
    # example numList = [1, 2, 9, 11]
    for index in range(len(numList)):
        if numList[index] == target:
            return index
    return -1

# Binary Search uses Divide & Conquer!
# We will leverage the fact that our list is already SORTED.

def binarySearch(numList, target, start = None, end = None):
    if start is None:
        start = 0
    if end is None:
        end = len(numList) - 1

    if end < start:
        return -1
    
    # Example numList = [1, 2, 4, 9, 11]  # should return 2
    midpoint = (start + end) // 2  # 2

    # We'll check if numList[midpoint] == target, and if not, we can find out if
    # target will be to the left or right of midpoint
    # We know everything to the left of midpoint is smaller than the midpoint
    # and everything to the right is larger
    if numList[midpoint] == target:
        return midpoint
    elif target < numList[midpoint]:
        return binarySearch(numList, target, start, midpoint-1)
    else:
        # target > numList[midpoint]
        return binarySearch(numList, target, midpoint+1, end)


if __name__=='__main__':
    # numberList = [1, 2, 4, 9, 11]
    # target = 9
    # print(linearSearch(numberList, target))
    # print(binarySearch(numberList, target))

    length = 10000
    # build a sorted list of length 10000
    sortedList = set()
    while len(sortedList) < length:
        sortedList.add(random.randint(-3*length, 3*length)) # range of -30,000 to 30,000
    sortedList = sorted(list(sortedList))

    start = time.time()
    for target in sortedList:
        linearSearch(sortedList, target)
    end = time.time()
    print("Linear search time: ", (end - start), "seconds")

    start = time.time()
    for target in sortedList:
        binarySearch(sortedList, target)
    end = time.time()
    print("Binary search time: ", (end - start), "seconds")



