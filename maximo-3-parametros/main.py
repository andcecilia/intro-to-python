#n1 = int(input("Digite um n: "))
#n2 = int(input("Digite um n: "))
#n3 = int(input("Digite um n: "))
n1 = 3
n2 = 4
n3 = 5

def maximo(x,y,z):
    if x>y and x>z:
        return x
    elif y>x and y>z:
        return y
    else:
        return z

maximo(n1,n2,n3)