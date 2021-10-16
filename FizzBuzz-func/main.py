#número = int(input("Digite um número:"))
número = 15
sótrês = "Fizz"
sócinco = "Buzz"
trêsecinco = "FizzBuzz"
def fizzbuzz(número):
    if número % 3 == 0 and número % 5 == 0:
        return trêsecinco
    if número%3==0:
        return sótrês
    elif número%5==0:
        return sócinco
    else:
        return número
fizzbuzz(número)