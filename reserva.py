"""
Faça um programa de terminal que exibe ao usuário uma lista dos quartos
disponíveis para alugar e o preço de cada quarto, esta informação está
disponível em um arquivo de texto separado por virgulas.

`quartos.txt`
# código, nome, preço
1,Suíte Master,500
2,Quarto Familia,200
3,Quarto Single,100
4,Quarto Simples,50

O programa pergunta ao usuário o nome, qual o número do quarto a ser reservado
e a quantidade de dias e no final exibe o valor estimado a ser pago.

O programa deve salvar esta escolha em outro arquivo contendo as reservas.

`reservas.txt`
# cliente, quarto, dias
Bruno,3,12

Se outro usuário tentar reservar o mesmo quarto o programa deve exibir uma
mensagem informando que já está reservado.
"""
# import sys
# import logging

# log = logging.Logger("booking")

# template_rooms = """Quarto {room_number}:
#     Nome: {name}
#     Preço: {price}
# """

# template_confirmation = """
# O preço da reserva do quarto {room}, {name} 
# por {days} dias é {price} reais.\nVocê deseja fazer a reserva?  
# [Digite sim para confirmar, e qualquer outra tecla para cancelar] 
# """

# rooms = {}
# try:
#     for room in open("quartos.txt"):
#         number, name, price = room.split(",")
#         rooms[number.strip()] = {"name": name.strip(), "price": int(price.strip())}
# except FileNotFoundError:
#     log.error("Arquivo não existe.")
#     sys.exit(1)

# for room_number in rooms.keys():
#     print(
#         template_rooms.format(
#             room_number=room_number,
#             name=rooms[room_number]["name"],
#             price=rooms[room_number]["price"],
#         )
#     )

# try:
#     room = int(input("Escolha um quarto: ").strip())
# except ValueError:
#     log.error("Por favor digite o número do quarto.")
#     sys.exit(1)

# if room not in rooms:
#     log.error("O quarto não existe.")
#     sys.exit(1)

# bookings = set(line.split(",")[1] for line in open("reservas.txt"))

# if room in bookings:
#     log.error("O quarto já foi reservado.")
#     sys.exit(1)

# name = input("Digite o seu nome: ").strip()
# if name.replace(".", "").isdigit():
#     log.error("Nome inválido.")
#     sys.exit(1)

# try:
#     days = int(input("Número de dias: ").strip())
# except ValueError:
#     log.error("Por favor, insira um número inteiro.")
#     sys.exit(1)

# total_price = rooms[room]["price"] * days

# confirmation = input(
#     template_confirmation.format(
#         room=room,
#         name=rooms[room]["name"],
#         days=days,
#         price=total_price,
#     )
# ).strip()

# if confirmation.lower() != "sim":
#     print("Sua reserva não foi efetuada.")
#     sys.exit(0)

# try:
#     with open("reservas.txt", "a") as f:
#         f.write(f"{name},{room},{days}\n")
#         print("Reserva efetuada com sucesso!")
# except FileNotFoundError:
#     log.error("Arquivo não existente.")
#     sys.exit(1)


import sys
import logging


ocupados = {}
try:
    for line in open("reservas.txt"):
        nome, num_quarto, dias = line.strip().split(",")
        ocupados[int(num_quarto)] = {
            "nome": nome,
            "dias": dias
        }

except FileNotFoundError:
    logging.error("Arquivo `reservas.txt` não existe")
    sys.exit(1)

quartos = {}
try:
    for line in open("quartos.txt"):
        codigo, nome, preco = line.strip().split(",")
        quartos[int(codigo)] = {
            "nome": nome,
            "preco": float(preco), # TODO: Decimal
            "disponivel": False if int(codigo) in ocupados else True
        }

except FileNotFoundError:
    logging.error("Arquivo `quartos.txt` não existe")
    sys.exit(1)


print("Reserva Hotel Pythonico")
print("-" * 40)

if len(ocupados) == len(quartos):
    print("Hotel lotado")
    sys.exit(1)

nome = input("Nome do cliente:").strip()

print("Lista de quartos disponíveis:")
for codigo, dados in quartos.items():
    nome_quarto = dados["nome"]
    preco = dados["preco"]
    disponivel = "✅" if dados["disponivel"] else "⛔️"
    # TODO: Substituir casa decimal por virgula
    print(f"{codigo} - {nome_quarto} - R$ {preco:.2f} - {disponivel}")

print("-" * 40)

try: 
    num_quarto = int(input("Número do quarto:").strip())
    if not quartos[num_quarto]["disponivel"]:
        print(f"O quarto {num_quarto} está ocupado.")
        sys.exit(1)
except ValueError:
    logging.error("Número inválido, digite apenas digitos.")
    sys.exit(1)
except KeyError:
    print(f"O quarto {num_quarto} não existe.")
    sys.exit(1)

try: 
    dias = int(input("Número de dias: ").strip())
except ValueError:
    logging.error("Número inválido, digite apenas digitos.")
    sys.exit(1)

nome_quarto = quartos[num_quarto]["nome"]
preco_quarto = quartos[num_quarto]["preco"]
disponivel = quartos[num_quarto]["disponivel"]
total = preco_quarto * dias

with open("reservas.txt", "a") as file_:
    file_.write(f"{nome},{num_quarto},{dias}\n")

print(f"{nome} você escolheu o quarto {nome_quarto} e vai custar: R${total:.2f}")
