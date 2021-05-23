from visit.models import Visit
from django.db import models
from django.db.models.deletion import DO_NOTHING
from faculty.models import Faculty


class Equipment(models.Model):
    name = models.CharField(max_length=250)
    faculty = models.ForeignKey(Faculty, on_delete=DO_NOTHING)
    visit = models.ManyToManyField(Visit)

    def __str__(self):
        return self.name
    