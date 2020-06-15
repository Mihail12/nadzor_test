from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView, UpdateAPIView, GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import BlockRequest, ProhibitedSite
from api.serializers import BlockRequestSerializer, ProhibitedSiteSerializer


# User Block

class BlockRequestCreateView(CreateAPIView):
    serializer_class = BlockRequestSerializer
    permission_classes = [AllowAny]
    queryset = BlockRequest.objects.all()

    def perform_create(self, serializer):
        serializer.save(user_ip=self.get_client_ip(self.request))

    @staticmethod
    def get_client_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip or ''


# Admin Block

class BlockRequestApproveView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        instance = get_object_or_404(BlockRequest, pk=pk, approved=False)
        approve = request.data.get('approve')
        if not approve and not isinstance(approve, bool):
            raise ValidationError('approve field is required and should be boolean')
        instance.approved = approve
        if approve:
            ProhibitedSite.objects.get_or_create(
                domain_or_ip=instance.domain_or_ip,
                block_request=instance,
                added_by=request.user,
            )
            subject = f'Changes from prohibition server'
            message = f'Hello! Site {instance.domain_or_ip} was added to prohibited sites'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [instance.email]
            # in future it could be celery task
            sent = send_mail(subject, message, email_from, recipient_list, fail_silently=True)

            instance.email_sent = sent
        instance.save()
        return Response('ok')


class ProhibitedSiteCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProhibitedSiteSerializer
    queryset = ProhibitedSite.objects.all()

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)
