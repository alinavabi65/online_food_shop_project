from django.db import models


class Region(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
