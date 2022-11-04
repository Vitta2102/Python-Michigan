#Programa para printar uma parte específica em uma determinada frase
text = "X-DSPAM-Confidence:    0.8475"
pos = text.find('0.8475')
text2 = (text[pos:29])
fext = float(text2)
print(fext)