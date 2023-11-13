# There are two arrays of integers. The first array is the original array, and the second array is the subsequence.
# Write a function that determines whether the second array is a subsequence of the first array.
# A subsequence of an array is a set of numbers that are not necessarily adjacent in the array but that are in the same order as they appear in the array.
# For example, the numbers [1,3,4] form a subsequence of the array [1,2,3,4], and so do the numbers [2,4].
# Note that a single number in an array and the array itself are both valid subsequences of the array.
# Sample Input:
# array = [5,1,22,25,6,-1,8,10]
# sequence = [1,6,-1,10]
# Sample Output:
# true
#
# Solution:
# Using two pointers, one for the array and one for the sequence.
# If the array pointer and the sequence pointer are pointing at the same value, then move both pointers forward.
# If the array pointer and the sequence pointer are not pointing at the same value, then move only the array pointer forward.
# If the sequence pointer reaches the end of the sequence, then the sequence is a subsequence of the array.
# Time Complexity: O(n)
# Space Complexity: O(1)
#
values = [5,1,22,25,6,-1,8,10]
sub = [1,6,-1,10]

# Solution 1:
# Using two pointers, one for the array and one for the sequence.
def isValidSubsequent1(array, sub):
  arr_pointer = 0
  sub_pointer = 0
  while(arr_pointer < len(array) and sub_pointer < len(sub)):
    if(array[arr_pointer] == sub[sub_pointer]):
      sub_pointer += 1
    arr_pointer += 1
  return sub_pointer == len(sub)

# Solution 2:
# Using one pointer for the array.
def isValidSubsequent2(array, sub):
  sub_pointer = 0
  for value in array:
    if(sub_pointer == len(sub)):
      break
    if(sub[sub_pointer] == value):
      sub_pointer += 1
  return sub_pointer == len(sub)


print(isValidSubsequent1(values, sub))
print(isValidSubsequent2(values, sub))