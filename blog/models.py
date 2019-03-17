from django.db import models

class Client(models.Model):
    lastName = models.CharField(max_length=20)
    firstName = models.CharField(max_length=20)
    phoneNumber = models.CharField(max_length=10)
    firm = models.CharField(max_length=50)

    def __str__(self):
        return "Client :\n\t" + self.lastName.upper()

class Project(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField()
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    client = models.ManyToManyField(Client)

    def __str__(self):
        return "Project :\n\t" + self.name 

class Task(models.Model):
    abstract = models.TextField()
    duration = models.IntegerField()
    startTime = models.TimeField()
    endTime = models.TimeField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return "Task :\n\t" + self.abstract