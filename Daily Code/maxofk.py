def Maxofk(arr, k):
    count = 0
    num_max = 0
    second_max = 0
    maxofk = []
    for i in range(0, len(arr)):
        count += 1
        if num_max < arr[i]:
            num_max = arr[i]
        elif second_max < arr[i]:
            second_max = arr[i]
        if(count == k  ):
            maxofk.append(num_max)
            if arr[i - count + 1] == num_max:
                num_max = second_max
                second_max = 0
            count = k - 1 
    return maxofk
print(Maxofk([10, 5, 2, 7, 9, 5, 6], 3))