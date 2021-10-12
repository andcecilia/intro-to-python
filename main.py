n = int(input("Digite o valor de n:"))
d = int(input("Digite o valor de d:"))
ocorrencia = 0
r=n
while n!=0:
    if (n%10==d):
        ocorrencia+=1
    n=n//10
print("O dígito", d, "ocorre", ocorrencia, "vezes em", r)