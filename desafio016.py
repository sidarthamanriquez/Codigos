# crie um algoritmo que leia um nro Real qualquer pelo teclado e mostre na tela a sua porção Inteira
# Ex: 'digite um nro ' 6.127
# o nro 6.127 tem a parte inteira 6

flutua = float(input('digite um nro Real '))

print('O nro {} tem a parte inteira {:.0f}'.format(flutua, flutua))