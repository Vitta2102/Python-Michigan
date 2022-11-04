#Estrutura condiconal para printar determinada nota de acordo com o Score
score = input("Enter Score: ")
fcore = float(score)

if fcore > 1.0:
    print("Error")
elif fcore >= 0.9:
    print("A")
elif fcore >= 0.8:
    print("B")
elif fcore >= 0.7:
    print("C")
elif fcore >= 0.6:
    print("D")
else:
    print("F")



