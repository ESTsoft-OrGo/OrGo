from rest_framework import serializers
from .models import Study, Tags

class StudySerializer(serializers.ModelSerializer):
    class Meta:
        model = Study
        fields = '__all__'
        # read_only_fields = ['is_active']

    # def create(self, validated_data):
    #     validated_data['is_active'] = True 
    #     study = super().create(validated_data)
    #     return study


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'