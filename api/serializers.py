from rest_framework import serializers
from base.models import Comic


class ComicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comic
        fields = '__all__'
        # ['id', 'name', 'rarity', 'price', 'priceChange',
        #   'dropPrice', 'variantIssued', 'totalIssued', 'totalListed']
