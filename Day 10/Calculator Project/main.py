def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

def mod(n1, n2):
    return n1 % n2

functions_dic = {"+" : add, "-" : sub, "*" : mult, "/" : div, "%" : mod}

num1 = int(input("First number:\t"))
operation_str = input("operation (+,-,*,/,%):\t")
num2 = int(input("Second number:\t"))

print(f"{num1} {operation_str} {num2} = {functions_dic[operation_str](num1, num2)}")
