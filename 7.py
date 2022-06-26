H, W, X, Y = map(int, input().split())

field = []
for i in range(H):
    S = input()
    S = list(S)

    field.append(S)

ans = 0

for i in range(1, H):
    if 0 <= X - i < H:
        if field[X - i][Y] == "#":
            break
        else:
            ans += 1

for i in range(1, H):
    if 0 <= X + i < H:
        if field[X + i][Y] == "#":
            break
        else:
            ans += 1

for i in range(1, H):
    if 0 <= Y - i < H:
        if field[X][Y - i] == "#":
            break
        else:
            ans += 1

for i in range(1, H):
    if 0 <= Y - i < H:
        if field[X][Y - i] == "#":
            break
        else:
            ans += 1

print(ans)