from rest_framework import serializers

from combiner.models import *

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class DrinkSerializer(serializers.ModelSerializer):
    ingredient_list = IngredientSerializer(many=True, read_only=True)

    class Meta:
        model = Drink
        fields = ('id', 'name', 'description', 'image', 'ingredient_list')
