def compare_strings(a, b):
    if a is None or b is None:
        return 0
        
    size = min(len(a), len(b)) # Finding the minimum length
    count = 0 # A counter to keep track of same characters

    for i in range(size):
        if a[i] == b[i]:
            count += 1
        else:
            break
    return count
def Ghost_game(dict):
    w_word = []
    l_word = []
    for x in dict:
        if len(x) % 2 == 0:
            w_word.append(x)
        else:
            l_word.append(x)
    for w in w_word:
        for l in l_word:
            if (compare_strings(w,l) + 1 ) % 2 :
                w_word.remove(w)
                break
    return w_word
print(Ghost_game(["cat", "calf", "dog", "bear", "bar"]))