from rest_framework import serializers
from .models import Detail
from .models import Parent_Detail

class DetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Detail
        fields = '__all__'
        # fields = ('name', )



class Parent_DetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Parent_Detail
        fields = '__all__'
        # fields = ('name', )
