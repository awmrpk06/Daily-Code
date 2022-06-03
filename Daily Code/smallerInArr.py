def solve(arr):
    org_arr = arr.copy()
    arr.sort()
    result = []
    for i in range(len(arr)):
        result.append( arr.index(org_arr[i]) )
        arr.remove(org_arr[i])
    return result
print( solve([3, 4, 9, 6, 1]) )