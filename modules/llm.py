import json
import asyncio
import websockets

async def inference(message, llm_role):
    async with websockets.connect('ws://localhost:your_websocket_port') as websocket:
        request = {
            "type": "inference",
            "message": {
                "prompt": message,
                "llmrole": llm_role
            }
        }
        await websocket.send(json.dumps(request))
        async for response in websocket:
            response_data = json.loads(response)
            if response_data.get("type") == "llmResponse":
                return response_data