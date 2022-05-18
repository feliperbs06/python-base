"""Imprime a mensagem de um e-mail

NÃO MANDE SPAM!!!
"""

import sys
import os

arguments = sys.argv[1:]

if not arguments:
    print("Informe o nome do arquivo de emails")
    sys.exit(1)

filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, filename)
templatepath = os.path.join(path, templatename)


for line in open(filepath):
    name, email = line.split(",")

    # TODO: Substituir por envio de email
    print(f"Enviando email para: {email}")
    print()
    print(
        open(templatepath).read()
        % {
            "nome": name,
            "produto": "caneta",
            "texto": "Escrever muito bem",
            "link": "https://canetaslegais.com",
            "quantidade": 1,
            "preco": 50.50,
        }
    )
    print("-" * 50)
