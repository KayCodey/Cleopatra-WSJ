# Generated by Django 4.1.3 on 2023-01-10 17:12

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Imię')),
                ('last_name', models.CharField(max_length=100, verbose_name='Nazwisko')),
                ('phone_number', models.CharField(max_length=20, unique=True, validators=[django.core.validators.MinLengthValidator(9)], verbose_name='Numer telefonu')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-mail')),
                ('login', models.CharField(max_length=20, unique=True, validators=[django.core.validators.MinLengthValidator(5)], verbose_name='Login')),
                ('password', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(8)], verbose_name='Hasło')),
                ('image', models.ImageField(null=True, upload_to='photos', verbose_name='Zdjęcie')),
            ],
            options={
                'verbose_name_plural': 'Fryzjerzy',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100, verbose_name='Nazwa produktu')),
                ('product_type', models.CharField(max_length=100, verbose_name='Typ')),
                ('manufacturer', models.CharField(max_length=100, verbose_name='Producent')),
                ('amount', models.IntegerField(verbose_name='Ilość')),
            ],
            options={
                'verbose_name_plural': 'Produkty',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=100, verbose_name='Usługa')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Cena')),
                ('approx_time', models.DurationField(verbose_name='Przewidywany czas')),
            ],
            options={
                'verbose_name_plural': 'Usługi',
            },
        ),
        migrations.CreateModel(
            name='Unavailability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(verbose_name='Początek')),
                ('end_date', models.DateTimeField(verbose_name='Koniec')),
                ('worker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.employee', verbose_name='Fryzjer')),
            ],
            options={
                'verbose_name': 'Niedostępność',
                'verbose_name_plural': 'Niedostępność',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, verbose_name='Username')),
                ('user_email', models.EmailField(max_length=254, verbose_name='E-mail klienta')),
                ('text', models.TextField(max_length=400, verbose_name='Treść')),
                ('service_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.service', verbose_name='Usługa')),
                ('worker_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.employee', verbose_name='Fryzjer')),
            ],
            options={
                'verbose_name_plural': 'Komentarze',
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Zrealizowana', 'Zrealizowana'), ('Zaplanowana', 'Zaplanowana'), ('Odwołana', 'Odwołana')], default='Zaplanowana', max_length=100)),
                ('date', models.DateTimeField(verbose_name='Data')),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Klient')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.employee', verbose_name='Fryzjer')),
                ('service', models.ManyToManyField(to='home.service', verbose_name='Usługa')),
            ],
            options={
                'verbose_name_plural': 'Wizyta',
            },
        ),
    ]
