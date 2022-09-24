from django.contrib.auth.models import User
from django.db import models
from app import settings


class Link(models.Model):
    """Молель url адресса"""

    name = models.CharField(max_length=300, blank=True, null=True)
    raw_url = models.URLField(max_length=5000)
    truncated_url = models.CharField(max_length=5000)
    success_url = models.CharField(max_length=5000, blank=True, null=True)
    transition = models.PositiveBigIntegerField(default=0, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs) -> None:
        self._generate_success_url()
        return super().save(*args, **kwargs)

    def is_transition(self):
        self.transition += 1

    def _generate_success_url(self):
        self.success_url = f"{settings.DOMAIN_URL}{self.user.id}/{self.truncated_url}"

    def __str__(self):
        return self.name

