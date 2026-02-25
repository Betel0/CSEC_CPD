a = input().split()

a1 = int(a[0])
a2 = int(a[1])
a3 = int(a[2])
a4 = int(a[3])

s = input().strip()

total = 0

for ch in s:
    if ch == '1':
        total += a1
    elif ch == '2':
        total += a2
    elif ch == '3':
        total += a3
    elif ch == '4':
        total += a4

print(total)
