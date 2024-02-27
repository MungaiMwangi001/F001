def merge_sort(array):
    # create a base case that stops the function execution when
    # the length of array is less than or equal to 1. This base case will stop the recursion call. 
    #Without it, the merge sort operation would continue to 
    #run even when the list has been sorted or has no element in it.
    if len(array) <= 1:
        return
    
    middle_point = len(array) // 2
    left_part = array[:middle_point]
    right_part = array[middle_point:]

    merge_sort(left_part)
    merge_sort(right_part)

    left_array_index = 0
    right_array_index = 0
    sorted_index = 0

    while left_array_index < len(left_part) and right_array_index < len(right_part):
        #checks if the index of left_part is less than the index of right_part.
        if left_part[left_array_index] < right_part[right_array_index]:
            #if condition evaluates to True, it means that the element in the left_part
            # list is smaller than the element it is being compared to in the right_part list            
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1
        else:
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1
        sorted_index += 1

    while left_array_index < len(left_part):#copy the remaining elements in left_part
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1
    
    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1

'''
You can use the __name__ variable to determine if a Python script is being run as 
the main program or if it is being imported as a module.
If the value of __name__ is set to '__main__', it implies that
 the current script is the main program, and not a module.
'''

if __name__ == '__main__':
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    print('Unsorted array: ')
    print(numbers)
    merge_sort(numbers)
    print('Sorted array: ' + str(numbers ))