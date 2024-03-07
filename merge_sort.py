def merge_sort(arr):
    # Check if the array has more than one element; if not, it's already sorted.
    if len(arr) > 1:
        # Find the middle index of the array to split it into two halves.
        mid = len(arr) // 2
        # Divide the array elements into two halves: left (L) and right (R).
        L = arr[:mid]
        R = arr[mid:]

        # Recursively sort the first half of the array.
        merge_sort(L)
        # Recursively sort the second half of the array.
        merge_sort(R)

        # Initialize pointers for the current index of L, R, and arr.
        i = j = k = 0

        # Merge the two halves back into arr in sorted order.
        while i < len(L) and j < len(R):
            # Compare the current elements of L and R.
            # If L's element is smaller, place it in the current position of arr.
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1  # Move to the next element in L.
            else:
                # If R's element is smaller or equal, place it in the current position of arr.
                arr[k] = R[j]
                j += 1  # Move to the next element in R.
            k += 1  # Move to the next position in arr.

        # After the main loop, one of the subarrays may have elements left.
        # This line appends any remaining elements from L or R to arr.
        # Since L and R are already sorted, appending the leftovers maintains the sorted order.
        arr[k:] = L[i:] + R[j:]

    # Once the entire array is sorted, return it.
    return arr


# Example usage of the merge_sort function.
print(merge_sort([1, 2, 8, 6, 3, 0, 3, 7, 10, 19, 11, 15, 12, 13]))
