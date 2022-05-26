""" 
Repete vogais

Faça um programa que pede ao usuário que digite uma ou mais palavras e 
imprime cada uma das palavras com suas vogais duplicadas.

ex:

python repete_vogal.py
'Digite uma palavra (ou enter para sair):' Python
'Digite uma palavra (ou enter para sair):' Bruno
'Digite uma palavra (ou enter para sair):' <enter>
Pythoon
Bruunoo
"""
import logging

log = logging.Logger("repeat vowel")
words = []

while True:
    word = input("Digite uma palavra (ou enter para sair): ").strip()

    if not word:
        break
    if word.replace(".", "").isdigit():
        log.error("Por favor, digite uma palavra")
        continue

    final_word = ""
    for char in word:
        # TODO: Remover acentuação usando função
        final_word += char * 2 if char.lower() in "aeiou" else char
    words.append(final_word)

print(*words, sep="\n")
