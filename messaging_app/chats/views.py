from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Conversation
from .models import Message
from .serializers import ConversationSerializer
from .serializers import MessageSerializer
from rest_framework.decorators import action
from .permissions import IsParticipant, IsSender
from .filters import MessageFilter
from django_filters.rest_framework import DjangoFilterBackend


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    permission_classes = [IsParticipant]
    serializer_class = ConversationSerializer
    

    def get_queryset(self):
        return Conversation.objects.filter(participants=self.request.user)


    def create(self, request, *args, **kwargs):
        participants = request.data.get('participants', [])
        conversation = Conversation.objects.create()
        conversation.participants.set(participants)
        conversation.save()
        serializer = self.get_serializer(conversation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    permission_classes = [IsSender]
    serializer_class = MessageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MessageFilter

    def get_queryset(self):
        return Message.objects.filter(conversation__participants=self.request.user)


    def create(self, request, *args, **kwargs):
        conversation_id = request.data.get('conversation')
        content = request.data.get('content')
        sender = request.user

        message = Message.objects.create(
            conversation_id=conversation_id,
            sender=sender,
            content=content
        )
        serializer = self.get_serializer(message)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
