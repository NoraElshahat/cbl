from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import DO_NOTHING

class Meeting(models.Model):
    title = models.CharField(max_length=250)
    time = models.DateTimeField()
    
    def __str__(self):
        return self.title
    
class MeetingAttendace(models.Model):
    user = models.ManyToManyField(get_user_model())
    meeting = models.ForeignKey(Meeting, on_delete=DO_NOTHING)
    
    def __str__(self):
        """
            returning a str
        """
        return str(self.meeting)