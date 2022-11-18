# Python3 implementation of QuickSort


# Function to find the partition position
def partition(array, left, right):

  # Choose the rightmost element as pivot
  pivot = array[right]

  # Pointer for greater element
  i = left - 1

  # Traverse through all elements
  # compare each element with pivot
  for j in range(left, right):
    if array[j] <= pivot:
      # If element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1

      # Swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])

  # Swap the pivot element with
  # e greater element specified by i
  (array[i + 1], array[right]) = (array[right], array[i + 1])

  # Return the position from where partition is done
  return i + 1


# Function to perform quicksort


def quick_sort(array, left, right):
  if left < right:

    # Find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(array, left, right)

    # Recursive call on the left of pivot
    quick_sort(array, left, pi - 1)

    # Recursive call on the right of pivot
    quick_sort(array, pi + 1, right)


# Driver code this is the user input code 
array = []
n = int(input('enter number of elements: '))
for i in range(0, n):
  ele = int(input())
  array.append(ele)
print(array)

# The above code is how to take a list as an user input in a code 

quick_sort(array, 0, len(array) - 1)

print(f'Sorted array: {array}')

# This code is contributed by Rohit Kumar
