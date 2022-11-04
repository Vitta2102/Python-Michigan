#Programa para encontrar o maior e o menor valor da uma sequência de números
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        value = int(num)
        if largest is None:
            largest = value
        elif value > largest:
            largest = value
        elif smallest is None:
            smallest = value
        elif value < smallest:
            smallest = value
    except:
        print('Invalid input')      
print("Maximum is", largest)
print("Minimum is", smallest)