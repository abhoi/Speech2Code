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
                "add_variables",
                "add_class",
                "add_try_catch",
                "save_file",
                "run_file",
                "add_newline"
            ]
            intent = intent_data["topScoringIntent"]["intent"]
            print(intent)
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
                        "status": "If-else Block Created",
                        "action": "add_if_else",
                        "data": {
                            "args": []
                        }
                    }
                elif intent == "add_main":
                    action_dic = {
                        "status": "Main Function Created",
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
                    #Here
                elif intent == "add_breakpoint":
                    action_dic = {
                        "status": "Breakpoint added.",
                        "action": "add_breakpoint",
                        "data": {
                            "args": []
                        }
                    }
                elif intent == "add_class":
                    action_dic = {
                        "status": "class added/created.",
                        "action": "add_class",
                        "data": {
                            "args": [{"entity": item['entity'], "type": item['type']} for item in intent_data['entities']]
                        }
                    }
                elif intent == "add_newline":
                    action_dic = {
                        "status": "NewLine inserted.",
                        "action": "add_newline",
                        "data": {
                            "args": []
                        }
                    }
                elif intent == "add_try_catch":
                    action_dic = {
                        "status": "Exception Handling block added.",
                        "action": "add_try_catch",
                        "data": {
                            "args": []
                        }
                    }
                elif intent == "delete_line":
                    action_dic = {
                        "status": "Line Removed",
                        "action": "delete_line",
                        "data": {
                            "args": []
                        }
                    }
                elif intent == "run_file":
                    action_dic = {
                        "status": "Running script",
                        "action": "run_file",
                        "data": {
                            "args": []
                        }
                    }
                elif intent == "save_file":
                    action_dic = {
                        "status": "Saved script.",
                        "action": "save_file",
                        "data": {
                            "args": []
                        }
                    }
                elif intent == "undo_changes":
                    action_dic = {
                        "status": "Changes reverted back (Undo).",
                        "action": "undo_changes",
                        "data": {
                            "args": []
                        }
                    }
                else:
                    action_dic = {
                        "status": "Invalid query"
                    }
                print(action_dic)
                return action_dic
            else:
                action_dic = {
                        "status": "Invalid query"
                    }
                return action_dic
        except Exception:
            print(traceback.format_exc())