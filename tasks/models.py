from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    tel_number = models.IntegerField()

    def __str__(self):
        return self.first_name + " " + self.last_name


class Task(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    priority = models.IntegerField(default=1)
    description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title + " | " + str(self.person)
