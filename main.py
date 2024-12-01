l1 = []
l2 = []
distance = []
total = 0
with open('input.txt') as inputfile:
    for line in inputfile:
        i = line.split()
        l1.append(int(i[0]))
        l2.append(int(i[1]))
l1.sort()
l2.sort()
for list1, list2 in zip(l1, l2):
    # print(f'{list1} {list2} {list1-list2}')
    i = list1 - list2
    if i < 0:
        i = list2 - list1
    distance.append(i)
for i in distance:
    total += i

print(f'The answer to challange one is {total}')
challange2 = []
for i in l1:
    similarityscore = 0
    for o in l2:
        if i == o:
            similarityscore += 1
    challange2.append(i * similarityscore)
total = 0
for i in challange2:
    total += i
print(f'The answer to challange one is {total}')