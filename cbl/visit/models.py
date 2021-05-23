from datetime import datetime
from time import time

from course.models import Course
from django.db import models
from django.db.models.deletion import DO_NOTHING
from faculty.models import Faculty


class Visit(models.Model):
    code =  time
    def get_visit_code():
        """
            generating random visit code
        """
        return (str(time())[:13])
    
    
    name = models.CharField(max_length=250)
    code = models.CharField(max_length=250, default=get_visit_code)
    date = models.DateTimeField(default=datetime.now)
    faculty = models.ForeignKey(Faculty, on_delete=DO_NOTHING)
    objectives = models.TextField()
    visit_course = models.ForeignKey(Course, on_delete=DO_NOTHING)

    def __str__(slef):
        """
            Getting Visit as a string
        """
        return "HU-" + str(slef.name) + '-' + str(slef.faculty)
    