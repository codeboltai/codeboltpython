import json
import asyncio
import websockets

class DebugLogType:
    INFO = "info"
    ERROR = "error"
    WARNING = "warning"

async def send_debug_log(log, log_type):
    async with websockets.connect('ws://localhost:your_websocket_port') as websocket:
        message = {
            "type": "debugEvent",
            "action": "addLog",
            "message": {
                "log": log,
                "type": log_type
            }
        }

        await websocket.send(json.dumps(message))
        async for response in websocket:
            response_data = json.loads(response)
            if response_data.get("type") == "debugEventResponse":
                return response_data

async def open_debug_browser(url, port):
    async with websockets.connect('ws://localhost:your_websocket_port') as websocket:
        message = {
            "type": "debugEvent",
            "action": "openDebugBrowser",
            "message": {
                "url": url,
                "port": port
            }
        }

        await websocket.send(json.dumps(message))
        async for response in websocket:
            response_data = json.loads(response)
            if response_data.get("type") == "openDebugBrowserResponse":
                return response_data