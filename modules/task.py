import json
import asyncio
import websockets

async def add_task(task):
    async with websockets.connect('ws://localhost:your_websocket_port') as websocket:
        await websocket.send(json.dumps({
            "type": "taskEvent",
            "action": "addTask",
            "message": {"task": task}
        }))
        async for response in websocket:
            response_data = json.loads(response)
            if response_data.get("type") == "addTaskResponse":
                return response_data

async def get_tasks():
    async with websockets.connect('ws://localhost:your_websocket_port') as websocket:
        await websocket.send(json.dumps({
            "type": "taskEvent",
            "action": "getTasks"
        }))
        async for response in websocket:
            response_data = json.loads(response)
            if response_data.get("type") == "getTasksResponse":
                return response_data

async def update_task(task):
    async with websockets.connect('ws://localhost:your_websocket_port') as websocket:
        await websocket.send(json.dumps({
            "type": "taskEvent",
            "action": "updateTask",
            "message": {"task": task}
        }))
        async for response in websocket:
            response_data = json.loads(response)
            if response_data.get("type") == "updateTaskResponse":
                return response_data