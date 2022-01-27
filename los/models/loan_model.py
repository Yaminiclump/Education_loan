from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Loan(models.Model):
    id = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True)
    # amount =
    # base_rate =
    # margin =
    # fixed_rate =
    # is_fixed_rate =
    # fixed_rate_months =
    # moratorium_period_months =
    # study_period_months =
    # grace_period_months =
    # tenure_months =
    # moratorium_start_date =
    # emi_start_date =
    # repayment_type =
    # application_number =
    # ext_ref_no =
    # source_id =