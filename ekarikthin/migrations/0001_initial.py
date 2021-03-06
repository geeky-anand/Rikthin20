# Generated by Django 2.2 on 2019-12-27 08:25

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contacts',
            fields=[
                ('contact_id', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phno', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{10,10}$')])),
                ('fbLink', models.CharField(max_length=254)),
                ('profileImage', models.ImageField(blank=True, null=True, upload_to='static/ekarikthin/img/contacts/')),
            ],
        ),
        migrations.CreateModel(
            name='events',
            fields=[
                ('eventCode', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('noOfParticipants', models.IntegerField(default=0)),
                ('organizers', models.CharField(max_length=30)),
                ('volunteers', models.CharField(max_length=30)),
                ('regFee', models.IntegerField(default=0)),
                ('prizes', models.CharField(max_length=16)),
                ('timeSlot', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='payment',
            fields=[
                ('paymentToken', models.CharField(max_length=256, primary_key=True, serialize=False)),
                ('timeStamp', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='registeredUsers',
            fields=[
                ('regNo', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('emailId', models.EmailField(max_length=254)),
                ('password', models.CharField(default=models.EmailField(max_length=254), max_length=16)),
                ('phno', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{10,10}$')])),
                ('instName', models.CharField(max_length=100)),
                ('paymentToken', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ekarikthin.payment')),
            ],
        ),
    ]
