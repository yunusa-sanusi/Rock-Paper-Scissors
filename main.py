import random
import sys


name = input('Please enter your name: ').capitalize().strip()

user_score = 0
comp_score = 0


def play_game():
    global user_score
    global comp_score

    while True:
        comp_list = ['Rock', 'Paper', 'Scissors']
        user = input(
            f'Welcome {name}, Please choose an opton : ').capitalize().strip()
        comp = random.choice(comp_list)

        if user in comp_list:
            print(f'{name}: {user} | Computer: {comp}')

            if user == 'Rock' and comp == 'Scissors':
                user_score += 1
                print('You Win!')
                print()
            elif user == 'Rock' and comp == 'Paper':
                comp_score += 1
                print('You Lose!')
                print()
            elif user == 'Paper' and comp == 'Scissors':
                comp_score += 1
                print('You Lose!')
                print()
            elif user == 'Paper' and comp == 'Rock':
                user_score += 1
                print('You Win!')
                print()
            elif user == 'Scissors' and comp == 'Paper':
                user_score += 1
                print('You Win!')
                print()
            elif user == 'Scissors' and comp == 'Rock':
                comp_score += 1
                print('You Lose!')
                print()
            elif user == comp:
                user_score = user_score
                comp_score = comp_score
                print("It's a tie!")
                print()
        else:
            print('Please give a valid input')
            continue

        play_again = input(
            'Do you want to play again? Yes(Y) / No(N): ').capitalize().strip()

        if play_again == 'Yes' or play_again == 'Y':
            play_game()
        elif play_again == 'No' or play_again == 'N':
            print('Game Ended')
            print(f"{name}: {user_score} | Computer: {comp_score}")
            if user_score > comp_score:
                print(f'{name} Wins!')
            elif user_score < comp_score:
                print('Computer Wins!')
            else:
                print("It's a tie")
            sys.exit(0)


play_game()
