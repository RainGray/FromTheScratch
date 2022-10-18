

dialog_001 = {
    'text': 'some text',
    'question': 'some question',
    'replys': [
        {
            'next_dialog': 'dialog_002',
            'counter': '1',
            'text': 'go to dialog 2',
        },
        {
            'next_dialog': 'dialog_003',
            'counter': '2',
            'text': 'go to dialog 3',
        },
    ],
}


dialog_002 = {
    'text': 'some text of 002',
    'question': 'some question',
    'replys': [
        {
            'next_dialog': 'dialog_001',
            'counter': '1',
            'text': 'go to beginning',
        },
        {
            'next_dialog': 'dialog_001',
            'counter': '2',
            'text': 'go to dialog 1',
        },
    ],
}


dialog_003 = {
    'text': 'some text of 003',
    'question': 'some question',
    'replys': [
        {
            'next_dialog': 'dialog_001',
            'counter': '1',
            'text': 'go to beginning',
        },
        {
            'next_dialog': 'dialog_001',
            'counter': '2',
            'text': 'go to start',
        },
    ],
}