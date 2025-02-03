import json
import asyncio
import websockets

async def get_project_path():
    async with websockets.connect('ws://localhost:your_websocket_port') as websocket:
        request = {
            "type": "settingEvent",
            "action": "getProjectPath"
        }
        await websocket.send(json.dumps(request))
        async for response in websocket:
            response_data = json.loads(response)
            if response_data.get("type") == "getProjectPathResponse":
                return response_data

async def run_project():
    async with websockets.connect('ws://localhost:your_websocket_port') as websocket:
        request = {"type": "runProject"}
        await websocket.send(json.dumps(request))