from django.contrib import admin
from .models import Detail
from .models import Parent_Detail
# Register your models here.

class DetailAdmin(admin.ModelAdmin):

    list_display = ('name', 'roll_number', 'class_standard')
    list_filter = ('class_standard',)

class Parent_DetailAdmin(admin.ModelAdmin):

    list_display = ('parent_name', 'age', 'occupation')
    list_filter = ('age',)

admin.site.register(Detail, DetailAdmin)
admin.site.register(Parent_Detail, Parent_DetailAdmin)