def readFile(typeOfReading, fileName):
    try:

        if typeOfReading == 1:
            with open(fileName, 'r') as file:
                content = file.read()
            print(content)
        elif typeOfReading == 2:
            with open(fileName, 'r') as file:
                for line in file:
                    print(line)

    except FileNotFoundError:
        print("Файл не существует")

readFile(1, './lab3/example.txt')
readFile(2, './lab3/example.txt')

def WriteFile(fileName):
    
    text = input("Введите текст для добавления в файл:")
    with open(fileName, 'a') as f:
        f.write(text)

WriteFile('./lab3/user_input.txt')

