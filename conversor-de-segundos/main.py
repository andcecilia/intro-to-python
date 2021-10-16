segundos = int(input("Por favor, entre com o número de segundos que deseja converter:"))
a = segundos//86400
segundos_restantes = segundos%86400
b = segundos_restantes//3600
segundos_remanescentes = segundos%3600
c = segundos_remanescentes//60
d = segundos%60
print(a,"dias", b, "horas", c, "minutos e", d, "segundos.")