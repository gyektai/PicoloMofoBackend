from rest_framework import serializers
from .models import Card, Deck

class CardSerializer(serializers.ModelSerializer):
	class Meta:
		model = Card
		fields = ('id', 'uses_names', 'present')


class DeckSerializer(serializers.ModelSerializer):
	class Meta:
		model = Deck
		fields = '__all__'