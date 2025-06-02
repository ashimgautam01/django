from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Student
        fields='__all__'


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model=Department
        fields='__all__'