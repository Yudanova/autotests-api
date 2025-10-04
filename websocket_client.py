import asyncio

import websockets


async def client():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        message = "Hello, server!"
        print(f"Sending: {message}")
        await websocket.send(message)

        # response = await websocket.recv()
        # print(f"Server's response: {response}")

        for _ in range(5):
            response = await websocket.recv()
            print(f"Server's response: {response}")


asyncio.run(client())
