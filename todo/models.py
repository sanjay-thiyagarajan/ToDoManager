from django.db import models

class Task(models.Model):
    categories = (
        ('Official','Official'),
        ('Personal','Personal')
    )
    Title = models.CharField(max_length=200)
    Description = models.CharField(max_length=200)
    Category = models.CharField(max_length=100, choices=categories)
    DueDate = models.DateTimeField()

    def __str__(self):
        return self.Title
    

