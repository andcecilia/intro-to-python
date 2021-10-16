tamanho = int(input("Digite quantos números você quer somar:"))
soma=0
i=0
while i < tamanho:
    valor = int(input("Digite o número a ser somado:"))
    soma = soma + valor
    i += 1
print("A soma de todos os valores é", soma)