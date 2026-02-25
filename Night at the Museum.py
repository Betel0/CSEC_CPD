s = input().strip()

current = 'a'
total = 0

for ch in s:
    pos1 = ord(current) - ord('a')
    pos2 = ord(ch) - ord('a')
    
    diff = abs(pos1 - pos2)
    total += min(diff, 26 - diff)
    
    current = ch

print(total)
