import sys
import importlib

# The program expects the dsl file as an argument
if len(sys.argv) != 2:
    print('usage: %s <dsl file>' % sys.argv[0])
    sys.exit(1)


def adder(a):
    def added(b):
        return b+a
    return added


def multiply(x):
    """ Implementing multiplication using the above
        adder closure
    """
    def times(y):
        if y == 0:
            return 0
        # Deals with negative numbers
        if y < 0:
            return -1 * adder(x)(multiply(x)(-1 * y - 1))
        return adder(x)(multiply(x)(y-1))
    return times


operator = {"plus": lambda args: str(float(args[0])+float(args[1])),
            "minus": lambda args: str(float(args[0])-float(args[1])),
            "divide_by": lambda args: str(float(args[0])/float(args[1])),
            "times": lambda args: str(float(args[0])*float(args[1])),

            "Plus": lambda args: str(adder(args[0])(args[1])),
            "multiply": lambda args: str(multiply(args[0])(args[1]))
            }

with open(sys.argv[1], 'r') as script:
    for expression in script:
        expression = expression.strip()
        # For Skipping comments
        if not (expression and not (expression[0] == '#')):
            continue
        parts = expression.split()
        mod = importlib.import_module("module1")
        # print(expression, " equals to ", getattr(mod, parts[1])(parts[0], parts[2]))
        print(expression, " equals to ", operator[parts[1]]((int(parts[0]), int(parts[2]))))
