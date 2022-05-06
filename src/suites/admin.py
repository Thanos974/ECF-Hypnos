from django.contrib import admin
from suites.models import Suite
# Register your models here.

# class Suite(admin.ModelAdmin):
#     list_display = ('title', 'description', 'thumbnail', 'price')
#     search_fields = ['title', 'price']

admin.site.register(Suite) 