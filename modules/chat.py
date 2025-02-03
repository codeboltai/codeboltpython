import json
import asyncio
from modules.websocket import cbws_instance
from asyncio import Event

class CustomEventEmitter:
    def __init__(self):
        self.events = {}

    def on(self, event_name, callback):
        if event_name not in self.events:
            self.events[event_name] = []
        self.events[event_name].append(callback)

    def emit(self, event_name, *args):
        if event_name in self.events:
            for callback in self.events[event_name]:
                callback(*args)

event_emitter = CustomEventEmitter()

class CBChat:
    async def get_chat_history(self):
        """
        Retrieves the chat history from the server.
        :return: A promise that resolves with an array of ChatMessage objects representing the chat history.
        """
        websocket = cbws_instance.get_websocket()
        await websocket.send(json.dumps({
            "type": "getChatHistory"
        }))
        async for message in websocket:
            response = json.loads(message)
            if response.get("type") == "getChatHistoryResponse":
                return response

    def on_action_message(self):
        """
        Sets up a listener for incoming WebSocket messages and emits a custom event when a message is received.
        :return: The event emitter used for emitting custom events.
        """
        websocket = cbws_instance.get_websocket()
        if not websocket:
            return
        websocket.on('message', lambda data: self._handle_message(data))
        return event_emitter

    def _handle_message(self, data):
        response = json.loads(data)
        if response.get("type") == "messageResponse":
            event_emitter.emit("userMessage", response, lambda message: self._process_stopped(message))

    def _process_stopped(self, message):
        print("Callback function invoked with message:", message)
        websocket = cbws_instance.get_websocket()
        websocket.send(json.dumps({
            "type": "processStoped"
        }))

    async def send_message(self, message, payload):
        """
        Sends a message through the WebSocket connection.
        :param message: The message to be sent.
        """
        print(message)
        websocket = cbws_instance.get_websocket()
        await websocket.send(json.dumps({
            "type": "sendMessage",
            "message": message,
            "payload": payload
        }))

    async def wait_for_reply(self, message):
        """
        Waits for a reply to a sent message.
        :param message: The message for which a reply is expected.
        :return: A promise that resolves with the reply.
        """
        websocket = cbws_instance.get_websocket()
        await websocket.send(json.dumps({
            "type": "waitforReply",
            "message": message
        }))
        async for message in websocket:
            response = json.loads(message)
            if response.get("type") == "waitFormessageResponse":
                return response

    def process_started(self):
        """
        Notifies the server that a process has started and sets up an event listener for stopProcessClicked events.
        :return: An object containing the event emitter and a stopProcess method.
        """
        websocket = cbws_instance.get_websocket()
        websocket.send(json.dumps({
            "type": "processStarted"
        }))
        websocket.on('message', lambda data: self._handle_process_message(data))
        return {
            "event": event_emitter,
            "stopProcess": self.stop_process
        }

    def _handle_process_message(self, data):
        message = json.loads(data)
        print("Received message:", message)
        if message.get("type") == 'stopProcessClicked':
            event_emitter.emit("stopProcessClicked", message)

    def stop_process(self):
        """
        Stops the ongoing process.
        Sends a specific message to the server to stop the process.
        """
        print("Stopping process...")
        websocket = cbws_instance.get_websocket()
        websocket.send(json.dumps({
            "type": "processStoped"
        }))

    def process_finished(self):
        """
        Stops the ongoing process.
        Sends a specific message to the server to stop the process.
        """
        print("Process Finished ...")
        websocket = cbws_instance.get_websocket()
        websocket.send(json.dumps({
            "type": "processFinished"
        }))

    async def send_confirmation_request(self, confirmation_message, buttons=None, with_feedback=False):
        """
        Sends a confirmation request to the server with two options: Yes or No.
        :return: A promise that resolves with the server's response.
        """
        if buttons is None:
            buttons = []
        websocket = cbws_instance.get_websocket()
        await websocket.send(json.dumps({
            "type": "confirmationRequest",
            "message": confirmation_message,
            "buttons": buttons,
            "withFeedback": with_feedback
        }))
        async for message in websocket:
            response = json.loads(message)
            if response.get("type") in ["confirmationResponse", "feedbackResponse"]:
                return response

    async def ask_question(self, question, buttons=None, with_feedback=False):
        """
        Sends a question to the server with options for response.
        :return: A promise that resolves with the server's response.
        """
        if buttons is None:
            buttons = []
        websocket = cbws_instance.get_websocket()
        await websocket.send(json.dumps({
            "type": "confirmationRequest",
            "message": question,
            "buttons": buttons,
            "withFeedback": with_feedback
        }))
        async for message in websocket:
            response = json.loads(message)
            if response.get("type") in ["confirmationResponse", "feedbackResponse"]:
                return response

    def send_notification_event(self, notification_message, event_type):
        """
        Sends a notification event to the server.
        :param notification_message: The message to be sent in the notification.
        :param event_type: The type of event.
        """
        websocket = cbws_instance.get_websocket()
        websocket.send(json.dumps({
            "type": "notificationEvent",
            "message": notification_message,
            "eventType": event_type
        }))

cbchat = CBChat()
