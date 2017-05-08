import os

NumberOfDirectories = input('How many directories do you want to create? ')

for i in range(1, int(NumberOfDirectories) + 1):
    path = './bible_text/' + str(i)
    os.makedirs(path)
