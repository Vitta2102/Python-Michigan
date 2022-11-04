#Abrir arquivo
fname = input("Enter file name: ")
fh = open(fname)
x = 0
total = 0

#Estrutura de repetição para percorrer as linhas do arquivo que comecem com a frase passada no método
#Variável x é um contador para a quantidade de linhas que começam com a frase passada no método
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    print(line)
    x = x + 1
    fline = float(line[20:])
    total = total + fline
print(x)
print(total)
print("Average spam confidence:", total/x)      
print("Done")
