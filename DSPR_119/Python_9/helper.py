from re import M


def between_min_max(*nums):
   for n in nums:
      max = nums[0]
      if n>max:
         max = n
   for m in nums:
      min = nums[0]
      if m<min:
         min = m
   return (max+min)/2

print(between_min_max(10))
print(between_min_max(1,2,3,4,5))
         