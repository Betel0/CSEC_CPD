n = int(input())
values = input().split()

numbers = []

for v in values:
    numbers.append(int(v))

numbers.sort()

for num in numbers:
    print(num, end=" ")
