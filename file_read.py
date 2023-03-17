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

    