from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=500, blank=True)
    last_name = models.CharField(max_length=500, blank=True)
    email = models.EmailField(max_length=500, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=Profile)
def model_post_save(sender, **kwargs):
    print("Object created/updated")


@receiver(post_delete, sender=Profile)
def model_post_delete(sender, **kwargs):
    print("Object deleted")
