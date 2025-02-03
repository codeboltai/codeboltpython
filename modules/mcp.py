import json
import asyncio
import websockets

async def execute_tool(tool_name, params):
    async with websockets.connect('ws://localhost:your_websocket_port') as websocket:
        request = {
            "type": "mcpEvent",
            "action": "executeTool",
            "toolName": tool_name,
            "params": params
        }
        await websocket.send(json.dumps(request))
        async for response in websocket:
            response_data = json.loads(response)
            if response_data.get("type") == "executeToolResponse":
                return response_data

async def get_mcp_tools(tools):
    async with websockets.connect('ws://localhost:your_websocket_port') as websocket:
        request = {
            "type": "mcpEvent",
            "action": "getMcpTools",
            "tools": tools
        }
        await websocket.send(json.dumps(request))
        async for response in websocket:
            response_data = json.loads(response)
            if response_data.get("type") == "getMcpToolsResponse":
                return response_data