from rest_framework import serializers

from .models import Info, Data

class InfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Info
        fields = ['user', 'name']

class DataSerializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.CharField(source='user_link', read_only=True)
    class Meta:
        model = Data
        fields = ['user_id', 'user_link', 'data_text']
