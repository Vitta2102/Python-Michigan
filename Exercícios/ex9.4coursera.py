#Programa para identificar a palavra que mais aparece e quantas vezes aparece em um determiando documento
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

#"Puxar" a segunda palavra de cada linha iniciada pela palavra "From". (E-mail que mais aparece)
#O dicionário counts armazena cada um dos e-mails e conta quantas vezes ele aparece
counts = dict()
for line in handle:
    if line.startswith('From '):
        word = line.split()
        word = word[1]
        counts[word] = counts.get(word, 0) + 1
        
bigcount = None
bigword = None

for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)
print(counts)