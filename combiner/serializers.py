from rest_framework import serializers

from combiner.models import *

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class DrinkIngredientSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer(read_only=True)
    class Meta:
        model = DrinkIngredient
        fields = ('id', 'size', 'ingredient')

class DrinkSerializer(serializers.ModelSerializer):
    ingredient_list = DrinkIngredientSerializer(many=True, read_only=True)

    class Meta:
        model = Drink
        fields = ('id', 'name', 'description', 'image', 'ingredient_list')
