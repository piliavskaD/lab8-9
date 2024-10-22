from array import*
import random

A = array("i", [])


for i in range(24):
    some_num = random.randint(1, 30)
    A.append(some_num)
#print(A, end=" ")


B = array("i", [])
for j in A:
    if j not in B:
        B.append(j)
print(f"Massive B: {B}")

#print(len(B))


s = 0
for el in B:
    s += el
    average = s/len(B)
print(f"Sum elements of massive B: {s}")
print(f"Average value: {format(average, ".2f")}")