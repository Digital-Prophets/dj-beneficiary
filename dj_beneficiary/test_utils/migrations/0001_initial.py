# Generated by Django 4.0 on 2021-12-29 21:33

from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dj_beneficiary', '0001_initial'),
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
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='District')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hmis_code', models.CharField(blank=True, max_length=100, null=True, verbose_name='HMIS Code')),
                ('name', models.CharField(help_text="Just enter name without 'Hostpial' or 'Clinic`, i.e for `Kitwe General Hospital` just enter `Kitwe General`.", max_length=200, verbose_name='Name')),
                ('district', models.ForeignKey(default=1, help_text='District in which the facility is located', max_length=250, on_delete=django.db.models.deletion.CASCADE, to='test_utils.district')),
                ('facility_type', models.ForeignKey(default=1, help_text="Facility Type, i.e 'Hospital, Clinic etc", max_length=250, on_delete=django.db.models.deletion.CASCADE, to='dj_beneficiary.facilitytype')),
                ('implementing_partner', models.ForeignKey(blank=True, help_text='Related Implementing Partner.', max_length=250, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dj_beneficiary.implementingpartner')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Province')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='District')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_utils.district')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrganizationBeneficiary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Organization Name')),
                ('org_type', models.CharField(choices=[('coorperative', 'Co-orperative'), ('businessfirm', 'Business Firm'), ('Other', 'Other')], max_length=100, verbose_name='Organization Type')),
                ('logo', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='org_logos')),
                ('total_beneficiaries', models.IntegerField(blank=True, null=True, verbose_name='Total Individual Beneficiary Count')),
                ('total_females', models.IntegerField(blank=True, null=True, verbose_name='Total Female Count')),
                ('total_males', models.IntegerField(blank=True, null=True, verbose_name='Total Male Count')),
                ('total_hhs', models.IntegerField(blank=True, null=True, verbose_name='Total HHs')),
                ('female_hhs', models.IntegerField(blank=True, null=True, verbose_name='Female HHs')),
                ('below_sixteen', models.IntegerField(blank=True, null=True, verbose_name='Below 16 Years Old')),
                ('sixteen_to_thirty', models.IntegerField(blank=True, null=True, verbose_name='16 to 30 Years Old')),
                ('thirty_to_fourty_five', models.IntegerField(blank=True, null=True, verbose_name='30 to 40 Years Old')),
                ('above_fourty_five', models.IntegerField(blank=True, null=True, verbose_name='Above 40 Years Old')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('email', models.EmailField(blank=True, max_length=200, null=True, verbose_name='Email')),
                ('cell', models.CharField(blank=True, max_length=100, null=True, verbose_name='Phone Number')),
                ('registered_date', models.DateField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('ward', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='test_utils.ward')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IndividualBeneficiary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=200, verbose_name='Last Name')),
                ('other_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Other Name')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender'), ('Other', 'Other')], default='Other', max_length=100, verbose_name='Gender')),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100, verbose_name='Sex')),
                ('profile_photo', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='profile_photo')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Phone Number')),
                ('email', models.EmailField(blank=True, max_length=200, null=True, verbose_name='Email')),
                ('beneficiary_id', models.CharField(editable=False, max_length=100)),
                ('art_status', models.CharField(blank=True, choices=[('Enrolled', 'Enrolled'), ('Not Enrolled', 'Not Enrolled')], max_length=100, null=True, verbose_name='ART Status')),
                ('last_vl', models.IntegerField(blank=True, null=True, verbose_name='Last Viral Load')),
                ('hiv_status', models.CharField(blank=True, choices=[('positive', 'Positive'), ('negative', 'Negative'), ('unkown', 'Uknown')], max_length=100, null=True, verbose_name='HIV Status')),
                ('date_of_birth', models.DateField(verbose_name='Date of Birth')),
                ('marital_status', models.CharField(blank=True, choices=[('single', 'Single'), ('married', 'Married'), ('seperated', 'Seperated'), ('divorced', 'Divorced'), ('widowed', 'Widowed')], max_length=100, null=True, verbose_name='Marital Status')),
                ('name_of_spouse', models.CharField(blank=True, max_length=200, null=True, verbose_name='Phone Number')),
                ('number_of_children', models.IntegerField(blank=True, null=True, verbose_name='Number of children')),
                ('number_of_siblings', models.IntegerField(blank=True, null=True, verbose_name='Number of siblings')),
                ('education_level', models.CharField(blank=True, choices=[('none', 'None'), ('primary', 'Primary'), ('basic', 'Basic'), ('secondary', "Secondary O'Level"), ('certificate', 'Certificate'), ('diploma', 'Diploma'), ('degree', 'Degree'), ('masters', 'Masters'), ('doctrate', 'Doctrate'), ('phd', 'PHD')], max_length=300, null=True, verbose_name='Education level')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Address')),
                ('alive', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('registered_facility', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='registerd_facility', to='test_utils.facility')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='district',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_utils.province'),
        ),
    ]
