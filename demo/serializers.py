from rest_framework import serializers

from demo.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'text', 'is_private', 'creator', 'updated_at']
        read_only_fields = ['creator']
