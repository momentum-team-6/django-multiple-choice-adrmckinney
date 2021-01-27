from core.models import Snippet
from rest_framework import serializers

class SnippetSerializer(serializers.ModelSerializer):
    # user = serializers.SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        model = Snippet
        fields = (
            'pk',
            'user',
            'title',
            'code',
            'description',
            'category',
        )