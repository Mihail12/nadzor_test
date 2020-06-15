from django.conf.urls import url

from api import views

app_name = 'api'

urlpatterns = [
    url(r'^block_requests/$', views.BlockRequestCreateView.as_view(), name='block_requests_add'),
    url(r'^block_requests/(?P<pk>[0-9]+)/$', views.BlockRequestApproveView.as_view(), name='block_requests_update'),
    url(r'^block_site/$', views.ProhibitedSiteCreateView.as_view(), name='block_site'),
]