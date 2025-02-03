import asyncio
import websockets
import yaml
import os

class CBWS:
    def __init__(self):
        self.websocket = None
        self.unique_connection_id = self.get_unique_connection_id()
        self.initial_message = self.get_initial_message()
        self.loop = asyncio.get_event_loop()
        self.loop.run_until_complete(self.initialize_websocket())

    def get_unique_connection_id(self):
        try:
            with open('./codeboltagent.yaml', 'r') as file:
                data = yaml.safe_load(file)
                return data.get('unique_connectionid', '')
        except FileNotFoundError:
            print('Unable to locate codeboltagent.yaml file.')
            return ''

    def get_initial_message(self):
        try:
            with open('./codeboltagent.yaml', 'r') as file:
                data = yaml.safe_load(file)
                return data.get('initial_message', '')
        except FileNotFoundError:
            print('Unable to locate codeboltagent.yaml file.')
            return ''

    async def initialize_websocket(self):
        agent_id_param = f"&agentId={os.getenv('agentId')}" if os.getenv('agentId') else ''
        parent_id_param = f"&parentId={os.getenv('parentId')}" if os.getenv('parentId') else ''
        dev_param = '&dev=true' if os.getenv('Is_Dev') else ''
        uri = f"ws://localhost:{os.getenv('SOCKET_PORT')}/codebolt?id={self.unique_connection_id}{agent_id_param}{parent_id_param}{dev_param}"

        try:
            async with websockets.connect(uri) as websocket:
                self.websocket = websocket
                print('WebSocket connected')
                # Uncomment the following lines to send the initial message
                # await websocket.send(json.dumps({
                #     "type": "sendMessage",
                #     "message": self.initial_message
                # }))
                # Handle incoming messages
                async for message in websocket:
                    # Handle incoming WebSocket messages here.
                    # print('WebSocket message received:', message)
                    pass
        except Exception as e:
            print("WebSocket connection failed:", e)

    def get_websocket(self):
        if not self.websocket or self.websocket.closed:
            raise Exception('WebSocket is not open')
        return self.websocket

# Create an instance of the CBWS class
cbws_instance = CBWS()
