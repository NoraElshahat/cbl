from django.db import models

class Report(models.Model):
    question = models.CharField(max_length=255)
    
    def __str__(self):
        """
            getting a string for the class
        """
        return self.question