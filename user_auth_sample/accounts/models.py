from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    image_url = models.URLField('image url', blank = True)
