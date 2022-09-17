import asyncio

class PageControllerApp:

    PageChanged = None
    

    def  __init__(self, pageChangedCallback):
        self.PageChanged = pageChangedCallback

    def SwichPageTo(self, pageId : int):
        print('zatup')
        self.PageChanged(pageId)