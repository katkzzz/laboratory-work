numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
total_el = len(numbers)
numbers_without_none = numbers[:4] + numbers[4 + 1:]
sum_of_numbers = sum(numbers_without_none)

average = round(sum_of_numbers / total_el, 2)
numbers[4] = average

print("Измененный список:", numbers)