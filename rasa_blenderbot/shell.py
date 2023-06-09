from typing import List, Text
from actions.blenderbot import Talker

if __name__ == '__main__':
    talker = Talker()

    dialog: List[Text] = ['Hello, i am Arty! How are you doing?']
    query: Text = None

    while query != '':
        response = talker(dialog)
        dialog.append(response)

        print(f'bot: {response}')
        
        query = input('usr: ')
        dialog.append(query)
