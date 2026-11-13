# num=int(input("enter a number"))
# if num>1:
#     for i in range(2,int(num**0.5)+1):
#         if(num%i==0):
#             print(num,"is not a prime number")
#             break
#     else:
#         print(f"{num} is a prime number")
# else:
#     print(f"{num} is a prime number")

# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def multiplication(a,b):
#     return a*b
# def division(a,b):
#     if(b!=0):
#         return a/b
#     else:
#         return "Error: Division by zero is not allowed."

# while True:
#     print("select opertaion")
#     print("1 for addition")
#     print("2 for subtraction")
#     print("3 for multiplication")
#     print("4 for division")

#     choice=int(input("enter your choice: "))

#     if (choice== 5):
#         print("exiting the program")
#         break

#     if choice in (1,2,3,4):
#         num1=float(input("enter num1: "))
#         num2=float(input("enter num2: "))

#         if choice== 1:
#             print("result:",add(num1,num2))
#         elif choice== 2:
#             print(num1,"-",num2,"=",sub(num1,num2))
#         elif choice== 3:
#             print("result:",multiplication(num1,num2))
#         elif choice== 4:
#             print("result:",division(num1,num2))
#     else:
#         print("invalid input")

# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#        result=1
#        for i in range(1,n+1):
#            result*=i
#     return result

# n=int(input("enter a number"))
# print(f"factorial of {n} is {factorial(n)}")

# list1=[10,34,5,6,78,90,23,45,67]
# highestnum=0
# for i in range(len(list1)):
#     if list1[i]>highestnum:
#         highestnum=list1[i]
    
# print(f"highest num in the lst is {highestnum}")
