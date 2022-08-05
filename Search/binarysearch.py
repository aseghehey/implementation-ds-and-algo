def iterative(array, target):
    left,right = 0, len(array)-1
    while left <= right:
        middle = (left+right)//2
        if array[middle] == target:
            return True
        else:
            if array[middle] > target:
                right = middle-1
            else:
                left = middle+1
    return False

# Recursive implementation
def recursive(array, target):
    if len(array) == 0:
        return False
    middle = len(array)//2
    if array[middle] == target:
        return True
    else:
        if array[middle] < target:
            return recursive(array[middle+1:], target)
        else:
            return recursive(array[:middle], target)


def main():
    arr = [1,2,4,10,122]
    print(recursive(arr,10))
main()