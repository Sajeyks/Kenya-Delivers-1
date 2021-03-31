# Generated by Django 3.1.6 on 2021-03-18 03:14

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('date_of_birth', models.DateField()),
                ('county', models.CharField(choices=[(1, 'Mombasa'), (2, 'Kwale'), (3, 'Kilifi'), (4, 'Tana River'), (5, 'Lamu'), (6, 'Taita/Taveta'), (7, 'Garissa'), (8, 'Wajir'), (9, 'Mandera'), (10, ' Marsabit'), (11, 'Isiolo'), (12, 'Meru'), (13, 'Tharaka-Nithi'), (14, 'Embu'), (15, 'Kitui'), (16, 'Machakos'), (17, 'Makueni'), (18, 'Nyandarua'), (19, 'Nyeri'), (20, 'Kirinyaga'), (21, "Murang'a"), (22, 'Kiambu'), (23, 'Turkana'), (24, 'West Pokot'), (25, 'Samburu'), (26, 'Trans Nzoia'), (27, 'Uasin Gishu'), (28, 'Elgeyo/Marakwet'), (29, 'Nandi'), (30, 'Baringo'), (31, 'Laikipia'), (32, 'Nakuru'), (33, 'Narok'), (34, 'Kajiado'), (35, 'Kericho'), (36, 'Bomet'), (37, 'Kakamega'), (38, 'Vihiga'), (39, 'Bungoma'), (40, 'Busia'), (41, 'Siaya'), (42, 'Kisumu'), (43, 'Homa Bay'), (44, 'Migori'), (45, 'Kisii'), (46, 'Nyamira'), (47, 'Nairobi City')], max_length=30)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
