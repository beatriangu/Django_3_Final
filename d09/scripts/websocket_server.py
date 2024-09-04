import asyncio
import websockets
import redis

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

async def handler(websocket, path):
    channel = path.strip('/')
    pubsub = redis_client.pubsub()
    pubsub.subscribe(channel)

    async def publish_messages():
        while True:
            message = pubsub.get_message()
            if message:
                await websocket.send(message['data'].decode('utf-8'))
            await asyncio.sleep(0.1)

    async def receive_messages():
        async for message in websocket:
            redis_client.publish(channel, message)

    await asyncio.gather(publish_messages(), receive_messages())

# Cambiado el puerto a 8766
start_server = websockets.serve(handler, "localhost", 8766)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
