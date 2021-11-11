import random


def check_win(user, computer):
    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        return print(f"Yay! you won! computer Choice is {computer}")
    return print(f"You lost! computer Choice is {computer}")


def rock_paper_scissors():
    player = input("What is your choice - 'r' for rock, 's' for scissor, 'p' for paper: ").lower()
    choices = ['r', 's', 'p']
    opponent = random.choice(choices)

    if player not in choices:
        print('The choice is wrong')
        return rock_paper_scissors()

    if player == opponent:
        return print(f"Its a Tie! computer Choice is {opponent}")
    return check_win(player, opponent)


rock_paper_scissors()
