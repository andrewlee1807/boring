def binarySearch(low, high):
    # mid = (low + high) // 2
    print(low, high)
    mid = int(low + (high - low) * (k - a[low]) / (a[high] - a[low])) 
    print(mid)
    if a[mid] == k:
        return mid
    if low == high:
        return -1
    if a[mid] > k:
        return binarySearch(low, mid-1)
    if a[mid] < k: 
        return binarySearch(mid+1, high)

a = list(range(10))
print(a)
k = 5
print(binarySearch(0, len(a)-1))


