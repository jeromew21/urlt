from django.db import models

# Create your models here.

class BasicUrlModel(models.Model):
    customUrl = models.CharField(max_length=10, unique=True)
    url = models.URLField()

class CoinRedirectModel(models.Model):
    customUrl = models.CharField(max_length=10, unique=True)
    url1 = models.URLField()
    url2 = models.URLField()

class RandomRedirectModel(models.Model):
    customUrl = models.CharField(max_length=10, unique=True)
    url1 = models.URLField(null=True, blank=True)
    url2 = models.URLField(null=True, blank=True)
    url3 = models.URLField(null=True, blank=True)
    url4 = models.URLField(null=True, blank=True)
    url5 = models.URLField(null=True, blank=True)
    url6 = models.URLField(null=True, blank=True)
    url7 = models.URLField(null=True, blank=True)