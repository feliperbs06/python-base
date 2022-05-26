"""
Faça um programa que imprime os números pares de 1 a 200


ex
`python3 numeros_pares.py`
2
4
6
8
...
"""
numbers = range(1, 201)
for num in numbers:
    if num % 2 == 0:
        print(num)
