#crie um algoritmo que leia um nro e mostre o seu dobro, triplo e raiz quadrada

v1 = int(input('digite um valor'))

d = v1 ** 2
t = v1 ** 3
r = v1 ** (1/2)

print('o nro {} elevado ao quadrado é {} e elevado ao cubo é {} e sua raiz quadrada é {}'.format(v1, d, t, r))