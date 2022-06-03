def find_element(arr):
    check_arr = [0]*100
    for i, v in enumerate(arr):
        check_arr[v] += 1
    list_1 = []
    for i, v in enumerate(check_arr):
        if v == 1: 
            list_1.append(i)
    return list_1

print(find_element([2, 4, 6, 8, 10, 2, 6, 10]))