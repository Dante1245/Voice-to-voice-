import asyncio, websockets
connected_clients = set()

async def media_handler(websocket, path):
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            print(f"Received: {len(message)} bytes")
            await websocket.send(message)
    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        connected_clients.remove(websocket)

start_server = websockets.serve(media_handler, "0.0.0.0", 8765)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
