def square(number):
    return number**2

def max_of_two(x, y):
    maxNumber = 0
    if x > y:
        return x
    elif y > x:
        return y
    else:
        print("Числа равны")

def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number == 3:
        return True
    else:
        for i in range(2, number - 1):
            if number % i == 0:
                return False
            return True