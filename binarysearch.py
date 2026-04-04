def binarysearch(List, target):
    if len(List) == 0:
        return -1  

    mid = len(List) // 2

    if List[mid] == target:
        return mid

    elif target < List[mid]:
        return binarysearch(List[:mid], target)

    else:
        res = binarysearch(List[mid+1:], target)
        if res == -1:
            return -1
        return mid + 1 + res

List = list(map(int, input("Enter numbers separated by comma: ").split(',')))
target=int(input("Enter the target: "))
List.sort()
print(f"Index of target in sorted list is {binarysearch(List,target)}")