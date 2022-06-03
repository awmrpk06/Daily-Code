def Sum_subset(arr):
    s = sum(arr)
    arr.sort(reverse=True)
    if s % 2 == 0:
       if SumUp(arr,s/2):
            if SumUp(arr,s/2,[]):
                return True
    return False
def SumUp(S, k, sub = []):
    if len(S) > 0:
        d = k - S[0]
        if d < 0 :
            S.pop(0)
            return SumUp(S, k, sub)
        elif d == 0:
            sub.append(S.pop(0))
            print(sub)
            return sub
        else:
            while(len(S) > 0):
                k = d
                sub.append(S.pop(0))
                result = SumUp(S, k, sub)
                if result != False:
                    return result
                else:
                    sub.pop(0)
                   # sub.append(S.pop(0))
                # result = SumUp(S, k, sub)
    return False
print( Sum_subset([15, 5, 20, 10, 35]) )