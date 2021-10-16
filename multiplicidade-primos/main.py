n = int(input("Digite um numero inteiro: "))
multiplicidade = 0
fator = 2
while n>1:
    while n%fator==0:
        multiplicidade +=1
        n = n/fator
    if multiplicidade>0:
        print("O fator", fator, "tem a multiplicidade", multiplicidade)
    fator +=1
    multiplicidade = 0


