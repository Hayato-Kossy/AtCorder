N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
def main():
    naiseki = 0
    for i in range(N):
        naiseki += A[i] * B[i]

    return "Yes" if naiseki == 0 else "No"

print(main())

