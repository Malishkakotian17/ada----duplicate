def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # swap
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Step 1: Start from first element.
# Step 2: Assume it is smallest.
# Step 3: Compare with next elements.
# Step 4: Find smallest value.
# Step 5: Note its position.
# Step 6: Swap with first unsorted element.
# Step 7: Move to next index.
# Step 8: Repeat for remaining elements.
# Step 9: Continue till last element.
# Step 10: Array becomes sorted. 