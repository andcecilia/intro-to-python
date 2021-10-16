# o programa pega o numero digitado e separa algarismo por algarismo para depois somar cada algarismo
# teremos como variáveis:
# 1 - a entrada digitada
# 2 - uma variável para guardar o resultado da divisão exata por 10
# 3 - o resto da divisão por 10 para extrair o último dígito
# 4 - uma variável para guardar a soma e ser incrementada a cada iteração
# isso estará dentro de um looping com a condição: se o n for maior que zero
n = int(input("Digite um número inteiro:"))
soma = 0
while n>0:
    resto = n%10
    soma = soma + resto
    n = n//10
print(soma)
