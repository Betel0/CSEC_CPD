n = int(input())

count = 0

for _ in range(n):
    values = input().split()
    
    a = int(values[0])
    b = int(values[1])
    c = int(values[2])
    
    if a + b + c >= 2:
        count += 1

print(count)
