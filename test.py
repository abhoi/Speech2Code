from message_broker import MessageBroker
import json


for item in range(10):
    MessageBroker.send_message("py_to_js", json.dumps({"New Message": item}))