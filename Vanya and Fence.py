n_h = input().split()
n = int(n_h[0])
h = int(n_h[1])

heights_input = input().split()

width = 0

for i in range(n):
    height = int(heights_input[i])
    
    if height > h:
        width += 2
    else:
        width += 1

print(width)
