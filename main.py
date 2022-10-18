import scripts


HERO = {}


def hello_function():
    print('welcome, player')
    hero_name = input('Tell me the name of your hero: \n\r')
    HERO['name'] = hero_name

def run_time_game():
    next_dialog = ''
    while True:
        next_dialog = scripts.continue_the_dialog(next_dialog)
        # print(next_dialog)
        """player_reply = input()
        if player_reply == 'exit':
            print(f'See ya HERO: {HERO}')
            break"""
        if next_dialog == 'exit':
            print(f'See ya HERO: {HERO}')
            break

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    hello_function()
    print(f'Hello HERO: {HERO}')
    run_time_game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
