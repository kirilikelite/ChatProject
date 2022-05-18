from Logic import Server
from UI import ServerWindow
import asyncio


async def main():
    server = Server.Server()
    server_window = ServerWindow.ServerWindow(server)
    main_task = asyncio.create_task(mainloop(server_window.window))
    await main_task

async def mainloop(window):
    while True:
        await asyncio.sleep(0.1)
        window.update_idletasks()
        window.update()


asyncio.run(main())
