from tkinter.tix import COLUMN
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Education(models.Model):
    id = models.BigAutoField(primary_key=True)
    customer_id=models.BigIntegerField(null=False)
    institute_id=models.BigIntegerField(null=False)
    institute_name=models.TextField(null=True)
    course_id=models.BigIntegerField(null=False)
    course_name=models.TextField(null=True)
    stream_id=models.BigIntegerField(null=False)
    stream_name=models.TextField(null=True)
    start_month_year=models.DateField(null=True)
    end_month_year=models.DateField(null=False)
    marks=models.IntegerField(null=False)
    max_marks=models.PositiveSmallIntegerField(validators=[MinValueValidator(1),
                                                              MaxValueValidator(999)], null=False)
    marks_type=models.PositiveSmallIntegerField(validators=[MinValueValidator(10),
                                                              MaxValueValidator(99)], null=False)
    duration_months=models.PositiveSmallIntegerField(validators=[MinValueValidator(1),
                                                              MaxValueValidator(99)], null=True)
    course_type=models.PositiveSmallIntegerField(validators=[MinValueValidator(10),
                                                              MaxValueValidator(99)], null=True)
    status=models.PositiveSmallIntegerField(validators=[MinValueValidator(1),
                                                              MaxValueValidator(9)], null=False)
    
    creation_date = models.DateTimeField(null=False)
    creation_by = models.TextField(null=False)
    updation_date = models.DateTimeField(null=True)
    updation_by = models.TextField(null=True)
