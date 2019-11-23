import asyncio
import websockets

async def hello(uri):
    async with websockets.connect(uri) as websocket:
    #     # await websocket.send('dissdoc')      
        greeting = await websocket.recv()
        print(f"< {greeting}")

asyncio.get_event_loop().run_until_complete(
    hello("ws://localhost:8765"))