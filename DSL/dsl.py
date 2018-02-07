import sys
import importlib

# The program expects the dsl file as an argument
if len(sys.argv) != 2:
    print('usage: %s <dsl file>' % sys.argv[0])
    sys.exit(1)

with open(sys.argv[1], 'r') as script:
    for expression in script:
        expression = expression.strip()
        # For Skipping comments
        if not expression or expression[0] == '#':
            continue
        parts = expression.split()
        mod = importlib.import_module("module1")
        print(expression, " equals to ",getattr(mod, parts[1])(parts[0], parts[2]))

