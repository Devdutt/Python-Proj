file_handle = open("../data/junk-data.txt", "r")

for lns in file_handle:
    lns = lns.rstrip()
    if not "ads" in lns:
        continue
    print(lns)
