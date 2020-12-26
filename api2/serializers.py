from rest_framework import serializers
from blog.models import Skill


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model=Skill
        fields=[
            'id',
            'title',
            'category',
        ]


