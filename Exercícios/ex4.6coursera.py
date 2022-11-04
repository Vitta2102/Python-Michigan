#Função para calcular o valor a ser pago de acordo com a taxa e o número de horas
#Estrutura condicional caso as horas sejam maiores que 40
def computepay(h, r):
    if h <= 40:
        sun = h*r
    elif h > 40:
        sun = (40*r + ((h-40)*r)*1.5)
    return sun

hrs = input("Enter Hours:")
hour = float(hrs)
rt = input("Enter Rate:")
rate = float(rt)

p = computepay(hour, rate)
print("Pay", p)