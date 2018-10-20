'''
Written by Debojit Kaushik  (Timestamp)
'''
import os
import sys
import traceback

class Action:
    @staticmethod
    def get_action(intent_data):
        try:
            action_dic = None
            print("Here", intent_data)
            if intent_data["topScoringIntent"]["intent"] == "add_function":
                action_dic = {
                    "status": "Function Creation Returned",
                    "action": "add_fun",
                    "data": {
                        "func_name": [i["entity"] for i in intent_data["entities"] if i["type"] == "function_name"][0],
                        "args": [i["entity"] for i in intent_data["entities"] if i["type"] == "argument"]
                    }
                }
            print(action_dic)
            return action_dic
        except Exception:
            print(traceback.format_exc())



if __name__ == '__main__':
    try:
        pass #Write here.
    except Exception:
        print(traceback.format_exc())