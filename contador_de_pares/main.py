contador=0
pares=0
impares=0
while contador<6:
    numero = int(input("Digite um numero:"))
    contador = contador+1
    if numero%2==0:
        pares=pares+1
    else:
        impares=impares+1
print("Foram digitados", pares, "numeros pares e", impares, "numeros impares.")