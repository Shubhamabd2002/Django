from rest_framework import serializers
from . import models

class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Todo
        fields = '__all__'
        #this include all the fields in that particular model of Todo and if any specific ['id'] this will only include id from Todo model
        # exclude = ['id']           Include everything except 'id'