from django.db import models

# Create your models here.
JOB_TYPE = (
    ("Full Time","Full Time"),
    ("Part Time","Part Time"),
)
class Job(models.Model):
    title = models.CharField (max_length=100)
    # location 
    job_type = models.CharField (max_length= 20, choices=JOB_TYPE)
    description = models.TextField (max_length=10000)
    published_at = models.DateTimeField (auto_now = True)
    vacancy = models.IntegerField (default=1)
    salary = models.IntegerField (default=0)
    category = models.ForeignKey ("Category", on_delete=models.CASCADE)
    experiance = models.IntegerField (default=1)

    def __str__(self):
        return self.title

class Category (models.Model):
    name = models.CharField (max_length=25)

    def __str__(self):
        return self.name