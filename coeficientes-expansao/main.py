#esse código não funciona

def main():
    n = int(input("Digite o valor de n:"))
    contador = 0
    while contador <=n:
        print("Coeficiente de x^", n-contador, "e de y", contador, "será", combinação(n, contador))
        contador +=1

def fatorial(a):
    k = int(input("Digite o valor de k:"))
    fat = 1
    contador = 1
    while (contador<k):
        contador +=1
        fat = fat * contador
    return fat

def combinação(m,n):
    n = int(input("Digite o valor de n:"))
    m = int(input("Digite o valor de m:"))
    comb = fatorial(m)/(fatorial(m-n)*fatorial(n))
    return comb

main()