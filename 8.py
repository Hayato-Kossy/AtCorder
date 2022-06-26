N, K = 314, 2
def get_min(x):
    x = str(x)
    x = list(x)
    x.sort()
    x = "".join(x)

    return int(x)

def get_max(x):
    x = str(x)
    x = list(x)
    x.sort(reverse=True)
    x = "".join(x)

    return int(x)

def calculation(target):
    return get_max(target) - get_min(target) 

a = N

for i in range(K):
    a = calculation(a)

print(a)
print(get_max(314))