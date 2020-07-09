#define a simple function with def key word
def helloPrint():
    print("hello from my first function")
# call the function to run the code in a function
helloPrint()
#=====================================
# Simple function with one parameter
def message(name):
    print("Hello : "+name+" from my function")
name="max"
message(name)
# Functions can have more than one parameter
def sum(a,b):
    sum_of_num=a+b
    print(sum_of_num)
sum(23,23)
# Functions can have more than one parameter and return a value
def prodcuct(a,b):
    product_of_num=a*b
    return product_of_num
    
sum(23,23)
print(prodcuct(1,2))
#=========================
#even odd finder function
def evenoddFinder(number):
    if number%2==0:
        return "even"
    else:
        return "odd"

number=int(input("enter a number: "))
print(evenoddFinder(n))