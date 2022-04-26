from django.db import models


# Create your models here.

class Cohort(models.Model):
    number = models.IntegerField(default=0, unique=True)
    name = models.CharField(max_length=100, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name


GENDER = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('others', 'Others')
)


class Native(models.Model):
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10, choices=GENDER, default='others')
    number = models.CharField(max_length=3, unique=True)
    date_of_birth = models.DateField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)

    def _str_(self):
        return self.first_name + " " + self.last_name
