
from tkinter import CASCADE
from django.db import models

# # Create your models here


class Pollingunit (models.Model):
    uniqueid = models.IntegerField()
    polling_unit_id =models.IntegerField()
    ward_id =   models.IntegerField()
    lga_id =models.IntegerField()
    uniqueward_id=models.IntegerField()
    polling_unit_number =models.IntegerField()
    polling_unit_name = models.CharField(max_length=1000)
    polling_unit_description =  models.CharField(max_length=1000)
    date_entered  = models.DateTimeField(null=True)
    user_ip_address = models.IntegerField()
    


class Lga(models.Model):
    uniqueid = models.IntegerField()
    lga_id  =models.IntegerField()
    lga_name = models.CharField(max_length=1000)
    state_id  = models.IntegerField()
    lga_description  = models.CharField(max_length=1000)
    entered_by_user = models.CharField(max_length=1000)
    date_entered   = models.DateTimeField(null= True)
    user_ip_address = models.IntegerField()
    pollingunit= models.ManyToManyField(Pollingunit)

class Ward(models.Model):
    uniqueid =models.IntegerField()
    ward_id = models.IntegerField()
    ward_name = models.CharField(max_length=1000)
    lga_id = models.IntegerField()
    ward_description = models.CharField(max_length=1000)
    entered_by_user =models.CharField(max_length=1000) 
    date_entered  = models.DateTimeField(null = True)
    user_ip_address =models.IntegerField()


class Party(models.Model):
    partyid = models.CharField(max_length=1000)
    partyname =models.CharField(max_length=1000)


class announced_lga_results(models.Model):
    lga_name  = models.CharField(max_length=1000)
    party_abbreviation = models.CharField(max_length=1000)
    party_score = models.CharField(max_length=1000) 
    entered_by_user = models.CharField(max_length=1000) 
    date_entered  =models.DateTimeField(null=True)
    user_ip_address = models.IntegerField()

class announced_pu_results(models.Model):
     result_id = models.IntegerField()
     polling_unit_uniqueid  = models.IntegerField()
     party_abbreviation   =models.IntegerField()
     party_score   =models.IntegerField()
     entered_by_user = models.CharField(max_length=1000) 
     date_entered   =models.DateTimeField(null = True)
     user_ip_address =  models.IntegerField()