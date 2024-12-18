Python 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> letter = input("Введите букву латинского алфавита: ").lower()
Введите букву латинского алфавита: a
>>> if letter in ['a', 'e', 'i', 'o', 'u']:
...     print(f"Буква '{letter}' является гласной.")
... elif letter == 'y':
...     print("Буква 'y' может быть как гласной, так и согласной.")
... elif letter.isalpha() and len(letter) == 1:
...     print(f"Буква '{letter}' является согласной.")
... else:
...     print("Ошибка: Введите одну букву латинского алфавита.")
... 
...     
Буква 'a' является гласной.
