# create function its clean and user readble 
# add 
def add(a,b):
    return a + b

# sub 
def sub(a,b):
    return a - b

# Mul
def mul(a,b):
    return a * b

# div
def div(a,b):
    return a / b

# wellcome page 
while True:
    print("\n=== wellcome to our calculator ===")
    dict = {
    1: "addation",
    2: "substraction",
    3: "multiplication",
    4: "divsion",
    5: "exit"
}
    for i,j in dict.items():
        print(f"{i} : {j}")
    choose = int(input("enter your choice : "))

    if choose == 5:
        print("Thanks for using our calculator")
        break

    num1 = int(input("enter number 1 : "))
    num2 = int(input("enter number 2 : "))  

    if choose == 1:
        print(f"The addation is {add(num1,num2)}")

    elif choose == 2:
        print(f"The substraction is {sub(num1,num2)}")

    elif choose == 3:
        print(f"The multiplication is {mul(num1,num2)}")

    elif choose == 4:
        print(f"The divison is {div(num1,num2)}")

    

