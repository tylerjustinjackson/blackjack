
from random import choice
from blackjackart import art
import time

choices = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10,  # all cards in deck
           10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]


def calcwin(userhand, computerhand):  # calculates win based on scores and blackjack rules

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


def finalcalc(userhand, computerhand):  # if user does not hit, final score calculations

    if total(userhand) > total(computerhand):
        winner()
        playagain()

    elif total(computerhand) > total(userhand):
        computerwin()
        playagain()

    else:
        draw()
        playagain()


def main():  # main gameplay

    computerhand = []
    userhand = []
    computerhand, userhand = starthand(computerhand, userhand)

    print('')  # prints hands to terminal
    print(f'''Your hand: {userhand} 
Total: {total(userhand)}
''')
    print(f'''Computer hand: {computerhand}
{total(computerhand)}''')
    x = calcwin(userhand, computerhand)
    if x == True:
        playagain()

    while True:  # loops through gameplay, until someone wins

        print('')
        x = input('Do you want to hit? (Y/N) ').strip().lower()
        print("")
        print('')

        if x == 'y' or x == 'yes':  # if you want to hit...
            userhand = addmove(userhand)
            win = calcwin(userhand, computerhand)

            if win == True:  # if someone wins
                print(f'''Your hand: {userhand}
Total: {total(userhand)}
''')
                print(f'''Computer hand: {computerhand}
Total: {total(computerhand)}''')
                playagain()  # play again?
                break

            else:  # if no one wins yet
                computerhand = addmove(computerhand)  # computer moves
                print(f'''Your hand: {userhand}
Total: {total(userhand)}
''')
                print(f'''Computer hand: {computerhand}
Total: {total(computerhand)}
''')
                win = calcwin(userhand, computerhand)  # see if there is a win

                if win == True:  # if win

                    print(f'''Your hand: {userhand}
Total: {total(userhand)}
''')
                    print(f'''Computer hand: {computerhand}
{total(computerhand)}''')
                    playagain()  # play again?
                    break

        elif x == 'n' or x == 'no':  # if user does not hit

            if total(computerhand) <= 17:  # if computer score is not over 17
                computerhand = addmove(computerhand)  # computer move
                print(f'''Your hand: {userhand}
Total: {total(userhand)}
''')
                print(f'''Computer hand: {computerhand}
{total(computerhand)}
''')
                x = calcwin(userhand, computerhand)  # calc
                if x == False:  # see who scored higher
                    finalcalc(userhand, computerhand)
                    break
                playagain()  # play again?
                break

            else:

                finalcalc(userhand, computerhand)
                break


def playagain():  # play again function
    print('')

    while True:

        again = input(
            "Would you like to play Black Jack again? (Y/N) ").strip().lower()

        if again == 'y' or again == 'yes':  # if want to play again....
            print('')
            main()
            break

        elif again == 'n' or again == 'no':  # if done with game
            time.sleep(1)
            print('OKAY! TAKE CARE!!!')
            print(art)
            exit()  # exit program
            break

        else:
            # put in right input before moving on
            print('Invalid input...', end='')
            continue


def computerwin():  # computer win function
    print('HARD LUCK! THE COMPUTER BEAT YOU!')
    print('')


def draw():  # tie function
    print('FAIR GAME! YOU AND THE COMPUTER TIED!')
    print('')


def winner():  # user win function
    print('CONGRATS YOU\'RE A WINNER!')
    print('')


def addmove(y):  # user/computer move function
    y.append(choice(choices))
    return y


def starthand(c, u):  # starting hands function

    for _ in range(2):

        c.append(choice(choices))
        u.append(choice(choices))

    return c, u


def total(list):  # adds up all values of list

    r = 0

    for i in list:
        r += i

    return r


if __name__ == '__main__':  # main running code

    try:
        print(art)
        print('')
        first = input('Do you want to play BlackJack? (Y/N) ').strip().lower()

        if first == 'y' or first == 'yes':  # if want to play...
            time.sleep(1)
            main()

        elif first == 'n' or first == 'no':  # if you do not want to play...
            time.sleep(1)
            print('Okay! Take care!!!')

    except:
        pass
