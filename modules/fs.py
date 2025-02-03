import json
import asyncio
import websockets

async def create_file(file_name, source, file_path):
    async with websockets.connect('ws://localhost:your_websocket_port') as websocket:
        message = {
            "type": "fsEvent",
            "action": "createFile",
            "message": {
                "fileName": file_name,
                "source": source,
                "filePath": file_path
            }
        }

        await websocket.send(json.dumps(message))
        async for response in websocket:
            response_data = json.loads(response)
            if response_data.get("type") == "createFileResponse":
                return response_data

async def create_folder(folder_name, folder_path):
    async with websockets.connect('ws://localhost:your_websocket_port') as websocket:
        message = {
            "type": "fsEvent",
            "action": "createFolder",
            "message": {
                "folderName": folder_name,
                "folderPath": folder_path
            }
        }

        await websocket.send(json.dumps(message))
        async for response in websocket:
            response_data = json.loads(response)
            if response_data.get("type") == "createFolderResponse":
                return response_data