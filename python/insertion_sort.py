def insertion_sort(arr):
    """
    Perform insertion sort on a given list.
    
    Args:
    arr (list): The list to be sorted.
    
    Returns:
    list: The sorted list.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def main():
    # Input list to be sorted
    input_list = [12, 11, 13, 5, 6]
    
    # Call the insertion_sort function
    sorted_list = insertion_sort(input_list)
    
    # Print the sorted list
    print("Sorted list:", sorted_list)

if __name__ == "__main__":
    main()
