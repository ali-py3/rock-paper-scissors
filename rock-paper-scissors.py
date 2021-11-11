import random


def check_win_or_lose(user, computer):
    r = 'rock'
    p = 'paper'
    s = 'scissor'

    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        if computer == 'r':
            return print(f"Yay! you won! Computer Choice is {r}")
        elif computer == 'p':
            return print(f"Yay! you won! Computer Choice is {p}")
        elif computer == 's':
            return print(f"Yay! you won! Computer Choice is {s}")
    if (computer == 'r' and user == 's') or (computer == 's' and user == 'p') or (computer == 'p' and user == 'r'):
        if user == 'r':
            return print(f"You lost! Computer Choice is {p}")
        elif user == 'p':
            return print(f"You lost! Computer Choice is {s}")
        elif user == 's':
            return print(f"You lost! Computer Choice is {r}")

def rock_paper_scissors():
    player = input("What is your choice 'r' for rock, 's' for scissor, 'p' for paper: ").lower()
    choices = ['r', 's', 'p']
    opponent = random.choice(choices)

    if player not in choices:
        print('The choice is wrong')
        return rock_paper_scissors()

    if player == opponent:
        return print(f"Its a Tie! computer Choice is {opponent}")
    return check_win_or_lose(player, opponent)


rock_paper_scissors()
