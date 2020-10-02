from rest_framework import serializers
from electronics.models import Products


class  ProductSerializer(serializers.ModelSerializer):
    Name = serializers.CharField(required=False)
    Description = serializers.CharField(required=False)
    RAM = serializers.IntegerField(required=False)
    Type = serializers.CharField(required=False)
    Processor = serializers.CharField(required=False)


    class Meta:
        model = Products
        fields = '__all__'