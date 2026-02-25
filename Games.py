n = int(input())

home = []
guest = []

for _ in range(n):
    data = input().split()
    h = int(data[0])
    g = int(data[1])
    home.append(h)
    guest.append(g)

count = 0

for i in range(n):
    for j in range(n):
        if i != j and home[i] == guest[j]:
            count += 1

print(count)
