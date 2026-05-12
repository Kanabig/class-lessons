import sys

with open(sys.argv[1], 'r') as f:
    content = f.read()
    inputs = content.split()
    print(inputs)

