#there are 3 different ways to solve this problem
#1. brute force
#2. hash table
#3. sort and two pointers
#the time complexity of brute force is O(n^2), space complexity is O(1)
#the time complexity of hash table is O(n), space complexity is O(n)
#the time complexity of sort and two pointers is O(nlogn), space complexity is O(1)
#the best solution is hash table

#brute force
values = [1,-1,5,-4,8,1,11,3,6]
def twosum1(nums, target):
  for i in range(len(nums)-1):
    for j in range(i+1, len(nums)):
      if nums[i] + nums[j] == target:
        return [nums[i], nums[j]]
      

#hash table
def twosum2(nums, target):
  dict = {}
  for i in range(len(nums)):
    expected_value = target - nums[i]
    if(expected_value in dict):
      return [nums[i], expected_value]
    else:
      dict[nums[i]] = True


#sort and two pointers
def twosum3(nums, target):
  nums.sort()
  left = 0
  right = len(nums)-1
  while(left < right):
    sum = nums[left] + nums[right]
    if(sum == target):
      return [nums[left], nums[right]]
    elif(sum < target):
      left += 1
    else:
      right -= 1







print(twosum1(values, 10))
print(twosum2(values, 10))
print(twosum3(values, 10))