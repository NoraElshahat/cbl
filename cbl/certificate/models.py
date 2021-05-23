from django.db import models
from django.db.models.deletion import DO_NOTHING
from visit.models import Visit


class Certificate(models.Model):
    title = models.CharField(max_length = 250)
    img = models.ImageField()
    visit = models.ForeignKey(Visit, on_delete = DO_NOTHING)
    