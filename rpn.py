#!/usr/bin/env python3

import operator

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}

def summation(stack):
    stack.append(sum(stack))

def rotate(stack):
    stack.reverse()

def copy(stack):
    temp = stack.pop()
    stack.append(temp)
    stack.append(temp)

commands = {
    "sum": summation,
    "rot": rotate,
    "copy": copy,
}

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            if operators.has_key(token):
                function = operators[token]
                arg2 = stack.pop()
                arg1 = stack.pop()
                result = function(arg1, arg2)
                stack.append(result)
            else:
                function = commands[token]
                function(stack)
        print(stack)
    print("")
    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        print("Result: ", result)

if __name__ == '__main__':
    main()
