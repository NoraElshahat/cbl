from django.contrib import admin

from attendance.models import Attendance


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('visit', )
    list_display_links = ('visit', )
    filter_horizontal = ('user', )
    

admin.site.register(Attendance, AttendanceAdmin)
