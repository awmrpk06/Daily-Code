from tabnanny import check


def longestPortion(arr):   
    count = 0
    longest_count = 0
    longest_pair = []
    checking_pair = [arr[0]]
    stack_count = 0
    for i in range (1, len(arr) ):
        if arr[i] not in checking_pair:
            if len(checking_pair) == 2:
                if longest_count < count:
                    longest_count = count 
                    longest_pair = checking_pair.copy()
                count = stack_count
                stack_count = 0
                checking_pair.pop(0)

            checking_pair.append(arr[i])
            
        else:
            count += 1
            if arr[i] == checking_pair[1] :
                stack_count += 1
            if len(checking_pair) == 2:
                if arr[i] == checking_pair[0]:
                    checking_pair[0], checking_pair[1] = checking_pair[1], checking_pair[0]
    return longest_count, longest_pair
                


            
  
print(longestPortion([2, 1, 1, 3, 3, 3 , 1 ,4, 3 ,5]))