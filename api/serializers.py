from rest_framework import serializers
from blog.models import Service


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Service
        fields=[
            'user',
            'title',
            'description',
            # 'category',
            'image',
            # 'skill',
            # 'is_published',
            # 'is_active'

        ]


