from django.db import models

# Create your models here.

class Type(models.Model):
    nomi = models.CharField(max_length=20)

    def __str__(self):
        return self.nomi

class Portfolio(models.Model):
    nomi = models.CharField(max_length=30)
    company_name = models.CharField(max_length=30)
    rasm = models.ImageField(upload_to='media')
    rasm1 = models.ImageField(upload_to='media',null=True,blank=True)
    rasm2 = models.ImageField(upload_to='media', null=True, blank=True)
    tur = models.ForeignKey(Type,models.CASCADE)
    sana = models.DateField()
    link = models.CharField(max_length=100)



class Malumot(models.Model):
    matn = models.CharField(max_length=200)

    def __str__(self):
        return self.matn

class Service(models.Model):
    nomi = models.CharField(max_length=30)
    rasm = models.ImageField(upload_to='media')
    rasm1 = models.ImageField(upload_to='media', null=True, blank=True)
    rasm2 = models.ImageField(upload_to='media', null=True, blank=True)
    malumot = models.ForeignKey(Malumot,models.CASCADE)



class Lavozim(models.Model):
    nomi = models.CharField(max_length=30)

    def __str__(self):
        return self.nomi


class Teams(models.Model):
    ism = models.CharField(max_length=20)
    familya = models.CharField(max_length=20)
    yosh = models.IntegerField()
    lavozim = models.ForeignKey(Lavozim,models.CASCADE)
    rasm = models.ImageField(upload_to='media')
    telegram = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    malumot = models.CharField(max_length=100)

class Murojat(models.Model):
    ism = models.CharField(max_length=30)
    gmail = models.CharField(max_length=100)
    title = models.CharField(max_length=20)
    text = models.TextField()
    vaqt = models.DateField()

# class Gmail(models.Model):
#     gmail = models.CharField(max_length=100)
#     vaqt = models.DateField()