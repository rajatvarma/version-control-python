a = input("enter a string value: ")

print("Duplicate characters in a given string: ")

x = []

for i in a:
    if i not in x: x.append(i)

for i in x:
    if a.count(i) > 1:
        print(i, a.count(i))