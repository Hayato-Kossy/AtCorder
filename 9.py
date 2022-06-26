N = 20

def get_8(target):
    ans = ""
    while target > 0:
        ans = str(target % 8) + ans
        target //= 8

    return ans

def main():
    times = N + 1
    inc_7 = 0
    target = ""
    for i in range(times):
        target = get_8(i)
        if '7' in target or '7' in str(i):
            inc_7 += 1
    
    return N - inc_7

print(main())