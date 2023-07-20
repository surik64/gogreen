# Generated by Django 3.2.20 on 2023-07-20 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_user',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, default='', null=True, upload_to='profile'),
        ),
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
