# userplay function
from random import choice
from blackjackart import art
import time

choices = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10,
           10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]


def calcwin(userhand, computerhand):

    if total(userhand) == 21 and total(computerhand) == 21:
        print('')
        draw()
        return True

    elif total(userhand) == 21:
        print('')
        winner()
        return True

    elif total(computerhand) == 21:
        print('')
        computerwin()
        return True

    elif total(userhand) > 21:
        print('')
        computerwin()
        return True

    elif total(computerhand) > 21:
        print('')
        winner()
        return True

    else:
        return False


def finalcalc(userhand, computerhand):

    if total(userhand) > total(computerhand):
        winner()
        playagain()

    elif total(computerhand) > total(userhand):
        computerwin()
        playagain()

    else:
        draw()
        playagain()


def main():

    computerhand = []
    userhand = []
    computerhand, userhand = starthand(computerhand, userhand)

    print('')
    print(f'''Your hand: {userhand}
Total: {total(userhand)}
''')
    print(f'''Computer hand: {computerhand}
{total(computerhand)}''')
    x = calcwin(userhand, computerhand)
    if x == True:
        playagain()

    while True:

        print('')
        x = input('Do you want to hit? (Y/N) ').strip().lower()
        print("")
        print('')

        if x == 'y' or x == 'yes':
            userhand = addmove(userhand)
            win = calcwin(userhand, computerhand)

            if win == True:
                print(f'''Your hand: {userhand}
Total: {total(userhand)}
''')
                print(f'''Computer hand: {computerhand}
Total: {total(computerhand)}''')
                playagain()
                break

            else:
                computerhand = addmove(computerhand)
                print(f'''Your hand: {userhand}
Total: {total(userhand)}
''')
                print(f'''Computer hand: {computerhand}
Total: {total(computerhand)}
''')
                win = calcwin(userhand, computerhand)

                if win == True:

                    print(f'''Your hand: {userhand}
Total: {total(userhand)}
''')
                    print(f'''Computer hand: {computerhand}
{total(computerhand)}''')
                    playagain()
                    break

        elif x == 'n' or x == 'no':

            if total(computerhand) <= 17:
                computerhand = addmove(computerhand)
                print(f'''Your hand: {userhand}
Total: {total(userhand)}
''')
                print(f'''Computer hand: {computerhand}
{total(computerhand)}
''')
                x = calcwin(userhand, computerhand)
                if x == False:
                    finalcalc(userhand, computerhand)
                    break
                playagain()
                break

            else:

                finalcalc(userhand, computerhand)
                break


def playagain():
    print('')

    while True:

        again = input(
            "Would you like to play Black Jack again? (Y/N) ").strip().lower()

        if again == 'y' or again == 'yes':
            print('')
            main()
            break

        elif again == 'n' or again == 'no':
            time.sleep(1)
            print('OKAY! TAKE CARE!!!')
            print(art)
            exit()

            break

        else:
            print('Invalid input...', end='')
            continue


def computerwin():
    print('HARD LUCK! THE COMPUTER BEAT YOU!')
    print('')


def draw():
    print('FAIR GAME! YOU AND THE COMPUTER TIED!')
    print('')


def winner():
    print('CONGRATS YOU\'RE A WINNER!')
    print('')


def addmove(y):
    y.append(choice(choices))
    return y


def starthand(c, u):

    for _ in range(2):

        c.append(choice(choices))
        u.append(choice(choices))

    return c, u


def total(list):

    r = 0

    for i in list:
        r += i

    return r


if __name__ == '__main__':

    try:
        print(art)
        print('')
        first = input('Do you want to play BlackJack? (Y/N) ').strip().lower()

        if first == 'y' or first == 'yes':
            time.sleep(1)
            main()

        elif first == 'n' or first == 'no':
            time.sleep(1)
            print('Okay! Take care!!!')

    except:
        pass
