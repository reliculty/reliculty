from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    dob = models.DateField()
    age = models.IntegerField()
    phone = models.CharField(max_length=20)
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    address = models.TextField()
    district = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    ACCOUNT_CHOICES = [
        ('savings', 'Savings'),
        ('current', 'Current'),
    ]
    account_type = models.CharField(max_length=10, choices=ACCOUNT_CHOICES)
    debit_card = models.BooleanField(default=False)
    credit_card = models.BooleanField(default=False)
    cheque_book = models.BooleanField(default=False)

    def __str__(self):
        return self.name
