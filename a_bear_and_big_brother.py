inp = input().split()
a= int(inp[0])
b = int(inp[1])
ans = 0
while a <= b:
    a *= 3
    b *= 2
    ans += 1

print(ans)
