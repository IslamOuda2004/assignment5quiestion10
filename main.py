tuple1 = (10, 20, 30, 40)

list1 = list(tuple1)

counter = 0

a = None

b = None

c = None

d = None

list2 = [a,b,c,d]

while counter < len(list1):
    list2[counter]=list1[counter]
    counter += 1

a = list1[0]
b = list1[1]
c = list1[2]
d = list1[3]

print(a)
print(b)
print(c)
print(d)


