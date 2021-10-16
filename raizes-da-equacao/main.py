import math

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

delta = b**2-4*(a)*(c)
print("O valor de delta e", delta)
if delta < 0:
    print("Essa equação não possui raizes reais.")
elif delta == 0:
    xzero= -b/(2*(a))
    print("Essa equação possui apenas uma raiz,", xzero)
else:
    raizdelta = math.sqrt(delta)
    print("A raiz quadrada de delta e", raizdelta)
    x1=(-b+raizdelta)/(2*(a))
    print("Uma raiz e", x1)
    x2=(-b-raizdelta)/(2*(a))
    print("A outra raiz e", x2)