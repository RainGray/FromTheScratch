import scripts
import game_exceptions as ex

HERO = {}


def hello_function():
    print('welcome, player')
    hero_name = input('Tell me the name of your hero: \n\r')
    HERO['name'] = hero_name
    print(f'Hello HERO: {HERO["name"]}')


def run_time_game():
    current_dialog = 'dialog_001'
    while True:
        try:
            scripts.play_current_dialog(current_dialog)
        except ex.InvalidDialogNameExeption:
            current_dialog = 'dialog_001'
            continue
        player_reply = input()
        if player_reply == 'exit':
            print(f'See you {HERO["name"]}')
            break
        try:
            next_dialog = scripts.get_next_dialog(
                current_dialog=current_dialog,
                users_answer=player_reply if player_reply else None
            )
            current_dialog = next_dialog
        except ex.WrongAnswerExeption:
            print('Wrong answer!!! Choose right answer!!!')


if __name__ == '__main__':
    hello_function()
    run_time_game()
