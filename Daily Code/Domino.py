def Domino(arr, i):
    if(i == len(arr)):
        return arr
    end_index = i
    if arr[i] == 'L':
         for z in range (i-1, -1 , -1):
             if arr[z] != '.':
                 break
             else:
                 arr[z] = 'L'
    elif arr[i] == 'R':
        for z in range(i+1, len(arr)):
            if arr[z] == 'L':
                mid =  (i+z)/2
                if(mid.is_integer()):
                    mid = int(mid)
                    arr[mid] = '.'
                else:
                    mid = int(mid)
                mid = mid + 1
                for k in range (mid, z):
                    arr[k] = 'L'
                end_index = z
                break
            else :
                arr[z] = "R" 
    return Domino(arr, end_index + 1 )
arr = "R.L.R...L..L"
listarr = list(arr)
print(listarr)
print(Domino(listarr,0))
