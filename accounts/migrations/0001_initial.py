# Generated by Django 4.0.3 on 2022-05-29 00:53

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('prenom', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('nom', models.CharField(max_length=30)),
                ('bio', models.TextField(null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='')),
                ('date_de_naissance', models.DateField(blank=True, null=True)),
                ('phone_number', models.CharField(max_length=150, null=True)),
                ('commune', models.CharField(choices=[('--COMMUNES--', '--COMMUNES--'), ('BDLG', 'Bandalungwa'), ('BRBU', 'Barumbu'), ('BMBU', 'Bumbu'), ('GMBE', 'Gombe'), ('KLMU', 'Kalamu'), ('KAVU', 'Kasavubu'), ('KBSK', 'Kimbanseke'), ('KINS', 'Kinshasa'), ('KINT', 'Kintambo'), ('KISE', 'Kisenso'), ('LMBA', 'Lemba'), ('LMTE', 'Limete'), ('MKLA', 'Makala'), ('MLKU', 'Maluku'), ('MSNA', 'Masina'), ('MATT', 'Matete'), ('MTNG', 'Montngafula'), ('NDLI', 'Ndjili'), ('NGBA', 'Ngaba'), ('NGLM', 'Ngaliema'), ('NSLE', 'Nsele'), ('SLBO', 'Selembao'), ('LGLA', 'lingwala')], default='KINS', max_length=255)),
                ('joined', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'auth_user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='EarlyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=150)),
                ('registered', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=150)),
                ('model', models.CharField(choices=[('--Phone model--', '--Phone model--'), ('Iphone 5', 'Iphone 5'), ('Iphone 6', 'Iphone 6'), ('Iphone 6+', 'Iphone 6+'), ('Iphone7', 'Iphone7'), ('Iphone 7+', 'Iphone 7+'), ('Iphone 8', 'Iphone 8'), ('Iphone 8+', 'Iphone 8+'), ('Iphone X', 'Iphone X'), ('Iphone XR', 'Iphone XR'), ('Iphone XS max', 'Iphone XS max'), ('Iphone 11', 'Iphone 11'), ('Iphone 11 Pro', 'Iphone 11 Pro'), ('Iphone 11 Pro Max', 'Iphone 11 Pro Max'), ('Iphone 12', 'Iphone 12'), ('Iphone 12 pro', 'Iphone 12 pro'), ('Iphone 12 pro max', 'Iphone 12 pro max'), ('Iphone 13', 'Iphone 13'), ('Iphone 13 pro max', 'Iphone 13 pro max'), ('Samsung s6', 'Samsung s6'), ('Samsung s6 edge', 'Samsung s6 edge'), ('Samsung s6 edge+', 'Samsung s6 edge+'), ('Samsung s7', 'Samsung s7'), ('Samsung s7 edge', 'Samsung s7 edge'), ('Samsung s8', 'Samsung s8'), ('Samsung s8 edge', 'Samsung s8 edge'), ('Samsung s8 edge+', 'Samsung s8 edge+'), ('Samsung s9', 'Samsung s9'), ('Samsung s10', 'Samsung s10'), ('Samsung s10+', 'Samsung s10+'), ('Samsung Note 8', 'Samsung Note 8'), ('Samsung Note 9,', 'Samsung Note 9'), ('Samsung Note 9 Duos', 'Samsung Note 9 Duos'), ('Samsung Note 10', 'Samsung Note 10'), ('Techno Pop3', 'Techno Pop3'), ('Techno Spark4', 'Techno Spark4'), ('Techno Spark 5', 'Techno Spark 5'), ('Techno Spark 5 Air', 'Techno Spark 5 Air'), ('Techno Camon 16s', 'Techno Camon 16s'), ('Techno Camo 16', 'Techno Camo 16'), ('Techno Camon 15 Premier', 'Techno Camon 15 Premier')], default='--Phone model--', max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('cat', models.CharField(choices=[('--CATEGORIE DU PRODUIT--', '--CATEGORIE DU PRODUIT--'), ('phone', 'phone'), ('tablette', 'tablette'), ('TV', 'TV'), ('ordinateur', 'ordinateur'), ('moniteur', 'moniteur'), ('console', 'console')], default='--Categorie du produit--', max_length=150)),
                ('price', models.CharField(default='no price', max_length=5)),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d')),
                ('fissure1', models.PositiveIntegerField(default=0)),
                ('fissure2', models.PositiveIntegerField(default=0)),
                ('imei', models.CharField(max_length=150)),
                ('battery', models.CharField(max_length=150)),
                ('is_sold', models.BooleanField(default=False)),
                ('memory', models.CharField(choices=[('--MEMORY', '--MEMORY--'), ('512GB', '512GB'), ('256GB', '256GB'), ('128GB', '128GB'), ('64GB', '64GB'), ('32GB', '32GB'), ('16GB', '16GB')], default='--MEMORY--', max_length=255)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
