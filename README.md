# Cypher

# Works in 4 modes, supports 2 ciphers
# Examples of launching for each of the modes:
## Encrypt:
### Caesar:
`python3 main.py encode --input_file input.txt --output_file output.txt --cipher caesar --key 2`
### Vigenere:
`python3 main.py encode --input_file input.txt --output_file output.txt --cipher vigenere --key lemon`
## Decrypt:
### Caesar:
`python3 main.py decode --input_file input.txt --output_file output.txt --cipher caesar --key 2`
### Vigenere:
`python3 main.py decode --input_file input.txt --output_file output.txt --cipher vigenere --key lemon`
## Calculate the frequency of characters in the text:
`python3 main.py frequency --input_file input.txt --output_file output.json`
## Hack cypher:
### Caesar:
`python3 main.py hack --input_file input.txt --output_file output.txt --cipher caesar --frequency_file frequency.json`
