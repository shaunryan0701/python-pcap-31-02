try:
    stream = open('animals.txt', 'a')
    stream.write('This is the first message\n')
    stream.write('This is the second message\n')
    stream.close()
except Exception as e:
    print('An error has occurred:', e)

# stderror
from os import strerror

try:
    fo = open('newtext.txt', 'wt')
    for i in range(10):
        fo.write("line #" + str(i+1) + "\n")
    fo.close()
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))

# byte array
data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 - i

for b in data:
    print(hex(b))