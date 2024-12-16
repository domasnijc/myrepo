


def greet(name):
    print("Здравствуйте, ", name)

def square(number):
    return number**2

def max_of_two(x, y):
    if x > y:
        return x
    elif y > x:
        return y
    else:
        print("Числа равны")

def describe_person(name, age=30):
    print("Ваше имя: ", name, "\nВаш возраст: ", age)

def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True

    else:
        for i in range(2, number - 1):
            if number % i == 0:
                return False
        return True

    
greet("Семён")
square(9)
print(max_of_two(45, 23))
describe_person("Семён", 21)
print(is_prime(3))