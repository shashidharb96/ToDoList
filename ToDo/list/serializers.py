from rest_framework import serializers
from .models import table_ToDo


class table_ToDoSerializer(serializers.ModelSerializer):

    class Meta:
        model=table_ToDo
        fields=['title','data']
        #fields='__all__'
