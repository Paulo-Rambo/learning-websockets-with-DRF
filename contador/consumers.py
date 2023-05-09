from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer


class CountConsumer(AsyncWebsocketConsumer):
    count = 0
    groups = ['count']
    async def connect(self):
        self.room_group_name = 'count'
        self.channel_layer = get_channel_layer()
        self.client_ip = self.scope["client"][0]
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    async def count_message(self, event):
        print(self.count)
        self.room_group_name = 'count'
        if event['text'] == "add":
            self.count += 1
        await self.send(text_data=str(self.count))