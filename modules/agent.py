import json
from modules.websocket import cbws_instance

class CodeboltAgent:
    def get_agent(self, task: str):
        """
        Retrieves an agent based on the specified task.
        :param task: The task for which an agent is needed.
        :return: A promise that resolves with the agent details.
        """
        async def get_agent_async():
            websocket = cbws_instance.get_websocket()
            await websocket.send(json.dumps({
                "type": "agentEvent",
                "action": "getAgentByTask",
                "task": task
            }))
            async for message in websocket:
                response = json.loads(message)
                if response.get("type") == "getAgentByTaskResponse":
                    return response

        return get_agent_async()

    def start_agent(self, agent_id: str, task: str):
        """
        Starts an agent for the specified task.
        :param agent_id: The ID of the agent to start.
        :param task: The task for which the agent should be started.
        :return: A promise that resolves when the agent has been successfully started.
        """
        async def start_agent_async():
            websocket = cbws_instance.get_websocket()
            await websocket.send(json.dumps({
                "type": "agentEvent",
                "action": "startAgent",
                "agentId": agent_id,
                "task": task
            }))
            async for message in websocket:
                response = json.loads(message)
                if response.get("type") == "taskCompletionResponse":
                    return response

        return start_agent_async()

codebolt_agent = CodeboltAgent()
