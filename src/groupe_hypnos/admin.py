from django.contrib import admin
from .models import Hotel
# Register your models here.

class Hoteladmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'address', 'zip_code', 'city')
    search_fields = ['name']

admin.site.register(Hotel, Hoteladmin)