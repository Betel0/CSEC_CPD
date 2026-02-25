
word = input()
upper_count = 0
for ch in word:
    if ch.isupper():
        upper_count += 1
lower_count = len(word) - upper_count
if upper_count > lower_count:
    print(word.upper())
else:
    print(word.lower())
