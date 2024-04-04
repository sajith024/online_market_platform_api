from django.contrib import admin

from .models import Role, OnlineMarketUser, OnlineMarketLogs

# Register your models here.
admin.site.register([Role, OnlineMarketUser, OnlineMarketLogs])