import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
class LiveConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'test'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        # self.room_group_name = 'test'

        # async_to_sync(self.channel_layer.group_add)(
        #     self.room_group_name,
        #     self.channel_name
        # )

        await self.accept()
    
    async def disconnect(self, close_code):
        self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        print("disconnecting!!!")

    async def receive(self, text_data):
        recieve_dict = json.loads(text_data)
        message = recieve_dict['message']
        action = recieve_dict['action']

        if action == 'new-offer' or action == 'new-answer':
            receive_channel_name = recieve_dict['message']['reciever_channel_name']
            recieve_dict['message']['reciever_channel_name'] = self.channel_name
            
            await self.channel_layer.send(
                receive_channel_name,
                {
                    'type': 'send.sdp',
                    'recieve_dict': recieve_dict
                }
            )
            return 
        recieve_dict['message']['reciever_channel_name'] = self.channel_name
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'send.sdp',
                'recieve_dict': recieve_dict
            }
        )

    async def send_sdp(self, event):
        recieve_dict = event['recieve_dict']
        print(recieve_dict)
        await self.send(text_data=json.dumps(recieve_dict))

