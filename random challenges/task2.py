import sys

def find4expression(n):
    ops = ["+", "-", "*", "//"]
    for op1 in ops:
        for op2 in ops:
            for op3 in ops:
                expression = "4 {} 4 {} 4 {} 4".format(op1, op2, op3)
                if eval(expression) == n:
                    return expression.replace("//", "/") + " = " + str(n)
    return "no solution"
    

once = 0 
for line in sys.stdin:
    if once == 1:
        print(find4expression(int(line)))
    once = 1

