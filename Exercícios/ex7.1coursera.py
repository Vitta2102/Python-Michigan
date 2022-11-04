#Abrir um arquivo, limpar linhas em branco e printar com letras maiúsculas
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    line = line.rstrip()
    laine = line.upper()
    print(laine)


