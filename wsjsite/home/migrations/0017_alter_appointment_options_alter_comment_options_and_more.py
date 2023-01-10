# Generated by Django 4.1.3 on 2023-01-10 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_alter_products_options_alter_unavailability_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appointment',
            options={'verbose_name_plural': 'Wizyta'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name_plural': 'Komentarze'},
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name_plural': 'Fryzjerzy'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name_plural': 'Usługi'},
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateTimeField(verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='service',
            field=models.ManyToManyField(related_name='Usługa', to='home.service'),
        ),
    ]