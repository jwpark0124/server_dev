from rest_framework import serializers
from .models import  Post


class PostSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Post
        fields = [
            
            "is_public",
            "title",
            "host",
            "award",
            "explanation",
            "period1",
            "period2",
            'Participant',
            'tag_set',
            'state',
        ]
    