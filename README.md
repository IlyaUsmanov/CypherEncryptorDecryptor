# Шифрование

# Работает в 4 режимах, поддерживает 2 шифра, без бонусов
# Примеры запуска для каждого из режимов:
## Зашифровать:
### Цезарь:
`python3 main.py encode --input_file input.txt --output_file output.txt --cipher caesar --key 2`
### Виженер:
`python3 main.py encode --input_file input.txt --output_file output.txt --cipher vigenere --key lemon`
## Дешифровать:
### Цезарь:
`python3 main.py decode --input_file input.txt --output_file output.txt --cipher caesar --key 2`
### Виженер:
`python3 main.py decode --input_file input.txt --output_file output.txt --cipher vigenere --key lemon`
## Посчитать частотность символов в тексте:
`python3 main.py frequency --input_file input.txt --output_file output.json`
## Взломать шифр:
### Цезарь:
`python3 main.py hack --input_file input.txt --output_file output.txt --cipher caesar --frequency_file frequency.json`
