from django.shortcuts import render
from rest_framework import viewsets, filters
from .serializers import CardSerializer, DeckSerializer
from .models import Card, Deck
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.views.generic import View
from django.conf import settings


import urllib.request
import logging
import os


class CardView(viewsets.ModelViewSet):
	serializer_class = CardSerializer
	queryset = Card.objects.all()


class DeckView(viewsets.ModelViewSet):
	search_fields = ['title']
	filter_backends = (filters.SearchFilter,)
	serializer_class = DeckSerializer
	queryset = Deck.objects.all()




class FrontendAppView(View):
	def get(self, request):
		print(os.path.join(settings.REACT_APP_DIR, 'build', 'index.html'))
		try:
			with open(os.path.join(settings.REACT_APP_DIR, 'build', 'index.html')) as f:
				return HttpResponse(f.read())
		except FileNotFoundError:
			logging.exception('Production build of app not found')
			return HttpResponse("Bad url", status=501)