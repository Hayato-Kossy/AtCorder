N = int(input())
mountain = []

for i in range(N):
    S, T = map(str, input().split())
    mountain.append([int(T), S])

mountain.sort(reverse=True)
print(mountain[1][1])