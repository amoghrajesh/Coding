def bs(arr, target, l, r):
    n = len(arr)
    while l<r:
        m = l + (r-l)//2
        if arr[m] == target:
            return arr[m]
        
        if arr[m] > target:
            if m>0 and target > arr[m-1]:
                if target - arr[m-1] >= arr[m] - target:
                    return arr[m] - target
                else:
                    return target - arr[m-1]
                r = m
        else:
            if m < n - 1 and target < arr[m+1]:
                if arr[m+1] - target >= target - arr[m]:
                    return target - arr[m]
                else:
                    return arr[m+1] - target
                l = m + 1
    return arr[m]


arr1 = [2,1,100,3]
arr2 = [-5,-2,10,-3,7]
d = 6

ans = 0
arr2.sort()
l = 0
r = len(arr2)
for i in arr1:

    closest = bs(arr2, i, l, r)
    if abs(i-closest) > d:
        ans+=1

print(ans)
     

