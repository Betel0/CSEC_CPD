username = input().lower()
value = len(set(username))
if value % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
