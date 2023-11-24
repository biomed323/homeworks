 number = int(input("Введіть ціле число: "))
 count_of_zeros = str(number).count('0')

 print(f"Кількість нулів у числі {number}: {count_of_zeros}")


 number = int(input("Введіть ціле число: "))
 number_str = str(number)
 trimmed_str = number_str.rstrip('0')
 count_of_zeros = len(number_str) - len(trimmed_str)
 print(f"Кількість нулів наприкінці числа {number}: {count_of_zeros}")

 my_list_1 = [1, 2, 3, 4, 5]
 my_list_2 = [10, 20, 30, 40, 50]
 my_result = []
 my_result.extend(my_list_1[1::2])
 my_result.extend(my_list_2[1::2])

 print(my_result)

 my_list = [1, 2, 3, 4]
 new_list = my_list[1:] + [my_list[0]]

# print(new_list)

# my_list = [1, 2, 3, 4]
# my_list.append(my_list.pop(0))
# print(my_list)

# input_string = "43 більше ніж 34, але менше ніж 56"
# words = input_string.split()
# sum_of_numbers = 0
# for word in words:
#     if word.isdigit():
#         sum_of_numbers += int(word)
# print(f"Сума всіх чисел у рядку: {sum_of_numbers}")

# my_list = [1, 2, 3, "11", "22", 33]
# string_list = [item for item in my_list if isinstance(item, str)]
# print(string_list)

# my_str = "abacabad"
# chars_list = [char for char in my_str if my_str.count(char) == 1]
# print(chars_list)

# str1 = "abc"
# str2 = "bcd"
# chars_list = list(set(str1) & set(str2))
# print(chars_list)

str1 = "aaaasdf1"
str2 = "asdfff2"
chars_list = [char for char in set(str1) & set(str2) if str1.count(char) == str2.count(char) == 1]
print(chars_list)