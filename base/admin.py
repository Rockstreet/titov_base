from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Category
from embed_video.admin import AdminVideoMixin


from .models import Category
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):

    inlines = [ ]

admin.site.register(Category, CategoryAdmin)