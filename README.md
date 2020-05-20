# Шифрование

# Работает в 4 режимах, поддерживает 2 шифра, без бонусов
# Примеры запуска для каждого из режимов:
## Зашифровать:
### Цезарь:
`python3 main.py encode --input_file input.txt --output_file output.txt --cipher caesar --key 2`
## Вижинер:
`python3 main.py encode --input_file input.txt --output_file output.txt --cipher vigenere --key lemon`
`python3 main.py decode --input_file input.txt --output_file output.txt --cipher caesar --key 2`

`python3 main.py frequency --input_file input.txt --output_file output.json`

`python3 main.py hack --input_file input.txt --output_file output.txt --cipher caesar --frequency_file frequency.json`
