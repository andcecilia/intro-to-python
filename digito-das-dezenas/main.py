número = input("Digite um número inteiro:")
if len(número) > 1:
    dezenas = (len(número)-2)
    content = número[dezenas]
    print("O dígito das dezenas é", content)
else:
    print("O dígito das dezenas é 0")