import random
import sys

total_barrels = 90
player_1 = 15
player_2 = 15
barrels = random.sample(range(90), 90)
game_set = random.sample(range(90), 30)
player1_set = random.sample(game_set, 15)
player2_set = [e for e in game_set if not e in player1_set]
player1_field = [player1_set[:5], player1_set[5:10], player1_set[10:]]
player2_field = [player2_set[:5], player2_set[5:10], player2_set[10:]]
for player1_line in player1_field:
    player1_line.sort()
    player1_line.insert(random.randint(0, 4), ' ')
    player1_line.insert(random.randint(0, 5), ' ')
    player1_line.insert(random.randint(0, 6), ' ')
    player1_line.insert(random.randint(0, 7), ' ')
for player2_line in player2_field:
    player2_line.sort()
    player2_line.insert(random.randint(0, 4), ' ')
    player2_line.insert(random.randint(0, 5), ' ')
    player2_line.insert(random.randint(0, 6), ' ')
    player2_line.insert(random.randint(0, 7), ' ')

def field(p):
    if p == 0:
        print('{:-^26}'.format('your card'))
        for line1 in player1_field:
            for n1 in line1:
                print('{0:>2}'.format(n1), end=' ')
            print()
        print('{:-^26}\n'.format('-'))
    if p == 1:
        print('{:-^26}'.format('computers card'))
        for line2 in player2_field:
            for n2 in line2:
                print('{0:>2}'.format(n2), end=' ')
            print()
        print('{:-^26}\n'.format('-'))


def player1_game():
    a = input('cross out the number? (y/n): ')
    if a == 'y':
        if ball in player1_set:
            for l in player1_field:
                try:
                    l.insert(l.index(ball), '><')
                    l.pop(l.index(ball))
                except ValueError:
                    continue
            print('\nOK')
            return 1
        else:
            print('\nGAME OVER')
            sys.exit()
    if a == 'n':
        if ball in player1_set:
            print('\nGAME OVER')
            sys.exit()
        else:
            print('\nOK')


def player2_game():
    if ball in player2_set:
        for i in player2_field:
            try:
                i.insert(i.index(ball), '><')
                i.pop(i.index(ball))
            except ValueError:
                continue
        return 1

for ball in barrels:
    total_barrels -= 1
    print('\nnew a barrel: {} (left: {})\n'.format(ball, total_barrels))
    field(0)
    field(1)
    if player1_game() == 1:
        player1 -= 1
    if player2_game() == 1:
        player2 -= 1
    if player1 == 0:
        print('\nyou won')
        sys.exit()
    if player2 == 0:
        print('\nyou lost')
        sys.exit()
    if total_barrels == 0:
        print('\nthe end')
        sys.exit()