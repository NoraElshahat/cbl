from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.deletion import DO_NOTHING
from visit.models import Visit

from datetime import datetime

class Attendance(models.Model):
     visit = models.ForeignKey(Visit, on_delete=DO_NOTHING)
     user = models.ManyToManyField(get_user_model())
     due_to = models.DateTimeField(default=datetime.now, null=True)
     
     def __str__(self):
          return str("Attendance for ") + str(self.visit)
     
