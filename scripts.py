import dialogs
import game_exceptions as ex

DIALOGS = {
    'dialog_001': dialogs.dialog_001,
    'dialog_002': dialogs.dialog_002,
    'dialog_003': dialogs.dialog_003,
}


def play_current_dialog(current_dialog=None):
    """
    Function play current dialog
    :param current_dialog: name of current dialog
    """
    _current_dialog = ''
    if not current_dialog:
        _current_dialog = 'dialog_001'
    if current_dialog in DIALOGS.keys():
        _current_dialog = current_dialog
    if not _current_dialog:
        raise ex.InvalidDialogNameExeption('invalid dialog name')
    print(DIALOGS[_current_dialog]['text'])
    print(DIALOGS[_current_dialog]['question'])
    for reply in DIALOGS[_current_dialog]['replys']:
        print(f"{reply['counter']}: {reply['text']}")


def get_next_dialog(current_dialog: str, users_answer: str) -> str:
    """
    Function return nex dialog by users answer
    :param current_dialog: current_dialog
    :param users_answer: users_answer
    :return: next dialog name
    """
    if current_dialog and users_answer:
        for reply in DIALOGS[current_dialog]['replys']:
            if reply['counter'] == users_answer:
                return reply['next_dialog']
    raise ex.WrongAnswerExeption('Wrong answer!!!')
