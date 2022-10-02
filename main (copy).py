# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# # from subscribers import subscriber
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_subscriber"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dispather.utter_message('hello')
#         return []
