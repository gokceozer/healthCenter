from django.db import models

class Patient(models.Model):

    name = models.CharField(max_length=100)
    idn = models.CharField(max_length=100,unique=True)
    date_of_birth = models.DateField()
    confirm_day = models.DateField()
    case_no = models.IntegerField()


    def __str__(self):
        return self.name

class Past_Location(models.Model):

    location = models.CharField(max_length=100)
    address = models.CharField(max_length=100,null=True, blank=True)
    district = models.CharField(max_length=100)
    x_cord = models.IntegerField(null=True, blank=True)
    y_cord = models.IntegerField(null=True, blank=True)
    date_from = models.DateField(null=True, blank=True)
    date_to = models.DateField(null=True, blank=True)
    detail = models.CharField(max_length=100,null=True, blank=True)
    category = models.CharField(max_length=100,null=True, blank=True)
    patient = models.ManyToManyField(Patient)
