n = int(input("Digite um número inteiro:"))
total = 0
i=1
while i<=n:
    if n%i==0:
        total+=1
    #print(i)
    i+=1

primo = True

if total==2:
    print(primo)
else:
    print("não primo")
