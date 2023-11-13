# There are two solutions 
# Solution 1: calculate the squared value of each element in the array, then sort the array. Time complexity is O(nlogn), space complexity is O(n)

array = [-4, 1, 10, 5, -2, 7, -3]
def sortedSquare1(values):
  for i in range(len(values)):
    values[i] = values[i] * values[i]
  values.sort()
  return values


# Solution 2: using two pointers, one for the left side of the array and one for the right side of the array. Time complexity is O(n), space complexity is O(n)
def sortedSquare2(values):
  values.sort()
  left = 0
  right = len(values) - 1
  result = [0] * len(values)
  index = len(values) - 1

  while(left <= right):
    if(abs(values[left]) > abs(values[right])):
      result[index] = values[left] * values[left]
      left += 1
    else:
      result[index] = values[right] * values[right]
      right -= 1
    index -= 1
  return result


print(sortedSquare1(array))
print(sortedSquare2(array))