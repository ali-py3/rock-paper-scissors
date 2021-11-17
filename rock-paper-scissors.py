import random


def check_win(user, computer):
    if (user == 'rock' and computer == 'scissor') or (user == 'scissor' and computer == 'paper') or \
            (user == 'paper' and computer == 'rock'):
        return print(f"Yay! you won! computer Choice is {computer}")
    return print(f"You lost! computer Choice is {computer}")


def rock_paper_scissors():
    player = input("What is your choice - 'r' for rock, 's' for scissor, 'p' for paper: ").lower()
    choices = ['rock', 'scissor', 'paper']
    opponent = random.choice(choices)

    if player == 'r':
        player = "rock"
    if player == 's':
        player = "scissor"
    if player == 'p':
        player = "paper"

    if player not in choices:
        print('The choice is wrong')
        return rock_paper_scissors()
    if player == opponent:
        return print(f"Its a Tie! computer Choice is {opponent}")

    return check_win(player, opponent)


rock_paper_scissors()
