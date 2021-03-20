from rest_framework import serializers

class serializer(serializers.Serializer):
    data = serializers.CharField(max_length = 100)