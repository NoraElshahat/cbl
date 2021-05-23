from django.db import models
from django.db.models.deletion import DO_NOTHING
from department.models import Department


class Faculty(models.Model):
    name            = models.CharField(max_length=250)
    contructured_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
    