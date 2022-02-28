from rest_framework import serializers
from base.models import Comic
from base.models import UserCollection


class ComicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comic
        fields = '__all__'
        # ['id', 'name', 'rarity', 'price', 'priceChange',
        #   'dropPrice', 'variantIssued', 'totalIssued', 'totalListed']


class CollectionSerializer(serializers.ModelSerializer):
    # userid = serializers.PrimaryKeyRelatedField(
    #     queryset=UserCollection.objects.all())

    class Meta:
        model = UserCollection
        fields = ['userid', 'comicCollection']
