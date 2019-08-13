file_handle = open("../data/junk-data.txt", "r")
data_dump = file_handle.read()
count = 0
for lines in file_handle:
    count = count + lines
print("Number of lines in the data file: ", count)
print("Is the file closed? ", file_handle.closed)
# print(data_dump)
