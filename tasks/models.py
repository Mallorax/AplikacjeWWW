from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    tel_number = models.IntegerField()


class Task(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    priority = models.IntegerField(default=1)
    description = models.CharField(max_length=100)
