def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2
while True:
    choice={'+':add,'-':sub,'*':mul,'/':div}
    num1=float(input("What is your first number?"))
    num2=float(input("What is your second number?"))
    print('Select your operation')
    for operation in choice:
        print(operation)
    print('exit')
    operation=input("What operation do you want to do? ")
    if operation in choice:
        calculation=choice[operation](num1, num2)
        print(f"{num1} {operation} {num2} is equal to {calculation}")
    elif operation == 'exit':
        break
    else:
        print("Invalid operation. Please choose a valid operation or type 'exit'.")
   
