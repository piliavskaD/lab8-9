import random

t1 = (1, 2, 3, 4)
t2 = (1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7)
t3 = ("aaa", "bbb", "ccc", "ddd", "eee")

all_t = t1 + t2 + t3
all_l = list(all_t)
#print(all_l)
random.shuffle(all_l)
print(tuple(all_l))