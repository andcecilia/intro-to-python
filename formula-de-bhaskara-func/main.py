import math

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

def delta(a,b,c):
    deltar = b ** 2 - 4 * (a) * (c)
    return deltar

if delta(a,b,c) < 0:
    print("esta equação não possui raízes reais")
elif delta(a,b,c) == 0:
    xzero=-b/(2*(a))
    print("a raiz desta equação é", xzero)
else:
    raizdelta = math.sqrt(delta(a,b,c))
    x1=(-b+raizdelta)/(2*(a))
    x2=(-b-raizdelta)/(2*(a))
    if x1 < x2:
        print("as raízes da equação são", x1, "e", x2)
    else:
        print("as raízes da equação são", x2, "e", x1)
