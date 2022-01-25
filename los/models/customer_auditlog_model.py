from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Customerauditlog(models.Model):
    id = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True)
    salutation = models.PositiveSmallIntegerField(validators=[MinValueValidator(0),
                                                              MaxValueValidator(9)], null=True)
    first_name = models.TextField(null=False)
    middle_name = models.TextField(null=True)
    last_name = models.TextField(null=True)
    gender = models.PositiveSmallIntegerField(validators=[MinValueValidator(0),
                                                          MaxValueValidator(9)], null=True)
    date_of_birth = models.DateTimeField(null=True)
    relation_with_applicant = models.PositiveSmallIntegerField(validators=[MinValueValidator(0),
                                                                           MaxValueValidator(9)], null=True)
    marital_status = models.PositiveSmallIntegerField(validators=[MinValueValidator(0),
                                                                  MaxValueValidator(9)], null=True)
    father_first_name = models.TextField(null=True)
    father_middle_name = models.TextField(null=True)
    father_last_name = models.TextField(null=True)
    mother_first_name = models.TextField(null=True)
    mother_middle_name = models.TextField(null=True)
    mother_last_name = models.TextField(null=True)
    spouse_first_name = models.TextField(null=True)
    spouse_middle_name = models.TextField(null=True)
    spouse_last_name = models.TextField(null=True)
    no_of_family_members = models.PositiveSmallIntegerField(validators=[MinValueValidator(0),
                                                                        MaxValueValidator(99)], null=True)
    household_income_monthly = models.IntegerField(max_length=20, null=True)
    status = models.PositiveSmallIntegerField(validators=[MinValueValidator(0),
                                                          MaxValueValidator(9)], null=True)
    creation_date = models.DateTimeField(null=False)
    creation_by = models.TextField(null=False)

