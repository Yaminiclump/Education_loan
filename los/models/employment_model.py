from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Employment(models.Model):
    id = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey('Customer', on_delete=models.RESTRICT, null=False)
    type = models.PositiveSmallIntegerField(validators=[MinValueValidator(0),
                                                        MaxValueValidator(99)], null=True)
    employer_id = models.BigIntegerField(null=True)
    employer_name = models.TextField(null=True)
    address_id = models.BigIntegerField(null=True)
    designation_id = models.PositiveSmallIntegerField(validators=[MinValueValidator(0),
                                                        MaxValueValidator(99)], null=True)
    designation_name = models.TextField(null=True)
    retirement_age_years = models.PositiveSmallIntegerField(validators=[MinValueValidator(0),
                                                        MaxValueValidator(99)], null=True)
    current_employer_months = models.PositiveSmallIntegerField(validators=[MinValueValidator(0),
                                                        MaxValueValidator(99)], null=True)
    gross_income_monthly = models.IntegerField(null=False)
    net_income_monthly = models.IntegerField(null=False)
    other_income_monthly = models.IntegerField(null=True)
    work_experience_month = models.PositiveSmallIntegerField(validators=[MinValueValidator(0),
                                                        MaxValueValidator(99)], null=True)
    status = models.PositiveSmallIntegerField(validators=[MinValueValidator(0),
                                                          MaxValueValidator(9)], null=False)
    creation_date = models.DateTimeField(null=False)
    creation_by = models.TextField(null=False)
    updation_date = models.DateTimeField(null=True)
    updation_by = models.TextField(null=True)

    class Meta:
        db_table = "los_empolyment"

class EmploymentLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey('Customer', on_delete=models.RESTRICT, null=False)
    employment = models.ForeignKey('Employment', on_delete=models.RESTRICT, null=False)
    type = models.PositiveSmallIntegerField(validators=[MinValueValidator(0),
                                                        MaxValueValidator(99)], null=True)
    employer_id = models.BigIntegerField(null=True)
    employer_name = models.TextField(null=True)
    address_id = models.BigIntegerField(null=True)
    designation_id = models.PositiveSmallIntegerField(validators=[MinValueValidator(0),
                                                                  MaxValueValidator(99)], null=True)
    designation_name = models.TextField(null=True)
    retirement_age_years = models.PositiveSmallIntegerField(validators=[MinValueValidator(0),
                                                                        MaxValueValidator(99)], null=True)
    current_employer_months = models.PositiveSmallIntegerField(validators=[MinValueValidator(0),
                                                                           MaxValueValidator(99)], null=True)
    gross_income_monthly = models.IntegerField(null=False)
    net_income_monthly = models.IntegerField(null=False)
    other_income_monthly = models.IntegerField(null=True)
    work_experience_month = models.PositiveSmallIntegerField(validators=[MinValueValidator(0),
                                                                         MaxValueValidator(99)], null=True)
    status = models.PositiveSmallIntegerField(validators=[MinValueValidator(0),
                                                          MaxValueValidator(9)], null=False)
    creation_date = models.DateTimeField(null=False)
    creation_by = models.TextField(null=False)

    class Meta:
        db_table = "los_empolyment_log"