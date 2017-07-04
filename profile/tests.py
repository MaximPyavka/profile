from django.test import TestCase
from profile.models import Profile
from django.contrib.auth.models import User


class ProfileTest(TestCase):
    def test_set(self):
        user = User.objects.create_user(username="Max10", password="qwerty123")
        profile = Profile.objects.create(user=user, bio="Was born in Ukraine.")

    def test_delete_object(self):
        user = User.objects.filter(username="Max10")
        profile = Profile.objects.filter(user=user).delete()
        user.delete()
