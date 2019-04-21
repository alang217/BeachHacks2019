from rest_framework import serializers
from .models import TextEntry

class TextEntrySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    text = serializers.TextField(max_length=10000)
    tone = serializers.CharField(max_length=255)
    emotion = serializers.CharField(max_length=255)
    professionalism = serializers.IntegerField()
    offensiveness = serializers.CharField(max_length=255)
    reading_level = serializers.IntegerField()

    def create(self, validated_data):
        return TextEntry.objects.create(**validated_data)




