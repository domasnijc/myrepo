import math as m
import datetime
import my_module
import my_package.math
import my_package.strings
def square(number):
    print(m.sqrt(number))

square(144)

def dateTime():
    print(datetime.datetime.now())

dateTime()

def getSum(num1, num2):
    print(my_module.sum(num1, num2))

getSum(5, 2)

def checkPackage():
    print(my_package.math.max_of_two(1, 8))
    print(my_package.math.square(8))
    print(my_package.math.is_prime(12))
    print(my_package.strings.length("kdankwud"))
    print(my_package.strings.add("abc", "def"))
checkPackage()