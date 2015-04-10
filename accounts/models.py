from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    """
    Profile model for tracking additional user metadata.
    """
    user = models.OneToOneField(User, related_name='profile')
    public = models.BooleanField(default=False)

    def __unicode__(self):
        return self.user.get_full_name()

    def get_absolute_url(self):
        return reverse('accounts.views.user_profile', kwargs={'user_id': self.user.pk})

    def recently_with(self):
        """
        Return the five most recent chats for a user.
        """
        return self.user.spaces.all()[:5]