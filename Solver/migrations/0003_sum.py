# Generated by Django 3.2 on 2021-05-16 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Solver', '0002_delete_sum'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=50)),
                ('sum_img', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
