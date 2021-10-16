n = int(input("Digite o valor de n:"))
def fatorial(n):
    fatorial = 1
    while n > 1:
        fatorial = fatorial * n
        n = n - 1
    print(fatorial)
while n>=0:
    fatorial(n)
    n = int(input("Digite o valor de n:"))