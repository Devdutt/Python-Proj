file_handle = open("../data/junk-data-3.txt", "r")
counts = dict()
for line in file_handle:
    words = line.split()
    for word in words:
        print(word)
        counts[word] = counts.get(word, 0) + 1
print(counts)
print("+++++++++++++++++++++++++++++++")

print(type(words))

print("+++++++++++++++++++++++++++++++")

a_list = list()

for k, v in counts.items():
    a_list.append((v, k))
print(a_list)
a_list.sort(reverse=True)

for i in a_list[:20]:
    print(i)
