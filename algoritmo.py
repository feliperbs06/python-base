"""Algoritmos

Sequencia de instruções lógicas que visam obter a solução de um problema.

Problema: Ir a padaria e comprar pão:
Premissa: Padaria da Esquina abre fds: até 12h, semana até 19h, feriado (exceto Natal) não abre.

1- A padaria está aberta?
    1. Se é feriado e NÃO é natal: não
    2. Senão, Se é sábado OU domingo E antes do meio dia: sim
    3. Senão, se é dia de semana E antes das 19h: sim
    4. senão: não
2- Se padaria está aberta E:
    1. Se está chovendo: Pegar guarda-chuvas
    2. Se está chovendo E calor: Pegar guarda-chuvas e garrafa de agua
    3. Se está chovendo E frio OU nevando: pegar guarda chuva, blusa e botas
    4. Ir até a padaria:
        1. Se tem pao integral E baguete: Pedir 6 de cada
        2. Senão, se tem apenas pao integral OU baguete: Pedir 12
        3. Senão: Pedir 6 de qualquer pão
3- Senão
    1. Ficar em casa em comer bolachas
"""
# PSEUDO CODIGO
import ir, pegar, pedir, tem, comer, ficar

# Premissas
today = "Segunda"
hora = 15
natal = False
chovendo = False
frio = True
nevando = True
semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
feriado = ["Quarta"]
horario_padaria = {
    "semana": 19,
    "fds": 12,
}

# Algoritmo
if today in feriado and not natal:
    padaria_aberta = False
elif (today not in semana and hora < horario_padaria["fds"]) or (
    today in semana and hora < horario_padaria["semana"]
):
    padaria_aberta = True
else:
    padaria_aberta = False

if padaria_aberta:
    if chovendo and frio or nevando:
        pegar("guarda-chuva")
        pegar("blusa")
        pegar("botas")
    elif chovendo and not frio:
        pegar("guarda-chuva")
        pegar("agua")
    elif chovendo:
        pegar("guarda-chuva")

    ir("padaria")

    if tem("pao int") and tem("baguete"):
        pedir(6, "pao int")
        pedir(6, "baguete")
    elif tem("pao int") or tem("baguete"):
        pedir(12, "qualquer um dos 2")
    else:
        pedir(6, "qualquer pao")
else:
    ficar("casa")
    comer("bolacha")
