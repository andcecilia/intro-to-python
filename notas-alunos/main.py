n = int(input("Quantos alunos você quer inserir?"))
recuperação =0
reprovados =0
aprovados =0
muitobom =0
while n>0:
    media = float(input("Digite uma media:"))
    n=n-1
    if media >= 3 and media< 5:
        recuperação +=1
    elif media < 3:
        reprovados +=1
    elif media >=5 and media < 8:
        aprovados +=1
    else:
        muitobom +=1
print("Número de alunos reprovados=",reprovados)
print("Número de alunos de recuperação=",recuperação)
print("Número de alunos aprovados=",aprovados)
print("Número de alunos com desempenho muito bom=",muitobom)