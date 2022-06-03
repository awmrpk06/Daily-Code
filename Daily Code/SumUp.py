def SumUp(S, k, sub = []):
    if len(S) > 0:
        d = k - S[0]
        if d < 0 :
            S.pop(0)
            return SumUp(S, k, sub)
        elif d == 0:
            sub.append(S.pop(0))
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
S = [12, 1, 61, 5, 9, 2]
S.sort(reverse=True)
print(SumUp( S, 63, []))


