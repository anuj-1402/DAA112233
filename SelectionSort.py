def selection_sort(arr):
    """
    Perform Selection Sort on the input array.
    It repeatedly selects the minimum element and places it at the correct position.
    """
    for i in range(len(arr)):
        # Find the minimum element in the unsorted part of the array
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

# Test case for Selection Sort
arr_selection = [64, 25, 12, 22, 11]
print("Selection Sort Result:", selection_sort(arr_selection))
