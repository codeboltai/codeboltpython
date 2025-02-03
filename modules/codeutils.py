import json
import os
import asyncio
from modules.websocket import cbws_instance

class CBCodeUtils:
    async def get_js_tree(self, file_path=None):
        """
        Retrieves a JavaScript tree structure for a given file path.
        :param file_path: The path of the file to retrieve the JS tree for.
        :return: A promise that resolves with the JS tree response.
        """
        websocket = cbws_instance.get_websocket()
        await websocket.send(json.dumps({
            "type": "settingEvent",
            "action": "getProjectPath"
        }))
        async for message in websocket:
            response = json.loads(message)
            if response.get("type") == "getProjectPathResponse":
                try:
                    path_input = file_path or response.get("projectPath")
                    trees = self._process_directory(path_input)
                    return {"event": "GetJsTreeResponse", "payload": trees}
                except Exception as error:
                    print('An error occurred:', error)
                    return {"event": "GetJsTreeResponse", "payload": None}

    def _process_directory(self, directory):
        # This is a placeholder for the actual directory processing logic
        print(f"Processing directory: {directory}")
        return []

    async def get_all_files_as_markdown(self):
        """
        Retrieves all files as Markdown.
        :return: A promise that resolves with the Markdown content of all files.
        """
        websocket = cbws_instance.get_websocket()
        await websocket.send(json.dumps({
            "type": "codeEvent",
            "action": "getAllFilesMarkdown"
        }))
        async for message in websocket:
            response = json.loads(message)
            if response.get("type") == "getAllFilesMarkdownResponse":
                return response

    async def perform_match(self, matcher_definition, problem_patterns, problems):
        """
        Performs a matching operation based on the provided matcher definition and problem patterns.
        :param matcher_definition: The definition of the matcher.
        :param problem_patterns: The patterns to match against.
        :param problems: The list of problems.
        :return: A promise that resolves with the matching problem response.
        """
        websocket = cbws_instance.get_websocket()
        await websocket.send(json.dumps({
            "type": "codeEvent",
            "action": "performMatch",
            "payload": {
                "matcherDefinition": matcher_definition,
                "problemPatterns": problem_patterns,
            }
        }))
        async for message in websocket:
            response = json.loads(message)
            if response.get("type") == "getgetJsTreeResponse":
                return response

    async def get_matcher_list(self):
        """
        Retrieves the list of matchers.
        :return: A promise that resolves with the list of matchers response.
        """
        websocket = cbws_instance.get_websocket()
        await websocket.send(json.dumps({
            "type": "codeEvent",
            "action": "getMatcherList",
        }))
        async for message in websocket:
            response = json.loads(message)
            if response.get("type") == "getMatcherListTreeResponse":
                return response

    async def match_detail(self, matcher):
        """
        Retrieves details of a match.
        :param matcher: The matcher to retrieve details for.
        :return: A promise that resolves with the match detail response.
        """
        websocket = cbws_instance.get_websocket()
        await websocket.send(json.dumps({
            "type": "codeEvent",
            "action": "getMatchDetail",
            "payload": {
                "match": matcher
            }
        }))
        async for message in websocket:
            response = json.loads(message)
            if response.get("type") == "matchDetailTreeResponse":
                return response

cbcodeutils = CBCodeUtils()
