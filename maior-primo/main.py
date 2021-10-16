
k = 100
def éPrimo(k):
    total = 0
    i=1
    while i<=k:
        if k%i==0:
            total +=1
        i +=1
    return total==2

def maior_primo(a):
    for i in range(1,a+1):
        if éPrimo(i):
            ultimo_primo = i
            #print("i=", i)
    return ultimo_primo
    #print(ultimo_primo)
maior_primo(k)