# Generated by Django 4.1.3 on 2023-01-10 11:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0017_alter_appointment_options_alter_comment_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Klient'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.employee', verbose_name='Fryzjer'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='service',
            field=models.ManyToManyField(to='home.service', verbose_name='Usługa'),
        ),
    ]