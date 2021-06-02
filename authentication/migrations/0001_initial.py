# Generated by Django 3.2.2 on 2021-06-02 12:42

import authentication.models
from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, unique=True, verbose_name='email address')),
                ('is_verified', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('Id', models.CharField(default=uuid.UUID('27331ea9-5f87-45f3-af8a-d578fb08bc86'), max_length=50, primary_key=True, serialize=False)),
                ('primary_contact', phonenumber_field.modelfields.PhoneNumberField(default='+256777777777', max_length=128, region=None)),
                ('secondary_contact', phonenumber_field.modelfields.PhoneNumberField(default='+256777777777', max_length=128, region=None)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', authentication.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='SystemAdmin',
            fields=[
                ('id', models.CharField(default=uuid.UUID('fdd2b784-ddd1-4205-b17c-2ec32a5fd9d7'), max_length=50, primary_key=True, serialize=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='SysAdmin', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.CharField(default=uuid.UUID('b3357eab-03fb-47f3-9477-e76d39e2f0a3'), max_length=50, primary_key=True, serialize=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Passenger', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FleetManager',
            fields=[
                ('id', models.CharField(default=uuid.UUID('a188d541-3f97-474f-8e2b-670c26fee3de'), max_length=50, primary_key=True, serialize=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='FleetManager', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.CharField(default=uuid.UUID('bf9719cc-bc04-40e8-acb0-ab254a6d78f4'), max_length=50, primary_key=True, serialize=False)),
                ('permit_number', models.CharField(default='UAX', max_length=50)),
                ('permit_class', models.CharField(default='UAX', max_length=50)),
                ('permit_expiry_date', models.CharField(default='UAX', max_length=50)),
                ('permit_issuance_date', models.CharField(default='UAX', max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Driver', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
