# Generated by Django 4.2.7 on 2023-11-24 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='certificate',
            field=models.CharField(choices=[('U', 'U'), ('PG', 'PG'), ('12a', '12a'), ('15', '15'), ('18', '18')], max_length=3),
        ),
    ]
