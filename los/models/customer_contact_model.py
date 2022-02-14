from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class CustomerContact(models.Model):
    id = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey('Customer', on_delete=models.RESTRICT, null=False)
    type = models.PositiveSmallIntegerField(validators=[MinValueValidator(0),
                                                        MaxValueValidator(9)], null=False)
    value = models.TextField(null=False)
    value_extra_1 = models.TextField(null=True)
    country_code = models.PositiveSmallIntegerField(validators=[MinValueValidator(0),
                                                                MaxValueValidator(999)], null=True)
    status = models.PositiveSmallIntegerField(validators=[MinValueValidator(0),
                                                          MaxValueValidator(9)], null=False)
    creation_date = models.DateTimeField(null=False)
    creation_by = models.TextField(null=False)
    updation_date = models.DateTimeField(null=True)
    updation_by = models.TextField(null=True)

    class Meta:
        db_table = "los_customer_contact"


class CustomerContactLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey('Customer', on_delete=models.RESTRICT, null=False)
    contact = models.ForeignKey('CustomerContact', on_delete=models.RESTRICT, null=False)
    type = models.PositiveSmallIntegerField(validators=[MinValueValidator(0),
                                                        MaxValueValidator(9)], null=False)
    value = models.TextField(null=False)
    value_extra_1 = models.TextField(null=True)
    country_code = models.PositiveSmallIntegerField(validators=[MinValueValidator(0),
                                                                MaxValueValidator(999)], null=True)
    status = models.PositiveSmallIntegerField(validators=[MinValueValidator(0),
                                                          MaxValueValidator(9)], null=False)
    creation_date = models.DateTimeField(null=False)
    creation_by = models.TextField(null=False)

    class Meta:
        db_table = "los_customer_contact_log"
