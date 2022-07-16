# Python code to remove duplicate elements
def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
     
def selectionsort(arr):
    n= len(arr)
    for i in range(n):
        minimum=i
        for j in range(i+1,n):
            if(arr[j]<arr[minimum]):
                minimum=j
        (arr[i],arr[minimum])= (arr[minimum],arr[i])
            
    return arr


def bubble_sort(arr):
    n=len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                swapped = True
                arr[j],arr[j+1] = arr[j+1],arr[j]
        if not swapped:
            return arr

arr=[4,5,2,4,5,2,6,3,6,4,5,7]
x=Remove(arr)
print(x)
y= selectionsort(x)
print(y)

z = bubble_sort(x)
print(z)
