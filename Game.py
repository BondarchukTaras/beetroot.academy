import random
print(' Let`s play rock, paper, scissors')
player = input('Choose rock, paper, scissors, by r, p or s: ')
if player == 'r' or player == 'p' or player == 's':
    computer = random.randint(1, 3)
    # 1 == r
    # 2 == p
    # 3 == s
    if (computer == 1 and player == 'r' or computer == 2 and player == 'p' or computer == 3 and player == 's'):
        print('It is draw')
    elif (computer == 1 and player == 'p' or computer == 2 and player == 's' or computer == 3 and player == 'r'):
        print('You WIN!')
    else:
        print('You los!')
else:
    print('Yor input was in format, no game for you')

