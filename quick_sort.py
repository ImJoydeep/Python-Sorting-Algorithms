
def sort_func(array, low, high):
    
    def partition(array, low, high):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= pivot:
                i = i + 1
                (array[i], array[j]) = (array[j], array[i])
        (array[i + 1], array[high]) = (array[high], array[i + 1])
        return i + 1
    
    if low < high:
        pi = partition(array, low, high) 
        sort_func(array, low, pi - 1)
        sort_func(array, pi + 1, high)
        
def quickSort(arr):
    low  = 0
    high = len(arr) - 1
    return sort_func(arr, low, high)
 
data = [10,9,8,7,6,5,4,3,2,1,-1,2,-3,0]

# CALLING quickSort Function....
quickSort(data)

print(data)



'''
**********************
*****************************
************************************
'''
# ANOTHER EXAMPLE / SHORTER SYNTEX


def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quickSort(less) + [pivot] + quickSort(greater)


data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5,100000,19999,-178812, -7651,0,-1]
sorted_list = quickSort(data)
print(sorted_list)


