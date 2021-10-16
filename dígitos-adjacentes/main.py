n = int(input("Digite um número inteiro:")) #5667
n_salvo = n #5667
anterior = n%10 #5667/10=566 com resto 7. anterior = 7
n = n//10 #5667/10 sem resto é=566
adj_iguais = False #o valor dessa variável é falso e ponto, não existe isso de "é verdadeiro que o valor disso é falso, não", é simplesmente falso.
#print("primeiro valor de n no loop:", n)
while n > 0 and not adj_iguais: #enquanto o 566>0 E not adj_iguais (esse not vai fazer o valor original que era false virar true, tornando a condição verdadeira)
    atual = n%10 #atual vai receber resto da divisão de 566 por 10 = 6
    #print("anterior, atual:", anterior, atual)
    if atual == anterior: #se 6 é igual a 6
        adj_iguais = True #se virar True significa que ao colocar no while not adj_iguais vai resultar False, o que faz sair do loop.
    else:
        anterior=atual #anterior receberá o valor da variável atual
        n=n//10 #a divisão exata vai ser o novo valor de n, a ser colocado no looping mais uma vez
if adj_iguais:
    #print(n_salvo, "tem dois dígitos adjacentes:", atual)
    print("sim")
else:
    #print(n_salvo, "não tem dígitos iguais adjacentes.")
    print("não")