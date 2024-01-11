Heap sort algorithm to find descending order elements of the array
def theHeap_sort(arr):
    n = len(arr)
    output = [0] * n

    # Copy the input array to the output array
    for l in range(n):
        output[l] = arr[l]

    # Sort the output array using heap sort
    for l in range(n):
        for m in range(l + 1, n):
            if output[l] < output[m]:
                temper = output[l]
                output[l] = output[m]
                output[m] = temper

    # Create a new array to store the result
    result = []
    for l in range(n):
        # Find the index of the current element in the input array
        # and add 1 to get the rank of the element
        result.append(output.index(arr[l]) + 1)

    return result
# Test code
arr = [11, 13, 18, 15, 9, 4, 23]
result = theHeap_sort (arr)
print(result)
