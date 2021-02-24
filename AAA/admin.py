from django.contrib import admin
from .models import Items

# Register your models here.



class ItemsAdmin(admin.ModelAdmin):

    list_display = ('item', 'desc','price')
    list_filter = ('item','id','price')


admin.site.register(Items, ItemsAdmin)

