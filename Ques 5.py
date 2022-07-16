def selectionsort(arr):
    n= len(arr)
    for i in range(n):
        minimum=i
        for j in range(i+1,n):
            if(arr[j]<arr[minimum]):
                minimum=j
        (arr[i],arr[minimum])= (arr[minimum],arr[i])
            
    return arr

def binarySearch(nums, target, searchFirst):
    (left, right) = (0, len(nums) - 1)
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            result = mid         
            if searchFirst:
                right = mid - 1
            else:
                left = mid + 1
 
        elif target < nums[mid]:
            right = mid - 1
       
        else:
            left = mid + 1
    return result
 
nums = [4,5,2,4,5,6,2,3,4,5,7]
target = 5
z= selectionsort(nums)
print(z)
first = binarySearch(z, target, True)        # pass true for the first occurrence
last = binarySearch(z, target, False)        # pass false for the last occurrence
 
count = last - first + 1
if first != -1:
    print(f'Element {target} occurs {count} times')
else:
    print('Element found not in the list')
 
 
