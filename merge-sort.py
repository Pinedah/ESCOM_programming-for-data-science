#! python3
# merge-sort.py - Merge Sort

def merge_sort(arr):
    if len(arr) > 1:
        # Find the middle of the array
        mid = len(arr) // 2
        
        # Divide the array elements into two halves
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        # Recursively sort the two halves
        merge_sort(left_half)
        merge_sort(right_half)
        
        # Merge the sorted halves
        merge(arr, left_half, right_half)

def merge(arr, left_half, right_half):
    i = j = k = 0
    
    # Merge the two halves into arr
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1
    
    # Check if any element was left in left_half
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1
    
    # Check if any element was left in right_half
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print("Sorted array:", arr)
