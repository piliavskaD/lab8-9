d = {}

students = ("A", "B", "C", "D", "E", "F", "G")

grade = [
    [10, 7, 4],
    [6, 3, 9],
    [2, 4, 3],
    [8, 8, 7],
    [10, 9, 10],
    [5, 8, 10],
    [2, 4, 9]
]

ave = []
for i, v in enumerate(grade):
    average = sum(grade[i]) / 3
    ave.append(format(average, ".1f"))
#print(ave)

for i in range(len(students)):
    d[students[i]] = ave[i]
print(d)