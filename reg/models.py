from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six


class UserProfile(models.Model):
    user = models.OneToOneField(User,related_name='profile', primary_key=True)
    email_confirmed = models.BooleanField(default=False)
    college = models.CharField(max_length=10,blank=False)
    branch = models.CharField(max_length=10,blank=False)
    year = models.CharField(max_length=10,blank=False)

    def __unicode__(self):
        return unicode(self.user)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        profile = UserProfile(user=user)
        profile.save()

