numbers0 = [1, 2, 4, 5]
numbers1 = [2, 4, 5]

def find_missing_number(numbers):

  highest_number_possible = len(numbers) + 1
  missing_number = []

  for i in range (1, highest_number_possible + 1):
    if i not in numbers:
      missing_number.append(i)

  if(len(missing_number) > 1):
    return missing_number
  else:
    return missing_number[0]
    
first_test_find_missing_number = find_missing_number(numbers0)
second_test_find_missing_number = find_missing_number(numbers1)
print(first_test_find_missing_number)
print(second_test_find_missing_number)

def separate_odd_and_even_numbers (numbers):
  even = []
  odd = []

  for i in range(len(numbers)):
    if (numbers[i] % 2 == 0):
      even.append(numbers[i])
    if (numbers[i] % 2 != 0):
      odd.append(numbers[i])

  return even + odd

numbers2 = [2, 5, 9, 1, 4, 8, 3, 6, 12, 22, 37, 7]

first_test_separate_odd_and_even_numbers = separate_odd_and_even_numbers(numbers2)
print(first_test_separate_odd_and_even_numbers)

