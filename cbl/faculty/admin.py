from django.contrib import admin
from .models import Faculty

class FacultyModel(admin.ModelAdmin):
    def prefix(self, faculty):
        return str(faculty.name[:3])

    list_display = ('name', 'prefix','contructured_at')
    list_per_page = 15
    ordering = ('id', )
    list_filter = ('contructured_at', )
    search_fields = ('name', )         
         
admin.site.register(Faculty, FacultyModel)

