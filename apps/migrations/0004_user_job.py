# Generated by Django 5.1.1 on 2024-10-12 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_user_address_user_mobile_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='job',
            field=models.CharField(choices=[('full stack developer', 'Full Stack Developer'), ('designer', 'Designer')], default='full stack developer', max_length=255),
        ),
    ]