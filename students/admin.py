from django.contrib import admin
from .models import Detail,Parent_Detail, Login_Detail
# Register your models here.

class DetailAdmin(admin.ModelAdmin):

    list_display = ('name', 'roll_number', 'class_standard')
    list_filter = ('class_standard',)

class Parent_DetailAdmin(admin.ModelAdmin):

    list_display = ('parent_name', 'age', 'occupation')
    list_filter = ('age',)

class Login_DetailAdmin(admin.ModelAdmin):

    list_display = ('username', 'password')
    list_filter = ('id',)
    
admin.site.register(Login_Detail, Login_DetailAdmin)
admin.site.register(Detail, DetailAdmin)
admin.site.register(Parent_Detail, Parent_DetailAdmin)