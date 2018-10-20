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
            intents = [
                "add_function",
                "add_if_else",
                "add_main",
                "add_while",
                "goto",
                "call_function",
                "add_variables" 
            ]
            intent = intent_data["topScoringIntent"]["intent"]
            if intent in intents:
                if intent == "add_function":
                    action_dic = {
                        "status": "Function Creation Returned",
                        "action": "add_fun",
                        "data": {
                            "func_name": [i["entity"] for i in intent_data["entities"] if i["type"] == "function_name"][0],
                            "args": [i["entity"] for i in intent_data["entities"] if i["type"] == "argument"]
                        }
                    }
                elif intent == "add_if_else":
                    action_dic = {
                        "status": "Function Creation Returned",
                        "action": "add_if_else",
                        "data": {}
                    }
                elif intent == "add_main":
                    action_dic = {
                        "status": "Function Creation Returned",
                        "action": "add_main",
                        "data": {}
                    }
                elif intent == "add_while":
                    action_dic = {
                        "status": "While statement added.",
                        "action": "add_while",
                        "data": {
                            "args": intent_data["query"]                            
                        }
                    }
                elif intent == "goto":
                    action_dic = {
                        "status": "Go to line/function called.",
                        "action": "goto",
                        "data": {
                            "args": intent_data["entities"][0]["entity"],
                            "type": intent_data["entities"][0]["type"]                         
                        }
                    }
                elif intent == "call_function":
                    action_dic = {
                        "status": "Function called.",
                        "action": "call_function",
                        "data": {
                            "args": [{"entity": item["entity"], "type": item["type"]} for item in intent_data["entities"]]                            
                        }
                    }
                elif intent == "add_variables":
                    action_dic = {
                        "status": "Variable added.",
                        "action": "add_variable",
                        "data": {
                            "args": [{"entity": item['entity'], "type": item['type']} for item in intent_data['entities']]
                        }
                    }
                else:
                    print(intent)
            return action_dic
        except Exception:
            print(traceback.format_exc())



if __name__ == '__main__':
    try:
        pass #Write here.
    except Exception:
        print(traceback.format_exc())