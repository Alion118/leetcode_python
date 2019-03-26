
s='45 12 45 12 5 6'
nums=[i for i in map(int,s.split())]
n=len(nums)
if nums.count(nums[0])==n:
	print(' '.join([str(n*(n-1)//2),str(n*(n-1)//2)]))
else:
	same_count=1
	same_count_list=[]
	have_same=False
	for i in range(n-1):
		if nums[i]==nums[i+1]:
			same_count+=1
			have_same = True
		else:
			same_count_list.append(same_count)
			same_count=1
	if same_count>1:
		same_count_list.append(same_count)
	min_l=0
	if have_same:
		for each in same_count_list:
			if each>1:
				min_l+=each*(each-1)//2
	else:
		diffs=[abs(nums[i]-nums[i+1]) for i in range(n-1)]
		min_l=diffs.count(min(diffs))
	max_l=nums.count(nums[0])*nums.count(nums[n-1])

	print(' '.join([str(min_l),str(max_l)]))