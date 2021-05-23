from django.contrib import admin
from .models import Equipment


class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'faculty')
    list_filter = ('faculty', )
    list_editable = ('faculty', )
    list_per_page = 15
    
    
admin.site.register(Equipment, EquipmentAdmin)