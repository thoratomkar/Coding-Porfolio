def spy(nums):
	i=0
	counter=0
	
	for i in range(len(nums)-3):
		
		if (nums[i]==0 and nums[i+1]==0) and (nums[i+2]==7):
			counter=counter+1
			return True
			
	if counter==0:
		return False
			


print(spy([1,2,4,0,0,7,5]))