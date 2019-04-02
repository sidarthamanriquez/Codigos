# faça um algoritmo que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por KM rodado.

dias = int(input('quantos dias alugados? '))
kms = float(input('quantos kms foram todados? '))
d = dias * 60
k = kms * 0.15
total = d + k
print('A pagar pelos dias R${:.2f} mais por KMs R${:.2f} o total é R${:.2f}'.format(d, k, total))



# tambem pode ser feito assim
#dias = int(input('quantos dias alugados? ')
#km = float(input('quantos kms rodados? '))
#pago = (dias * 60) + (km * 0.15)
#print('o total a pagar é R${:.2f}'.format(pago))