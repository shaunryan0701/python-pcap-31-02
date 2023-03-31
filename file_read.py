try:
    stream = open('animals.txt')
    character = stream.read(100)
    stream.close()
except Exception as e:
    print('An Error has occurred', e)

print(character)


try:
    stream = open('animals.txt')
    print(stream.read(1000))
    print(stream.read(100))
    stream.close()
except Exception as e:
    print('An Error has occurred', e)

try:
    stream = open('animals.txt')
    character = stream.read(1)
    while character != '':
      print(character, end='-')
      character = stream.read(1)
    
    stream.close()
except Exception as e:
    print('An Error has occurred', e)

try:
    stream = open('animals.txt')
    line = stream.readline()
    while line != '':
      print(line, end='.')
      line = stream.readline()
    
    stream.close()
except Exception as e:
    print('An Error has occurred', e)


# read()
from os import strerror

try:
    cnt = 0
    s = open('text.txt', "rt")
    content = s.read()
    for ch in content:
        print(ch, end='')
        cnt += 1
    s.close()
    print("\n\nCharacters in file:", cnt)
except IOError as e:
    print("I/O error occurred: ", strerr(e.errno))

# readline()
from os import strerror

try:
    ccnt = lcnt = 0
    s = open('text.txt', 'rt')
    line = s.readline()
    while line != '':
        lcnt += 1
        for ch in line:
            print(ch, end='')
            ccnt += 1
        line = s.readline()
    s.close()
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

