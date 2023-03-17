import sys

for line in sys.stdin:
    if line.rstrip() == 'q':
        break
    print(line)

print('You pressed q so I am quitting')