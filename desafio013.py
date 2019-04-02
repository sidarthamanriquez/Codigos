# Faça um algoritmo que leia o salário de um funcionário e mostre o seu novo salário, com 15% de aumento

salarioAtual = float(input('Digite seu slário atual para saber o novo com aumento de 15% '))

porcetagem15 = (salarioAtual * 15) / 100

resultado = porcetagem15 + salarioAtual

print('Seu sálario com 15% de aumto é {:.2f}'.format(resultado))