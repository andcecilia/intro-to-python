número = int(input("Insira o número para exibir sua tabuada:"))
 for i in range(0,11):
     result = número*i
     print(número, "x", i, "=", result)

 número = int(input("Insira o número para exibir sua tabuada:"))
 i=0
 while i<=10:
     print(número, "x", i, "=",número*i)
     i+=1

#nested loop tabuada de 1 a 10:
linha = 1
coluna = 1
while linha<=10:
    while coluna <=10:
        print(linha*coluna, end = "\t")
        coluna+=1
    linha+=1
    print()
    coluna=1
