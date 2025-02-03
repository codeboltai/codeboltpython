import json
from modules.websocket import cbws_instance

class DBMemory:
    async def add_knowledge(self, key, value):
        """
        Adds a key-value pair to the in-memory database.
        :param key: The key under which to store the value.
        :param value: The value to be stored.
        :return: A promise that resolves with the response from the memory set event.
        """
        websocket = cbws_instance.get_websocket()
        await websocket.send(json.dumps({
            "type": "memoryEvent",
            "action": "set",
            "key": key,
            "value": value
        }))
        async for message in websocket:
            response = json.loads(message)
            if response.get("type") == "memorySetResponse":
                return response

    async def get_knowledge(self, key):
        """
        Retrieves a value from the in-memory database by key.
        :param key: The key of the value to retrieve.
        :return: A promise that resolves with the response from the memory get event.
        """
        websocket = cbws_instance.get_websocket()
        await websocket.send(json.dumps({
            "type": "memoryEvent",
            "action": "get",
            "key": key
        }))
        async for message in websocket:
            response = json.loads(message)
            if response.get("type") == "memoryGetResponse":
                return response

dbmemory = DBMemory()
