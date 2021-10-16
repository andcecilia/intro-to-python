número = int(input("Digite um número para ser verificado se é triangular:"))
n1=1
t=0
while t<número:
	t = n1 * (n1 + 1) * (n1 + 2)
	n1 += 1
print(t, n1)
if t==número:
	print("Esse número é triangular.", número)
else:
	print("Esse número não é triangular.", número)








# n1 = int(input('Entre com o número: '))
# i = 1
# t = 0
# while t < n1:
# 	t = i*(i+1)*(i+2)
# 	i += 1
# print(t,i)
# if t == n1:
# 	print ('O número', n1, 'é triangular')
# else:
# 	print ('O número', n1, 'não é triangular')