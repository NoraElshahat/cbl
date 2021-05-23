from django.contrib import admin

from .models import Visit
   

class VisitAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'faculty', 'visit_course', 'date')
    list_display_links = ('name', )
    list_filter = ('faculty', 'date')
    list_editable  = ('faculty', 'visit_course')
    search_fields = ('name',)
    list_per_page= 10 

admin.site.register(Visit, VisitAdmin)
