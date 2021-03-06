# Generated by Django 3.0.6 on 2020-06-02 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0002_case_owner'),
        ('users', '0002_donation_report_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='case_donations',
            field=models.ManyToManyField(blank=True, related_name='donations', through='users.Donation', to='cases.Case'),
        ),
        migrations.AddField(
            model_name='user',
            name='case_reports',
            field=models.ManyToManyField(blank=True, related_name='reports', through='users.Report', to='cases.Case'),
        ),
        migrations.AddField(
            model_name='user',
            name='case_votes',
            field=models.ManyToManyField(blank=True, related_name='votes', through='users.Vote', to='cases.Case'),
        ),
    ]
