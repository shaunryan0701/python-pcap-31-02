try:
    stream = open('animals.txt', 'a')
    stream.write('This is the first message\n')
    stream.write('This is the second message\n')
    stream.close()
except Exception as e:
    print('An error has occurred:', e)
