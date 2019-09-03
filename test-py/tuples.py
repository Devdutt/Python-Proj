# Lists
# Dictionaries
# Tuples (are like lists which as non-changable)
# tuples have () brackets
# Tuples like Strings are immutable

# t = tuple()

(a, b) = ("jack", 4)
print(b)

d = {"h": 10, "b": 19, "c": 20, "g": 10}
a_list = list()
t = sorted(d.items())
# t = d.items()
for i, j in t:
    a_list.append((j, i))
print(a_list)

a_list.sort(reverse=True)

print(a_list)
