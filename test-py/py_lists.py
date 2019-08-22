alist = list()
someNumbers = input("Type a number:")

while someNumbers != "done":
    someNumbers = int(someNumbers)
    alist.append(someNumbers)
    someNumbers = input("Type a number:")
    continue
averageNumber = sum(alist) / len(alist)
print("The average number is: ", averageNumber)
