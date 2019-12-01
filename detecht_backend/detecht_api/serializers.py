from rest_framework import serializers

from detecht_api.models import Document
from rest_framework.authtoken.models import Token


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('id', 'file', 'title', 'downloads', 'favorites')


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('key', 'user')
