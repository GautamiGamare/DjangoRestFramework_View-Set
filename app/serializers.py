from rest_framework import serializers
from app.models import ProductModel

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = ProductModel