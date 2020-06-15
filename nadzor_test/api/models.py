from django.contrib.auth.models import AbstractUser
from django.db import models


class Admin(AbstractUser):
    pass


class BlockRequest(models.Model):
    user_ip = models.GenericIPAddressField()
    email = models.EmailField()
    approved = models.BooleanField(default=False)
    email_sent = models.BooleanField(default=False)

    domain_or_ip = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f'user mail: {self.email}, address: {self.domain_or_ip}, approved: {self.approved}'

    class Meta:
        unique_together = ('email', 'domain_or_ip')


class ProhibitedSite(models.Model):
    domain_or_ip = models.CharField(max_length=100, unique=True)
    added_by = models.ForeignKey('Admin', on_delete=models.CASCADE, null=True, blank=True)
    block_request = models.ForeignKey('BlockRequest', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'address {self.domain_or_ip}'
