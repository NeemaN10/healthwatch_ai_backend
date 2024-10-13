# Generated by Django 5.1.2 on 2024-10-13 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inmate_id', models.CharField(max_length=16)),
                ('description', models.CharField(max_length=2000)),
                ('duration', models.CharField(choices=[('LESS_THAN_A_DAY', 'Less Than A Day'), ('ONE_TO_THREE_DAYS', '1 - 3 Days'), ('FOUR_TO_SEVEN_DAYS', '4 - 7 Days'), ('ONE_TO_FOUR_WEEKS', '1 - 4 Weeks'), ('MORE_THAN_A_MONTH', 'More than a month')], max_length=30)),
            ],
        ),
    ]
