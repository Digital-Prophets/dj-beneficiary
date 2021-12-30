# Generated by Django 4.0 on 2021-12-30 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=200, verbose_name='Last Name')),
                ('birthdate', models.DateField(blank=True, null=True, verbose_name='Birth Date')),
                ('agent_id', models.CharField(editable=False, max_length=100)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender'), ('Other', 'Other')], default='Other', max_length=50, verbose_name='Gender')),
            ],
            options={
                'verbose_name': 'Agent',
                'verbose_name_plural': 'Agents',
            },
        ),
        migrations.CreateModel(
            name='FacilityType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Facility Type Name')),
            ],
        ),
        migrations.CreateModel(
            name='ImplementingPartner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('ip_type', models.IntegerField(choices=[(1, 'Non-Profit Organization'), (2, 'Company'), (3, 'Government'), (4, 'Other')], default=1, verbose_name='Type')),
                ('is_active', models.BooleanField(default=True, help_text='Is still an active Implementing Partner', verbose_name='Is Active')),
            ],
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hmis_code', models.CharField(blank=True, max_length=100, null=True, verbose_name='HMIS Code')),
                ('name', models.CharField(help_text="Just enter name without 'Hostpial' or 'Clinic`, i.e for `Kitwe General Hospital` just enter `Kitwe General`.", max_length=200, verbose_name='Name')),
                ('facility_type', models.ForeignKey(default=1, help_text="Facility Type, i.e 'Hospital, Clinic etc", max_length=250, on_delete=django.db.models.deletion.CASCADE, to='dj_beneficiary.facilitytype')),
                ('implementing_partner', models.ForeignKey(blank=True, help_text='Related Implementing Partner.', max_length=250, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dj_beneficiary.implementingpartner')),
            ],
            options={
                'verbose_name': 'Facility',
                'verbose_name_plural': 'Facilities',
            },
        ),
    ]
