#  Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la,
#  sabendo que cada litro de tinta, pinta uma área de 2mquadrados

a1 = float(input('digite a altura '))
a2 = float(input('digite a largura '))

r1 = a1 * a2
r2 = r1 / 2
print('será necessário {:.2f} litros de tinta'.format(r2))