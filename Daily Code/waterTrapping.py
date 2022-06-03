def waterTraping(arr, unit):
    forward = True
    if(len(arr) <= 1):
         return unit
    if min(arr[0], arr[len(arr) - 1]) == arr[len(arr) - 1]:
        forward = False
    if(forward):
        lower = arr[0]
        for i in range(1 , len(arr)):
            if arr[i] > lower:
                return waterTraping(arr[ i : len(arr)], unit)
            else:
                unit = unit + lower - arr[i]
    else:   
        lower = arr[len(arr) - 1]
        for i in range(len(arr) - 1 , -1, -1 ):
            if arr[i] > lower:
                return waterTraping(arr[ 0 : i + 1 ], unit)
            else:
                unit = unit + lower - arr[i]

print(waterTraping( [3, 0, 1, 3, 0, 5] , 0))