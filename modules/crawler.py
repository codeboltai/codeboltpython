import json
from modules.websocket import cbws_instance

class CBCrawler:
    def start(self):
        """
        Starts the crawler.
        """
        websocket = cbws_instance.get_websocket()
        websocket.send(json.dumps({
            "type": "crawlerEvent",
            "action": "start"
        }))

    def screenshot(self):
        """
        Takes a screenshot using the crawler.
        """
        websocket = cbws_instance.get_websocket()
        websocket.send(json.dumps({
            "type": "crawlerEvent",
            "action": "screenshot"
        }))

    def go_to_page(self, url):
        """
        Directs the crawler to navigate to a specified URL.
        :param url: The URL for the crawler to navigate to.
        """
        websocket = cbws_instance.get_websocket()
        websocket.send(json.dumps({
            "type": "crawlerEvent",
            "action": "goToPage",
            "url": url
        }))

    def scroll(self, direction):
        """
        Scrolls the crawler in a specified direction.
        :param direction: The direction to scroll ('up', 'down', 'left', 'right').
        """
        websocket = cbws_instance.get_websocket()
        websocket.send(json.dumps({
            "type": "crawlerEvent",
            "action": "scroll",
            "direction": direction
        }))

    async def click(self, element_id):
        """
        Simulates a click event on an element with the specified ID.
        :param element_id: The ID of the element to be clicked.
        :return: A promise that resolves when the click action is complete.
        """
        websocket = cbws_instance.get_websocket()
        await websocket.send(json.dumps({
            "type": "crawlerEvent",
            "action": "click",
            "id": element_id
        }))
        async for message in websocket:
            response = json.loads(message)
            if response.get("event") == "clickFinished":
                return response

    async def type(self, element_id, text):
        """
        Types the provided text into an element with the specified ID.
        :param element_id: The ID of the element where text will be typed.
        :param text: The text to type into the element.
        :return: A promise that resolves when the type action is complete.
        """
        websocket = cbws_instance.get_websocket()
        await websocket.send(json.dumps({
            "type": "crawlerEvent",
            "action": "type",
            "id": element_id,
            "text": text
        }))
        async for message in websocket:
            response = json.loads(message)
            if response.get("event") == "typeFinished":
                return response

    def enter(self):
        """
        Simulates the Enter key press using the crawler.
        """
        websocket = cbws_instance.get_websocket()
        websocket.send(json.dumps({
            "type": "crawlerEvent",
            "action": "enter"
        }))

    async def crawl(self, query):
        """
        Initiates a crawl process.
        :param query: The query to use for the crawl.
        :return: A promise that resolves with the crawl response.
        """
        websocket = cbws_instance.get_websocket()
        await websocket.send(json.dumps({
            "type": "crawlerEvent",
            "action": "crawl",
            "message": {
                "query": query
            }
        }))
        async for message in websocket:
            response = json.loads(message)
            if response.get("type") == "crawlResponse":
                return response

cbcrawler = CBCrawler()
