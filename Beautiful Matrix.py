row_position = 0
col_position = 0

for i in range(5):
    values = input().split()
    
    for j in range(5):
        if values[j] == '1':
            row_position = i + 1
            col_position = j + 1

moves = abs(row_position - 3) + abs(col_position - 3)

print(moves)
