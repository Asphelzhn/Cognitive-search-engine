from rest_framework import serializers

from detecht_api.models import Document


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('title', 'file')
