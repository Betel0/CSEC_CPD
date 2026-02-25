n = int(input())

groups = 1  # first magnet always makes one group
previous = input()

for _ in range(n - 1):
    current = input()
    if current != previous:
        groups += 1
    previous = current

print(groups)

