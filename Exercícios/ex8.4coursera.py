#Programa para adicionar palavras a uma lista, tendo como base uma arquivo
#A variável check itera no documento e na lista, verificando se as palavras do documento já existem na lista
#O método append adiciona os itens à lista
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    thing = line.rstrip()
    thing = thing.split()
    for check in thing:
        if check in lst:
            continue
        else:
            lst.append(check)
lst.sort()
print(lst)
        
    
    