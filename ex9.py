A = [23, -2, 14, -10, 50, -30, 11, -60, 30, -16]

negativos = len([n for n in A if n < 0])
somaPositivos = sum([n for n in A if n > 0])

print (A)
print (f"O vetor tem {negativos} números negativos.")
print (f"A soma de todos os números positivos do vetor é {somaPositivos}.")