from django.db import models
from django.contrib.auth.models import User

from spaces.models import Space

class Message(models.Model):
	"""
	Model of a conversation between 2 or more people.
	"""
	created = models.DateTimeField(auto_now_add=True)
	content = models.CharField(max_length=255, null=True, blank=True)
	sender = models.ForeignKey(User, related_name='sender')
	space = models.ForeignKey(Space, related_name='space')


