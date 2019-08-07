import sys

fruit = "banana"
l = len(fruit)
print(l)
""" i = 0
while i < l:
    print(fruit[i])
    i = i + 1

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
 """

raw_data = "dmarc=fail (p=NONE sp=NONE dis=NONE) header.from=nytimes.com Date: Thu, 01 Aug 2019 12:18:30 -0700 (PDT) Received: from app06.cl02.ca.us.workfront.com  (app06.cl02.ca.us.workfront.com [10.44.102.36]) by mail.attask-ondemand.com (Postfix) with ESMTP id 5265C81CBA for <Dave.Mohapatra@nytimes.com>; Thu, 1 Aug 2019 13:18:29 -0600 (MDT)"

pos_1 = raw_data.find("@")
print(pos_1)
pos_2 = raw_data.find(">", pos_1)

hosting_server = raw_data[pos_1 + 1 : pos_2]
print(hosting_server)
print("the length of data is:", len(raw_data))

counter = 0
for i in raw_data:
    pos_a = raw_data.find("ESMTP")
    pos_b = raw_data.find(" ", pos_a)

r_value = raw_data[pos_a:pos_b]
print("pos b is ", pos_b)
print("r value is ", r_value)
