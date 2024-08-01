frase = str(input('Digite uma frase: ').strip()).upper()
a = frase.count('A')
primeira_a = frase.find('A')+1
ultima_a = frase.rfind('A')+1
print(f'A letra A aparece {a} vezes')
print(f'A primeira letra A apareceu na posição {primeira_a}')
print(f'A útima letra A apareceu na posição {ultima_a}')
