numbers = []
for i in range(0, 5):
    number = int(input("Number: "))
    numbers.append(number)
print(f"The first number is {numbers[0]}")
print(f"The first number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The biggest number is {max(numbers)}")
print(f"The average number is {sum(numbers)/len(numbers)}")