#!/usr/bin/env python3

# For loops / Laço for
original = [1, 2, 3]
dobrada = []
for n in original:
    dobrada.append(n * 2)

print(dobrada)

# Funcional
# List Comprehension
dobrada = [n * 2 for n in original]
print(dobrada)

# Dict comprehension
dados = {
    line.split(":")[0]:line.split(":")[1].strip()
    for line in open("post.txt")
    if ":" in line
}
print(dados)
