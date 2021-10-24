n = int(input("Digite um número inteiro:"))
total = 0
i=1

def Primo(total,i, n):
    while i<=n:
        if n%i==0:
            total+=1
    #print(i)
        i+=1
    return total

def Verificar(total):
    if Primo(total, i, n) == 2:
        return True
    else:
        return False

print(Verificar(total))
