from django.db import models

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    SEX_CHOICES = [
        ("Male", 'Male'),
        ("Female", 'Female'),
        ("Other", 'Other'),
    ]

    birth_date = models.DateField(null=True, blank=True)
    sex = models.CharField(max_length=6, choices=SEX_CHOICES, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)