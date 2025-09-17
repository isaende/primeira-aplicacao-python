# exercício 01
num = int (input ('Digite um número: '))

if num % 2 == 0:
    print('O número é par!')
else:
    print('O número é impar!')


# exercício 02
idade = int(input('Digite sua idade: '))

if idade >= 0 and idade <= 12:
    print('Criança')
elif idade >= 13 and idade <= 18:
    print('Adolescente')
elif idade >= 18:
    print('Adulto')
else:
    print('Valor inválido!')

#exercício 03
usuario = input("Digite o usuário: ")

senha = int(input("Digite a senha: "))

while usuario != 'Frederico':
    usuario = input("Digite o usuário corretamente: ")


while senha != 12345:
    senha = int(input('Digite a senha corretamente: '))