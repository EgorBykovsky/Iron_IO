from rest_framework import serializers
from session.models import Session
from users.models import User
from chat.models import  Chat

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Session
        fields = ['uuid', 
                  'creator',
                  'word'] 
        
    def update(self, instance, validated_data):
        # Обновляем поле word с помощью данных из validated_data
        instance.word = validated_data.get('word', instance.word)
        # Сохраняем изменения
        instance.save()
        return instance
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ['uuid', 
                  'session'] 
        
class ChatSerializers(serializers.ModelSerializer):
    
    user = UserSerializer()
    class Meta:
        model=Chat
        fields = ["user", "text"]
