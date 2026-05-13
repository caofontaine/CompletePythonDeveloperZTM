import sys

from random import randint

random_num = randint(int(sys.argv[1]), int(sys.argv[2]))

while True:
    try:
        number = int(input('Enter a number within your boundaries: '))
        if number >= int(sys.arv[1]) and number <= int(argv[2]):
            print('All Gucci')
            if number == random_num:
                print('Winner, winner, chicken dinner!')
                break
    except ValueError:
        print("Please enter a number")
        continue