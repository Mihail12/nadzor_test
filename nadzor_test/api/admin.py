from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from api.models import Admin, BlockRequest, ProhibitedSite


admin.site.register(Admin, UserAdmin)
admin.site.register(BlockRequest, admin.ModelAdmin)
admin.site.register(ProhibitedSite, admin.ModelAdmin)
