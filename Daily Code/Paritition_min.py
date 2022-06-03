def Partition_min(n, k):
    n.sort(reverse=True)
    p =[]
    for i in range(k):
        p.append([0])
    p[0].append(n.pop(0))
    while(len(n) > 0 ):
        min_sum = sum(p[0])
        j = 0
        for i in range(len(p)):
            if min_sum > sum(p[i]):
                j = i
                min_sum = sum(p[i])
        p[j].append(n.pop(0))
    return p
print(Partition_min([12, 1, 2, 19, 3, 4], 3))



# N = [12, 1, 2, 19, 3, 4]