"""
1. Користувач вводить рядок з клавіатури.
Порахуйте кількість літер, цифр у рядку.
Виведіть обидві кількості на екран. (використовувати цикл)
"""

input_text = input("Please enter a string: ")
count_alpha = 0
count_digit = 0

for i in input_text:
    if i.isalpha():
        count_alpha += 1
    elif i.isdigit():
        count_digit += 1
print(f'Amount of letters: {count_alpha} \nAmount of digits: {count_digit}')
