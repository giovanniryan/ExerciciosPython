#Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
n = int(input('Digite um número: '))
s = n+1
a = n-1
print("O sucessor e antecessor do número {} é {} e {}".format(n, s, a))

#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
d = n*2
t = n*3
rq = n ** (1/2)
print('O número é {}, seu dobro é {}, seu triplo é {} e sua raiz quadrada é {:.3f}'.format(n, d, t, rq))

#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
nota1 = int(input('Insira sua nota do 1° bimestre: '))
nota2 = int(input('Insira sua nota do 2° bimestre: '))
média = (nota1+nota2)/2
print('Sua média é {}'.format(média))

#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
m = float(input('Insira o seu métro: '))
cm = m * 100
mm = cm * 100
print('O seu métro >{}< em centímetros é {} e em milímetros é {}'.format(m, cm, mm))

#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
real = float(input('Insira o quanto de R$ que você tem: '))
dolar = real / 5.10
print("Você tem {} reais e pode comprar {:.2f} dólares.".format(real, dolar))

#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Digite seu sálario: '))
aumento = salario * 15/100
sn = salario + aumento
print('O seu aumento foi de R${:.2f}, portanto, seu sálario novo será R${:.2f}'.format(aumento, sn))

#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input("Qual o preço do produto? R$"))
np = preco - (preco * 5 /100)
print("O produto que custava R${:.2f} agora custa R${:.2f} com desconto de 5%!!! ".format(preco, np))

#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dias = int(input("Quantos dias o carro foi alugado? "))
km = float(input("Quantos kilometros o carro percorreu? "))
preco = (60 * dias) + (0.15 * km)
print("O preço a ser pago é de R${:.2f}, seu carro percorreu {} dias e rodou {}km.".format(preco, dias, km))