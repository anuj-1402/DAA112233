def insertion_sort(arr):
    """
    Perform Insertion Sort on the input array.
    It builds the sorted array one item at a time.
    """
    for i in range(1, len(arr)):
        key = arr[i]  # The element to be inserted
        j = i - 1  # The index of the element before the key

        # Move elements of arr[0..i-1], that are greater than key, one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key  # Place the key at the correct position

    return arr

# Test case for Insertion Sort
arr_insertion = [12, 11, 13, 5, 6]
print("Insertion Sort Result:", insertion_sort(arr_insertion))
