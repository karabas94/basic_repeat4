"""
3. Користувач вводить з клавіатури рядок, слово для пошуку, слово для заміни.
Зробіть у рядку заміну одного слова на інше.
Отриманий рядок на екрані.
"""

input_string = "hello hello"
input_first_word = "hello"
input_second_word = "buy"

if input_string.strip() == "":
    print("Enter the string")
elif input_first_word.strip() == "":
    print("Enter the search word")
elif input_second_word.strip() == "":
    print("Enter the word for replacing")
else:
    words_in_str = input_string.split()

    # count words in string
    for i in range(len(words_in_str)):
        # check if word from string equal to search word
        if words_in_str[i] == input_first_word:
            # replacing words
            words_in_str[i] = input_second_word
            # making new string
            new_string = ' '.join(words_in_str)
            print(new_string)
        else:
            print("Word not found")
