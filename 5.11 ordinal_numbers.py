numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ordinated_numbers = []
for num in numbers:
    if num == 1:
        ordinated_numbers.append(str(num) + "st")
    elif num == 2:
        ordinated_numbers.append(str(num) + "nd")
    elif num == 3:
        ordinated_numbers.append(str(num) + "rd")
    else:
        ordinated_numbers.append(str(num) + "th")

for i in range(len(ordinated_numbers)):
    print(ordinated_numbers[i])
