def findPeak(arr, start, end, peak):
    if start <= end:
        mid = (start + end) /2
        mid = int(mid)
        if arr[mid] > arr[mid + 1]:
            if arr[mid] > peak:
                peak = arr[mid]
            end = mid - 1 
        else :
            start = mid + 1
        return findPeak(arr, start, end, peak)
    else: 
     #   print(peak)
        return peak
arr = [1, 3, 7, 5, 2, 0]
m_peak = findPeak(arr, 0, len(arr) - 1, 0)
print(m_peak)