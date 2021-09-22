# Generated by Django 3.2.4 on 2021-09-22 07:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0017_alter_passwordresetinfo_expires_at'),
        ('api', '0010_auto_20210921_1915'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('lastupdated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.UUIDField(default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'), primary_key=True, serialize=False)),
                ('rate_value', models.FloatField(default=0.0)),
                ('reason', models.CharField(max_length=100)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_rating_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('lastupdated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_rating_lastmodified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by')),
            ],
            options={
                'ordering': ['-lastupdated_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PassengerRating',
            fields=[
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('lastupdated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.UUIDField(default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'), primary_key=True, serialize=False)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_passengerrating_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('lastupdated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_passengerrating_lastmodified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by')),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.passenger')),
                ('rating', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.rating')),
            ],
            options={
                'ordering': ['-lastupdated_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DriverRating',
            fields=[
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('lastupdated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.UUIDField(default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'), primary_key=True, serialize=False)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_driverrating_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.driver')),
                ('lastupdated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_driverrating_lastmodified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by')),
                ('rating', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.rating')),
            ],
            options={
                'ordering': ['-lastupdated_at'],
                'abstract': False,
            },
        ),
    ]
