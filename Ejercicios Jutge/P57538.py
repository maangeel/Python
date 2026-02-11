numbers = input().split()
if len(numbers) == 1:
    numbers2 = input().split()
    numbers.append(numbers2[0])
total = 0
for num in numbers:
    total += int(num)
print(total)