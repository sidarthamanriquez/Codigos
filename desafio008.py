#Escreva um programa que leia um valor em metros e o exiba em centimetros e milimetros

m1 = float(input('Digite sua altura '))

c = m1 * 100
m = m1 * 1000

print('o {} em centimetros {} e em milimetros {}'.format(m1, c, m))
