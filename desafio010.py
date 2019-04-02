#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dolares ela pode comprar
#Considere que US$1,00 = R$3,27

d1 = float(input('digite quanto tem na carteira '))

r1 = d1 / 3.27

print('voce pode comprar {:.2f} dolares'.format(r1))