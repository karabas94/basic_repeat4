"""
2. Користувач вводить з клавіатури рядок та символ для пошуку.
Порахуйте скільки разів у рядку зустрічається потрібний символ.
Отримане число виведіть на екран.
"""

input_text = input("Enter a string: ")
input_symbol = input("Enter a symbol for search: ")

if input_text == '' and input_symbol == '':
    print("Please enter string and symbol for search.")
elif input_text == '':
    print("Please enter string.")
elif input_symbol == '':
    print("Please enter symbol for search.")
else:
    count = input_text.count(input_symbol)
    print(count)
