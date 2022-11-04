#Ler valores de horas e taxa e passar para o formato float
hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)

#Estrutura condiconal para estimar o valor a ser pago se as horas forem maiores do que 40
if h > 40:
    rayte = r * h
    bla = (h - 40.0) * (r * 0.5)
    final = rayte + bla
else:
    final = h * r

print(final)



