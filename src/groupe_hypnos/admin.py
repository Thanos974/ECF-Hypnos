from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Hotel
# Register your models here.

class Hoteladmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'address', 'zip_code', 'city')
    search_fields = ['name', 'city']

admin.site.register(Hotel, Hoteladmin)

admin.site.site_header = "Hypnos Administration"
admin.site.site_title = "Hypnos"
admin.site.index_title = "Boss"