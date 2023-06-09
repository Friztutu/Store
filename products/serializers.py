from rest_framework import serializers

from products.models import Product


class ProductSerializers(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    gender = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'quantity', 'price', 'category', 'img', 'gender', 'slug')
