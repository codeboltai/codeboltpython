import json
import asyncio
import websockets

class CustomEventEmitter:
    def __init__(self):
        self.listeners = {}

    def on(self, event_type, listener):
        if event_type not in self.listeners:
            self.listeners[event_type] = []
        self.listeners[event_type].append(listener)

    def emit(self, event_type, data):
        if event_type in self.listeners:
            for listener in self.listeners[event_type]:
                listener(data)

async def execute_command(command, return_empty_string_on_success=False):
    async with websockets.connect('ws://localhost:your_websocket_port') as websocket:
        await websocket.send(json.dumps({
            "type": "executeCommand",
            "message": command,
            "returnEmptyStringOnSuccess": return_empty_string_on_success
        }))
        async for response in websocket:
            response_data = json.loads(response)
            if response_data.get("type") in ["commandError", "commandFinish"]:
                return response_data

def send_manual_interrupt():
    async def interrupt():
        async with websockets.connect('ws://localhost:your_websocket_port') as websocket:
            await websocket.send(json.dumps({"type": "sendInterruptToTerminal"}))
            async for response in websocket:
                response_data = json.loads(response)
                if response_data.get("type") == "terminalInterrupted":
                    return response_data
    return asyncio.run(interrupt())