from rest_framework import serializers
from blog.models import Service
from home.models import Category


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Service
        fields=[
            'id',
            # 'user',
            'title',
            'description',
            'category',
            # 'image',
            'skill',
            # 'is_published',
            # 'is_active'

        ]
        
    def validate(self, data):
        request = self.context.get('request')
        data['user'] = request.user
        return super().validate(data)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model =Category
        fields = [
            'id',
            'title',
        ]
