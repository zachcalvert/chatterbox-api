from django.db import models
from django.contrib.auth.models import User

class Space(models.Model):
	"""
	Model of a conversation between 2 or more people.
	"""
	people = models.ManyToManyField(User, related_name='people')
	created = models.DateTimeField(auto_now_add=True)

	def messages(self):
		"""
		Return the chat history
		"""
		return self.messages.order_by('-created')
