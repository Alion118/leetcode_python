n=int(input())
nums=[i for i in map(int,input().split())]

nums.sort()

max_val=0

i=0
while i<len(nums) and nums[i]<0:
	max_val-=nums[i]
	i+=1

if i==len(nums) and i>1:
	max_val+=nums[-1]*2
else:
	temp = nums[i]
	if i < len(nums) - 1:
		temp=sum(nums[i+1:])-nums[i]
	max_val += temp

print(max_val)

