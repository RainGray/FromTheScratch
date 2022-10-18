import dialogs

DIALOGS = {
    'dialog_001': dialogs.dialog_001,
    'dialog_002': dialogs.dialog_002,
    'dialog_003': dialogs.dialog_003,
}

def continue_the_dialog(next_dialog=None):
    _next_dialog = ''
    if not next_dialog:
        _next_dialog = 'dialog_001'
    if next_dialog in DIALOGS.keys():
        _next_dialog = next_dialog
    if not _next_dialog:
        raise Exception('invalid dialog name')

    print(DIALOGS[_next_dialog]['text'])
    print(DIALOGS[_next_dialog]['question'])
    counters_for_this_dialog = {'exit': 'exit'}
    for reply in DIALOGS[_next_dialog]['replys']:
        print(reply['counter'], ':', reply['text'])
        counters_for_this_dialog[reply['counter']] = reply['next_dialog']

    player_input = input()
    while not player_input in counters_for_this_dialog:
        print('invalid choise. Pick another line number.')
        player_input = input()

    return counters_for_this_dialog[player_input]




