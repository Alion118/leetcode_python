n=int(input())

m1=[i for i in map(int, input().split())]
m2=[i for i in map(int, input().split())]
m3=[i for i in map(int, input().split())]

out=[m1[1],m2[1],m3[1]]

while sum(out)>n:
	if out[2]>m3[0]:
		out[2]-=1
		continue
	if out[1]>m2[0]:
		out[1]-=1
		continue
	if out[0]>m1[0]:
		out[0]-=1
		continue

print(out[0],end=' ')
print(out[1],end=' ')
print(out[2])
