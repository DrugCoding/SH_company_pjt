from django.contrib import admin
from .models import Construction, C_Category
# Register your models here.
class C_CategoryAdmin(admin.ModelAdmin):
    list_display = ('name')
class ConstructionAdmin(admin.ModelAdmin):
    list_display = ('title', 'c_list')

admin.site.register(Construction, ConstructionAdmin)
admin.site.register(C_Category)