def max_value(nums):
  largest = nums[0]
  for i in nums:
      if i > largest:
         largest = i
  return largest

    

print(max_value([4, 7, 2, 8, 10, 9]))
print(max_value([10, 5, 40, 40.3]))
print(max_value([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(max_value([42]))
print(max_value([1000, 8, 9000]))
print(max_value([1000, 8]))
print(max_value([2, 5, 1, 1, 4]))
