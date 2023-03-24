import asyncio
import NextionEdition

nextionApp = NextionEdition.NextionApp(None, None)

def OpenGrafPage():
    pass











if __name__ == '__main__':
    
    loop = asyncio.get_event_loop()
    task = loop.create_task(_nextionApp.Run())
    asyncio.ensure_future(task)
    loop.run_forever()