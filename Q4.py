import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))
# continue here
for i in range(len(random_numbers)):

    if random_numbers[i] % 2 != 0:
        random_numbers[i] = -random_numbers[i]
    else:
        random_numbers[i] = random_numbers[i] * 2

print(random_numbers)