from django.core.exceptions import ValidationError
from rest_framework import serializers

from api.models import BlockRequest, ProhibitedSite

from django.core.validators import validate_ipv46_address, RegexValidator

validate_hostname = RegexValidator(regex=r'[a-zA-Z0-9-_]*\.[a-zA-Z]{2,6}')


# User Block

class BlockRequestSerializer(serializers.ModelSerializer):
    def validate_domain_or_ip(self, data):
        try:
            validate_hostname(data)
            return data
        except ValidationError:
            validate_ipv46_address(data)
        return data

    class Meta:
        model = BlockRequest
        fields = ['email', 'domain_or_ip', 'description']


# Admin Block

class ProhibitedSiteSerializer(serializers.ModelSerializer):
    def validate_domain_or_ip(self, data):
        try:
            validate_hostname(data)
            return data
        except ValidationError:
            validate_ipv46_address(data)
        return data

    class Meta:
        model = ProhibitedSite
        fields = ['domain_or_ip']
