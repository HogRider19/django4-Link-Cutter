from django.db import models
from django.contrib.auth.models import User


class Link(models.Model):
    """Молель url адресса"""

    name = models.CharField(max_length=300, blank=True, null=True)
    raw_url = models.URLField(max_length=5000)
    truncated_url = models.URLField(max_length=5000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

