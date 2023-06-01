from rest_framework import fields, serializers

from hr.models import doc

class DocSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = doc
        fields = '__all__'
        