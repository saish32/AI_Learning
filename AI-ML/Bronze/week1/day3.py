
# import math_operations as mo

# print("Length of string:", mo.string_length("Hello World"))
# print("Reversed string:", end=" ")
# mo.string_reverse("Hello World")
# print()
# print("Is 'madam' a palindrome?", mo.checkpalindrome("madam"))

# def chechevenorodd(num):
#     if num%2==0:
#         return "Even"
#     else:
#         return "Odd"

# def print_even_odd(num):
#     result=chechevenorodd(num)
#     print(f"{num} is {result}")

# print_even_odd(10)




# import math_operations as mo
# num1=10
# num2=5

# print("Addition:", mo.add(num1, num2))
# print("Subtraction:", mo.sub(num1, num2))
# print("Multiplication:", mo.multiplication(num1, num2)) 
# print("Division:", mo.division(num1, num2))

# from math import factorial as m
# print(m(5))



# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)

# def print_fact(n):
#     result=factorial(n)
#     print(f"factorial of {n} is {result}")

# print_fact(5)


#global scope
# c = 10

# def add_numbers():
#     print(c,"inside function")
 
# add_numbers()
# print(c)
    




#local scope
# def add_numbers(a, b):
#     c=a+b
#     return c
# print(c)

# def add_numbers(a, b):
#     c=a+b
#     return c

# print(add_numbers(5, 10))