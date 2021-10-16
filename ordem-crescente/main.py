n = int(input("Digite a quantidade de dígitos: "))
crescente=True
anterior=int(input("Digite um número:"))
i=1
while i<n and crescente:
    atual = int(input("Digite mais um número:"))
    if anterior>=atual:
        crescente=False
    anterior=atual
    i+=1
if crescente:
    print("Esta em ordem crescente.")
else:
    print("Não esta em ordem crescente.")