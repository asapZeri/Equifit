# Generated by Django 5.2.1 on 2025-07-08 19:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0010_addhorse_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addhorse',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='horse_pics/'),
        ),
        migrations.CreateModel(
            name='Addrace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('race', models.CharField(choices=[('chief', 'Chief Race'), ('relay', 'Relay Race')], max_length=20)),
                ('date', models.DateField()),
                ('notes', models.TextField(blank=True)),
                ('horse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='races', to='tracker.addhorse')),
            ],
        ),
    ]
