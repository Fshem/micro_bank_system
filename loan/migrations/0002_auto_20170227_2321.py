# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-02-27 20:21
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('loan', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atmcard',
            name='atm_current',
        ),
        migrations.RemoveField(
            model_name='atmcard',
            name='atm_saving',
        ),
        migrations.RemoveField(
            model_name='personal_information',
            name='address',
        ),
        migrations.RemoveField(
            model_name='personal_information',
            name='atm_card',
        ),
        migrations.RemoveField(
            model_name='personal_information',
            name='current_ac',
        ),
        migrations.RemoveField(
            model_name='personal_information',
            name='economic',
        ),
        migrations.RemoveField(
            model_name='personal_information',
            name='loan_ac',
        ),
        migrations.RemoveField(
            model_name='personal_information',
            name='saving_ac',
        ),
        migrations.AlterField(
            model_name='economic',
            name='econ_life',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='guarantor',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.Addresse'),
        ),
        migrations.AlterField(
            model_name='guarantor',
            name='pin_no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='loan',
            name='loan_period',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='loan',
            name='participant_no',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='other_borrower',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.Addresse'),
        ),
        migrations.AlterField(
            model_name='other_borrower',
            name='pin_no',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='Addresse',
        ),
        migrations.DeleteModel(
            name='ATMCard',
        ),
        migrations.DeleteModel(
            name='CurrentAccount',
        ),
        migrations.DeleteModel(
            name='Personal_Information',
        ),
        migrations.DeleteModel(
            name='SavingAccount',
        ),
    ]
