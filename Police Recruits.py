n = int(input())
events = input().split()

available = 0
untreated = 0

for i in range(n):
    event = int(events[i])
    
    if event == -1:
        if available > 0:
            available -= 1
        else:
            untreated += 1
    else:
        available += event

print(untreated)
