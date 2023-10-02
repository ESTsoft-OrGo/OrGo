import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Room , Message
from django.contrib.auth import get_user_model
from django.db.models.functions import TruncDay

User = get_user_model()


class ChatConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        
        user = self.scope["user"]

        if not user.is_authenticated:
            self.close()
            
    	# 파라미터 값으로 채팅 룸을 구별
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # 룸 그룹에 참가
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # 룸 그룹 나가기
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # 웹소켓으로부터 메세지 받음
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        method = text_data_json['method']
        message = text_data_json['message']
        
        # 룸 그룹으로 메세지 보냄
        if method == 'join':
            await self.find_room(self.room_name)
            
            room = Room.objects.get(title=self.room_name)
            join_messages = Message.objects.filter(room=room).annotate(day=TruncDay('created_at')).values('day', 'id')
            join_message = await self.messages_to_json(join_messages)
            
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'status': 'join',
                    'message': join_message
                }
            )
        elif method == 'message':
            writer = text_data_json['writer']
            user = User.objects.get(pk=writer)
            room = Room.objects.get(title=self.room_name)
            message = Message.objects.create(writer=user,content=message,room=room)
            new_message = await self.message_to_json(message)
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': new_message,
                    'status': 'message'
                }
            )

    # 룸 그룹 방을 찾거나 만듬
    async def find_room(self, data):
        room = Room.objects.get_or_create(title=data)
    
    # 룸 그룹으로부터 메세지 받음
    async def chat_message(self, event):
        message = event['message']
        status = event['status']
        # 웹소켓으로 메세지 보냄
        await self.send(text_data=json.dumps({
            'message': message,
            'status': status
        }))
    
    async def messages_to_json(self, messages):
        # 날짜별로 메시지들을 그룹화
        message_grouped_by_day = {}
        for entry in messages:
            day = entry['day'].strftime('%Y.%m.%d')
            message = Message.objects.get(id=entry['id'])  # 해당 메시지 가져오기 (필요한 필드에 맞게 변경)
            wrtier_id = message.writer.id
            dict_ = message.__dict__
            data = {
                "content": dict_['content'],
                "created_at": str(dict_['created_at']),
                "writer": wrtier_id
            }
            if day not in message_grouped_by_day:
                message_grouped_by_day[day] = [data]
            else:
                message_grouped_by_day[day].append(data)
        
        return message_grouped_by_day
    
    async def message_to_json(self, message):
        result = []
        wrtier_id = message.writer.id
        dict_ = message.__dict__
        data = {
            "content": dict_['content'],
            "created_at": str(dict_['created_at']),
            "writer": wrtier_id
        }
        result.append(data)
        return result