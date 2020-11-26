from django.shortcuts import render
from rest_framework import viewsets, filters
from .serializers import CardSerializer, DeckSerializer
from .models import Card, Deck

class CardView(viewsets.ModelViewSet):
	serializer_class = CardSerializer
	queryset = Card.objects.all()


class DeckView(viewsets.ModelViewSet):
	search_fields = ['title']
	filter_backends = (filters.SearchFilter,)
	serializer_class = DeckSerializer
	queryset = Deck.objects.all()

