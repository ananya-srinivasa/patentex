# models.py
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=100)



class Organization(models.Model):
    orgname = models.CharField(max_length=255)
    orgtype = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    phone_number_2 = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField()
    reg_no = models.CharField(max_length=50)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.orgname


# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class Agent(AbstractUser):
    gender_choices = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    mobile_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    patent_agent_key = models.CharField(max_length=255)
    key_valid_till = models.DateField()
    gender = models.CharField(max_length=6, choices=gender_choices)

    # Add unique related_name for the fields causing the clash
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='agent_groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='agent_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username

