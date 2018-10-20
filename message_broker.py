'''
Written by Debojit Kaushik  (Timestamp)
'''
import os
import sys
import traceback
import pika
import json

class MessageBroker:
    @staticmethod
    def send_message(queue_ID, json_data={"Message": None}):
        """Method to send/publish messages on the queue."""
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
            channel = connection.channel()
            channel.queue_declare(queue_ID)
            channel.basic_publish(body = json.dumps(json_data), routing_key=queue_ID, exchange = "")
            connection.close()
        except Exception:
            print(traceback.format_exc())

    @staticmethod
    def receive_callback(ch, method, properties, body):
        try:
            print("Recieved:", json.loads(body))
        except Exception:
            print(traceback.format_exc())
            
    @staticmethod
    def recieve_message(queue_ID):
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
            channel = connection.channel()
            channel.queue_declare(queue_ID)
            channel.basic_consume(MessageBroker.receive_callback, queue = queue_ID, no_ack = True)
            channel.start_consuming()
        except Exception:
            print(traceback.format_exc())


# if __name__ == '__main__':
#     try:
#         # print("Hey")
#         message = {"first_name": "Debojit", "last_name": "Kaushik", "Age": 27}
#         MessageBroker.send_message("py_to_js", json_data = json.dumps(message))
#         MessageBroker.recieve_message("py_to_js")
#     except Exception:
#         print(traceback.format_exc())