import json
import asyncio
import websockets

async def get_application_state():
    async with websockets.connect('ws://localhost:your_websocket_port') as websocket:
        await websocket.send(json.dumps({"type": "getAppState"}))
        async for response in websocket:
            response_data = json.loads(response)
            if response_data.get("type") == "getAppStateResponse":
                return response_data

async def add_to_agent_state(key, value):
    async with websockets.connect('ws://localhost:your_websocket_port') as websocket:
        await websocket.send(json.dumps({
            "type": "agentStateEvent",
            "action": "addToAgentState",
            "payload": {"key": key, "value": value}
        }))
        async for response in websocket:
            response_data = json.loads(response)
            if response_data.get("type") == "addToAgentStateResponse":
                return response_data

async def get_agent_state():
    async with websockets.connect('ws://localhost:your_websocket_port') as websocket:
        await websocket.send(json.dumps({
            "type": "agentStateEvent",
            "action": "getAgentState"
        }))
        async for response in websocket:
            response_data = json.loads(response)
            if response_data.get("type") == "getAgentStateResponse":
                return response_data