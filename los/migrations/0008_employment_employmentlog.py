# Generated by Django 3.2.8 on 2022-02-15 08:39

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('los', '0007_rename_customercontact_customercontactlog_customer_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employment',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('type', models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99)])),
                ('employer_id', models.BigIntegerField(null=True)),
                ('employer_name', models.TextField(null=True)),
                ('address_id', models.BigIntegerField(null=True)),
                ('designation_id', models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99)])),
                ('designation_name', models.TextField(null=True)),
                ('retirement_age_years', models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99)])),
                ('current_employer_months', models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99)])),
                ('gross_income_monthly', models.IntegerField()),
                ('net_income_monthly', models.IntegerField()),
                ('other_income_monthly', models.IntegerField(null=True)),
                ('work_experience_month', models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99)])),
                ('status', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9)])),
                ('creation_date', models.DateTimeField()),
                ('creation_by', models.TextField()),
                ('updation_date', models.DateTimeField(null=True)),
                ('updation_by', models.TextField(null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='los.customer')),
            ],
            options={
                'db_table': 'los_empolyment',
            },
        ),

    ]
