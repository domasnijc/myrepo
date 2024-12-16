def printNumbers():
    num = int(input("Введите число: "))
    if num >= 1:
        i = 1
        while i <= num:
            print(i)
            i += 1
    else:
        print("Число меньше 1")
        
printNumbers()

def maxNumber():
    num1 = int(input("Введите 1 число: "))
    num2 = int(input("Введите 2 число: "))
    maxNumber = 0
    if num1 > num2:
        maxNumber = num1
    elif num2 > num1:
        maxNumber = num2
    else:
        print("Числа равны")
    print("Большее число: ", maxNumber)

maxNumber()