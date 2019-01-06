def adjacent(nums):
	for i in range(0,len(nums)-2):
		if nums[i]==nums[i+1]:
			return True
print(adjacent([1,2,3,4,5,6]))