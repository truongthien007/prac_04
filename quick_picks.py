import random

quick_pick = int(input("How many quick pick you want to generate? "))
for i in range(0, quick_pick):
    values = []
    while len(values) != 6:
        value = random.randint(1, 45)
        if value not in values:
            values.append(str(value))
    print(', '.join(values))
