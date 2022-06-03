def permutation(arr_per, arr):
    rep_arr = arr.copy()
    for i, v in enumerate(arr_per):
        arr[i] = rep_arr[v]
    return arr
arr_per = [2,3,0,1]
arr = ["a", "b", "c","d"]
print(permutation(arr_per,arr))