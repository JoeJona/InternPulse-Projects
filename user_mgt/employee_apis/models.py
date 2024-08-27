from django.db import models


# Create your models here.

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, default='')
    position = models.CharField(max_length=255, default='')
    department = models.CharField(max_length=255, default='')
    phone = models.CharField(max_length=255, default='')
    email = models.CharField(max_length=255, default='')
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.id


class EmployeeReview(models.Model):
    id = models.AutoField(primary_key=True)
    reviewer_id = models.IntegerField(max_length=255, default=0)
    employee_id = models.IntegerField(max_length=255, default=0)
    review = models.TextField(max_length=255, default='')

    def __str__(self):
        return self.id
