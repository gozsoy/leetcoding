import random


def merge_sort(arr):

    if len(arr) <= 1:
        return arr
    else:
        split_idx = len(arr)//2

        arr1 = arr[:split_idx]
        arr2 = arr[split_idx:]

        arr1 = merge_sort(arr1)
        arr2 = merge_sort(arr2)

        l, r, idx = 0, 0, 0

        while True:

            if len(arr1) > l and len(arr2) > r:

                if arr1[l] <= arr2[r]:
                    arr[idx] = arr1[l]
                    l += 1
                else:
                    arr[idx] = arr2[r]
                    r += 1
                idx += 1
            
            elif len(arr1) > l:
                arr[idx:] = arr1[l:]
                break

            elif len(arr2) > r:
                arr[idx:] = arr2[r:]
                break
        
        return arr


# constant swapping until sorted.
def bubble_sort(arr):

    while True:

        swapped = False

        for idx in range(1, len(arr)):

            if arr[idx] < arr[idx-1]:
                temp = arr[idx-1]
                arr[idx-1] = arr[idx]
                arr[idx] = temp
                swapped = True
        
        if not swapped:
            break
    
    return arr


# sorted-unsorted regions. at each iteration, find min of unsorted region. 
# and put as the last elem of sorted region.
def selection_sort(arr):

    for i in range(len(arr)):

        min_idx = -1
        min_val = float('inf')

        for j in range(i, len(arr)):
            if arr[j] < min_val:
                min_val = arr[j]
                min_idx = j
        
        temp = arr[i]
        arr[i] = arr[min_idx]
        arr[min_idx] = temp
    
    return arr


# sorted-unsorted regions.
# find place for the next unsorted elem in the sorted region.
def insertion_sort(arr):

    for j in range(1, len(arr)):

        for i in range(j, 0, -1):

            if arr[i] < arr[i-1]:
                temp = arr[i]
                arr[i] = arr[i-1]
                arr[i-1] = temp
            else:
                break

    return arr


def quick_sort(arr):

    if len(arr) <= 1:
        return arr
    else:

        pivot_idx = random.randrange(len(arr))
        pivot_el = arr[pivot_idx]
        l_arr = []
        r_arr = []

        for idx in range(len(arr)):
            curr_el = arr[idx]

            if idx != pivot_idx:
                if curr_el >= pivot_el:
                    r_arr.append(arr[idx])
                else:
                    l_arr.append(arr[idx])
        
        l_arr = quick_sort(l_arr)
        r_arr = quick_sort(r_arr)

        return l_arr + [pivot_el] + r_arr