import sys

fruit = "banana"
l = len(fruit)
print(l)
""" i = 0
while i < l:
    print(fruit[i])
    i = i + 1
 """
count = 0
for letter in fruit:
    if letter == "a":
        count = count + 1

print("a appears:", count, "times.")
print(fruit[0:3])
print(fruit[1:])
print(fruit[:4])

logical = "a" in fruit
print(logical)
