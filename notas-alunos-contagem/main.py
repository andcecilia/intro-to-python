n = int(input("Digite o número de alunos: "))
recuperação=0
while n>0:
    nf = float(input("Digite a nota do aluno:"))
    if nf>3 and nf<5:
        recuperação+=1
    n=n-1
print("O total de alunos em recuperação é", recuperação)