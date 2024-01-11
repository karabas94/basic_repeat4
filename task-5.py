"""
Додатково:
Є певний текст. Реалізуйте наступну функціональність:
■ Змінити текст таким чином, щоб кожне речення починалися з великої літери;
■ Порахуйте скільки разів цифри зустрічаються у тексті;
■ Порахуйте скільки разів розділові знаки зустрічаються в тексті;
■ Порахуйте кількість знаків оклику в тексті.
"""

input_text = "jgjglkfglk. fgjkfdld123. sdfds 45678,90!"
new_string = ""
for i in input_text.split(". "):
    new_string += i.capitalize() + ". "
new_string = new_string.rstrip(". ")
print(new_string)

count_digit = 0
for i in input_text:
    if i.isdigit() == True:
        count_digit += 1
print(count_digit)

count_strip = 0
for i in input_text:
    if i == "." or i == ",":
        count_strip += 1
print(count_strip)

count_wik = 0
for i in input_text:
    if i == "!":
        count_wik += +1
print(count_wik)