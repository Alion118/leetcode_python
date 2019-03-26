
def sol(n, x, y):
	dist = [float('Inf') for _ in range(n)]
	for i in range(n):
		for j in range(n):
			t = 0
			tmp = []
			for k in range(n):
				tmp.append(abs(x[i] - x[k]) + abs(y[j] - y[k]))
			tmp.sort()
			for k in range(n):
				t += tmp[k]
				dist[k] = min(dist[k], t)
	return dist


n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
# print(sol(n, x, y))
print(' '.join(map(str, sol(n, x, y))))