from message_broker import MessageBroker
import json

MessageBroker.send_message("ele_to_py", json.dumps({"Name":"Sandeep"}))