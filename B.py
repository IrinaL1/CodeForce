t = int(input())

for j in range(t):
    l, r = map(int, input().split())
    s = int(l**0.5)
    e = int(r**0.5)
    answ = 0
    if s != e:
        answ += (e - s - 1) * 3
        if (l == s**2):
            answ += 3
        elif (l <= s**2 + s):
            answ += 2
        elif (l <= s**2 + 2*s):
            answ += 1
        if (r < e**2 + e):
            answ += 1
        elif (r < e**2 + 2*e):
            answ += 2
        elif (r >= e**2 + 2*e):
            answ += 3
    else:
        if l == s**2 and s**2 <= r:
            answ += 1
        if l <= s**2 + s and s**2 + s <= r:
            answ += 1
        if l <= s**2 + 2 * s and s**2 + 2*s <= r:
            answ += 1
    print(answ)



