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

