n = int(input("Digite o valor de n:"))
m = int(input("Digite o valor de m:"))
def fatorial(a):
    fat = 1
    while (a>1):
        fat = fat * a
        a = a-1
    return fat
print(fatorial(n))
print(fatorial(m))

def combinação(m,n):
    comb = fatorial(m)/(fatorial(m-n)*fatorial(n))
    return comb

print(combinação(m,n))
print("Combinacao(4,2) =", combinação(4,2))
print("Combinacao(5,2) =", combinação(5,2))
print("Combinacao(10,4) =", combinação(10,4))