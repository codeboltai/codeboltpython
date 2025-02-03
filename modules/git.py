import json
import asyncio
import websockets

async def git_init(path):
    async with websockets.connect('ws://localhost:your_websocket_port') as websocket:
        message = {
            "type": "gitEvent",
            "action": "Init",
            "path": path
        }

        await websocket.send(json.dumps(message))
        async for response in websocket:
            response_data = json.loads(response)
            if response_data.get("type") == "InitResponse":
                return response_data

async def clone_repo(url, path):
    async with websockets.connect('ws://localhost:your_websocket_port') as websocket:
        message = {
            "type": "gitEvent",
            "action": "Clone",
            "url": url,
            "path": path
        }

        await websocket.send(json.dumps(message))
        async for response in websocket:
            response_data = json.loads(response)
            if response_data.get("type") == "CloneResponse":
                return response_data