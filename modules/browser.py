import json
from modules.websocket import cbws_instance

class CBBrowser:
    async def new_page(self):
        """
        Opens a new page in the browser.
        """
        websocket = cbws_instance.get_websocket()
        await websocket.send(json.dumps({
            "type": "browserEvent",
            "action": "newPage"
        }))
        async for message in websocket:
            response = json.loads(message)
            if response.get("event") == "newPageResponse":
                return response

    async def get_url(self):
        """
        Retrieves the current URL of the browser's active page.
        :return: A promise that resolves with the URL.
        """
        websocket = cbws_instance.get_websocket()
        await websocket.send(json.dumps({
            "type": "browserEvent",
            "action": "getUrl"
        }))
        async for message in websocket:
            response = json.loads(message)
            if response.get("event") == "getUrlResponse":
                return response

    async def go_to_page(self, url: str):
        """
        Navigates to a specified URL.
        :param url: The URL to navigate to.
        :return: A promise that resolves when navigation is complete.
        """
        websocket = cbws_instance.get_websocket()
        await websocket.send(json.dumps({
            "type": "browserEvent",
            "action": "goToPage",
            "url": url
        }))
        async for message in websocket:
            response = json.loads(message)
            if response.get("event") == "goToPageResponse":
                return response

    async def screenshot(self):
        """
        Takes a screenshot of the current page.
        """
        websocket = cbws_instance.get_websocket()
        await websocket.send(json.dumps({
            "type": "browserEvent",
            "action": "screenshot"
        }))
        async for message in websocket:
            response = json.loads(message)
            if response.get("event") == "screenshotResponse":
                return response.get("payload")

    async def get_html(self):
        """
        Retrieves the HTML content of the current page.
        :return: A promise that resolves with the HTML content.
        """
        websocket = cbws_instance.get_websocket()
        await websocket.send(json.dumps({
            "type": "browserEvent",
            "action": "getHTML"
        }))
        async for message in websocket:
            response = json.loads(message)
            if response.get("event") == "htmlReceived":
                return response.get("htmlResponse")

    async def get_markdown(self):
        """
        Retrieves the Markdown content of the current page.
        :return: A promise that resolves with the Markdown content.
        """
        websocket = cbws_instance.get_websocket()
        await websocket.send(json.dumps({
            "type": "browserEvent",
            "action": "getMarkdown"
        }))
        async for message in websocket:
            response = json.loads(message)
            if response.get("event") == "getMarkdownResponse":
                return response

    def get_pdf(self):
        """
        Retrieves the PDF content of the current page.
        """
        websocket = cbws_instance.get_websocket()
        websocket.send(json.dumps({
            "type": "browserEvent",
            "action": "getPDF"
        }))

    def pdf_to_text(self):
        """
        Converts the PDF content of the current page to text.
        """
        websocket = cbws_instance.get_websocket()
        websocket.send(json.dumps({
            "type": "browserEvent",
            "action": "pdfToText"
        }))

    async def get_content(self):
        """
        Retrieves the content of the current page.
        :return: A promise that resolves with the content.
        """
        websocket = cbws_instance.get_websocket()
        await websocket.send(json.dumps({
            "type": "browserEvent",
            "action": "getContent"
        }))
        async for message in websocket:
            response = json.loads(message)
            if response.get("event") == "getContentResponse":
                return response

    async def get_snapshot(self):
        """
        Retrieves the snapshot of the current page.
        :return: A promise that resolves with the content.
        """
        websocket = cbws_instance.get_websocket()
        await websocket.send(json.dumps({
            "type": "browserEvent",
            "action": "getSnapShot"
        }))
        async for message in websocket:
            response = json.loads(message)
            if response.get("event") == "getSnapShotResponse":
                return response

    async def get_browser_info(self):
        """
        Retrieves browser info like height, width, scrollX, scrollY of the current page.
        :return: A promise that resolves with the content.
        """
        websocket = cbws_instance.get_websocket()
        await websocket.send(json.dumps({
            "type": "browserEvent",
            "action": "getBrowserInfo"
        }))
        async for message in websocket:
            response = json.loads(message)
            if response.get("event") == "getBrowserInfoResponse":
                return response

    async def extract_text(self):
        """
        Extracts text from the current page.
        :return: A promise that resolves with the extracted text.
        """
        websocket = cbws_instance.get_websocket()
        await websocket.send(json.dumps({
            "type": "browserEvent",
            "action": "extractText"
        }))
        async for message in websocket:
            response = json.loads(message)
            if response.get("event") == "extractTextResponse":
                return response

    def close(self):
        """
        Closes the current page.
        """
        websocket = cbws_instance.get_websocket()
        websocket.send(json.dumps({
            "type": "browserEvent",
            "action": "close"
        }))

    async def scroll(self, direction: str, pixels: str):
        """
        Scrolls the current page in a specified direction by a specified number of pixels.
        :param direction: The direction to scroll.
        :param pixels: The number of pixels to scroll.
        :return: A promise that resolves when the scroll action is complete.
        """
        websocket = cbws_instance.get_websocket()
        await websocket.send(json.dumps({
            "type": "browserEvent",
            "action": "scroll",
            "direction": direction,
            "pixels": pixels
        }))
        async for message in websocket:
            response = json.loads(message)
            if response.get("event") == "scrollResponse":
                return response

    async def type(self, elementid: str, text: str):
        """
        Types text into a specified element on the page.
        :param elementid: The ID of the element to type into.
        :param text: The text to type.
        :return: A promise that resolves when the typing action is complete.
        """
        websocket = cbws_instance.get_websocket()
        await websocket.send(json.dumps({
            "type": "browserEvent",
            "action": "type",
            "text": text,
            "elementid": elementid
        }))
        async for message in websocket:
            response = json.loads(message)
            if response.get("event") == "typeResponse":
                return response

    async def click(self, elementid: str):
        """
        Clicks on a specified element on the page.
        :param elementid: The ID of the element to click.
        :return: A promise that resolves when the click action is complete.
        """
        websocket = cbws_instance.get_websocket()
        await websocket.send(json.dumps({
            "type": "browserEvent",
            "action": "click",
            "elementid": elementid
        }))
        async for message in websocket:
            response = json.loads(message)
            if response.get("event") == "clickResponse":
                return response

    async def enter(self):
        """
        Simulates the Enter key press on the current page.
        :return: A promise that resolves when the Enter action is complete.
        """
        websocket = cbws_instance.get_websocket()
        await websocket.send(json.dumps({
            "type": "browserEvent",
            "action": "enter"
        }))
        async for message in websocket:
            response = json.loads(message)
            if response.get("event") == "EnterResponse":
                return response

    async def search(self, elementid: str, query: str):
        """
        Performs a search on the current page using a specified query.
        :param elementid: The ID of the element to perform the search in.
        :param query: The search query.
        :return: A promise that resolves with the search results.
        """
        websocket = cbws_instance.get_websocket()
        await websocket.send(json.dumps({
            "type": "browserEvent",
            "action": "search",
            "elementid": elementid,
            "query": query
        }))
        async for message in websocket:
            response = json.loads(message)
            if response.get("event") == "searchResponse":
                return response

cbbrowser = CBBrowser()
