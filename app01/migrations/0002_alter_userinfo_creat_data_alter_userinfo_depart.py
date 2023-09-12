# Generated by Django 4.2.4 on 2023-08-19 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='creat_data',
            field=models.DateField(auto_now=True, verbose_name='入职时间'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='depart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app01.department', verbose_name='部门'),
        ),
    ]
