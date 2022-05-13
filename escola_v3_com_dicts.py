#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade.


Imprimir a lista de crianças agrupadas por sala
que frequenta cada uma das atividades.
"""
__version__ = "0.1.1"

# Dados
salas = {
    "sala1": ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"],
    "sala2": ["João", "Antonio", "Carlos", "Maria", "Isolda"],
}

atividades = {
    "Inglês": ["Erik", "Maia", "Joana", "Carlos", "Antonio"],
    "Musica": ["Erik", "Carlos", "Maria"],
    "Dança": ["Gustavo", "Sofia", "Joana", "Antonio"],
}

# Listar alunos em cada atividade por sala
for nome_atividade, atividade in atividades.items():
    print("-" * 40)
    print(f"Alunos da atividade {nome_atividade}\n")

    print(f"Sala 1 {set(salas['sala1']) & set(atividade)}")
    print(f"Sala 2 {set(salas['sala2']).intersection(atividade)}")
    print("-" * 40)
