def sum_up(arr, k):
    sum = []
    temp = 0
    count = -1
    for i in range(0, len(arr)):
        temp += arr[i]
        count += 1
        if(count == k - 1 ):
            sum.append(temp)
            temp -= arr[i-count]
            count = 1
    return sum
print(sum_up([10, 5, 2, 7, 8, 7], 3))