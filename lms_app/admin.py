from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Category)
admin.site.register(Book)

admin.site.site_header = 'NOUVIL'
admin.site.site_title = 'NOUVIL'