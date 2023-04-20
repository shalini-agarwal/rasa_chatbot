# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []



from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionExtractAnswer(Action):

    def name(self) -> Text:
        return "action_extract_answer"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_response_enta = False
        user_response_entb = False
        use_type = tracker.get_slot('use_type')
        info_type = tracker.get_slot('info_type')
        if use_type == 'illegal' or use_type == 'misuse' or use_type == 'stealing' or use_type == 'unauthorized' or use_type == 'illicitly' or use_type == 'steals':
            user_response_enta = True
        if info_type == 'personal information':
            user_response_entb = True
        if user_response_enta and user_response_entb:
            dispatcher.utter_message(text="That's right!")
        else:
            dispatcher.utter_message(text="You have got something wrong there. Identity theft occurs when someone misuses or steals your personal information for fradulent activity.")
        return []