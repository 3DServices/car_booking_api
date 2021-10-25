# Generated by Django 3.2.4 on 2021-10-25 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0029_alter_passwordresetinfo_expires_at'),
        ('api', '0021_alter_departmentpassenger_passenger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departmentdriver',
            name='driver',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authentication.driver'),
        ),
    ]
