# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p1 = float(input('Digite o preço '))

r = (p1 * 5) / 100

r2 = p1 - r

print('o preço com 5% de desconto é {}'.format(r2))