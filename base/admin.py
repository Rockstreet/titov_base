from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Category,Item,Reg
from embed_video.admin import AdminVideoMixin



# Register your models here.


class CategoryAdmin(admin.ModelAdmin):

    inlines = [ ]

class ItemAdmin(admin.ModelAdmin):

    inlines = [ ]

class RegAdmin(admin.ModelAdmin):

    inlines = [ ]

admin.site.register(Category, CategoryAdmin)

admin.site.register(Item, ItemAdmin)

admin.site.register(Reg, RegAdmin)




