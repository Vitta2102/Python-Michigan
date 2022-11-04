#Programa para identificar, separar as duas primeiras casas decimais e ordenar os valores em horas em um documento
#Contar quantas vezes aparece cada "hora"
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
    if line.startswith('From '):
        numb = line.split()
        numb = numb[5]
        numb = numb[:2]
        counts[numb] = counts.get(numb, 0) + 1

lst = list()
for numb,count in counts.items():
    tup = (numb, count)
    lst.append(tup)
    lst = sorted(lst)

for x,y in lst:
    print(x,y)
    