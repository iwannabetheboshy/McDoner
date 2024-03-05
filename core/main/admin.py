from django.contrib import admin
from .models import FeedBack


class FeedBackAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'question']


admin.site.register(FeedBack, FeedBackAdmin)