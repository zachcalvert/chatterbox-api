import django_filters
from rest_framework import viewsets
from rest_framework import filters
from django.views import generic

from models import Space
from serializers import SpaceSerializer

class EntryViewSet(viewsets.ModelViewSet):
	queryset = Space.objects.all()
	serializer_class = SpaceSerializer

	def pre_save(self, obj):
		obj.owner = self.request.user
