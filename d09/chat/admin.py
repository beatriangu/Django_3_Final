# # chat/admin.py

from django.contrib import admin
from .models import ChatRoom, Message, ChatRoomUser

@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'room', 'user', 'body', 'timestamp')
    search_fields = ('room__name', 'user__username', 'body')
    list_filter = ('room', 'user', 'timestamp')

@admin.register(ChatRoomUser)
class ChatRoomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'room', 'user', 'date')
    search_fields = ('room__name', 'user__username')
    list_filter = ('room', 'user', 'date')
