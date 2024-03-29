# Most commonly used words in the data file

file_handle = open("../data/junk-data-3.txt", "r")
""" 
for lns in file_handle:
    lns = lns.rstrip()
    if not "-a" in lns:
        continue
    print(lns) """

counts = dict()
for line in file_handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
print("+++++++++++++++++++++++++++++++")

print(type(words))

print("+++++++++++++++++++++++++++++++")

a_list = list()

for k, v in counts.items():
    a_list.append((v, k))

a_list.sort(reverse=True)

for v, k in a_list[:20]:
    print(k, v)

