def palindrome(arr):
    result = []
    for i in range(len(arr) - 1):
        for j in range(i, len(arr)):
            check1 = isPalindrome(arr[i] + arr[j])
            check2 = isPalindrome(arr[j] + arr[i])
            if(check1):
                result.append([i,j])
            if(check2):
                result.append([j,i])
    return result
        
def isPalindrome(s):
    return s == s[::-1] 
print(palindrome(["code", "edoc", "da", "d"]))