#A file to schedule tasks

import random

n = random.randint(1, 2*10 **5)


print("N = ",n)

#n = 5

list1 = random.choices(range(1, 10 **9), k = n)

list2 = []
for x in list1:
    number = random.choices(range(x ,10 **9), k = n)
    list2.append(number)

print("List1 = ",list1)
print("List2 = ",list2)


#list1 = [1, 1, 1, 1, 1]
#list2 = [2, 2, 2, 2, 2]


def scheduling(list1, list2):
    i = 0
    j = 1
    while i <= n-1:
        x = (list1[i], list2[i])
        if i <= n-2:
            y = (list1[i+1], list2[i+1])

            if x != y:
                z = [x, y]
                print(f'Machine {j} = {z}')
                
            else:
                print(f'Machine {j} = {[x]}')
                print(f'Machine {j+1} = {[y]}')
                j += 1
        if i == (len(list1))-1:
            print(f'Machine {j} = {[x]}')
        i += 2
        j +=1
        continue
        
scheduling(list1, list2)
