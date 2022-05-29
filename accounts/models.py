
from email.policy import default
from operator import truediv
from secrets import choice
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime



#Session.objects.all().delete() : to clear the current session.

CAT_CHOICES = [
    ('--CATEGORIE DU PRODUIT--', '--CATEGORIE DU PRODUIT--'),
    ('phone', 'phone'),
    ('tablette', 'tablette'),
    ('TV', 'TV'),
    ('ordinateur', 'ordinateur'),
    ('moniteur', 'moniteur'),
    ('console', 'console',)
]

COMMUNES = [
    ('--COMMUNES--', '--COMMUNES--'),
    ('BDLG', 'Bandalungwa'),
    ('BRBU', 'Barumbu'),
    ('BMBU', 'Bumbu'),
    ('GMBE', 'Gombe'),
    ('KLMU', 'Kalamu'),
    ('KAVU', 'Kasavubu'),
    ('KBSK','Kimbanseke'),
    ('KINS', 'Kinshasa'),
    ('KINT', 'Kintambo'),
    ('KISE', 'Kisenso'),
    ('LMBA', 'Lemba'),
    ('LMTE', 'Limete'),
    ('MKLA', 'Makala'),
    ('MLKU', 'Maluku'),
    ('MSNA', 'Masina'),
    ('MATT', 'Matete'),
    ('MTNG', 'Montngafula'),
    ('NDLI', 'Ndjili'),
    ('NGBA', 'Ngaba'),
    ('NGLM', 'Ngaliema'),
    ('NSLE', 'Nsele'),
    ('SLBO', 'Selembao'),
    ('LGLA','lingwala'),
    ]

MODEL_CHOICES = [
    ('--Phone model--', '--Phone model--'),
    ('Iphone 5', 'Iphone 5'),
    ('Iphone 6', 'Iphone 6'),
    ('Iphone 6+', 'Iphone 6+'),
    ('Iphone7' , 'Iphone7'),
    ('Iphone 7+', 'Iphone 7+'),
    ('Iphone 8','Iphone 8'),
    ('Iphone 8+', 'Iphone 8+'),			
    ('Iphone X','Iphone X'),				
    ('Iphone XR', 'Iphone XR'),				
    ('Iphone XS max', 'Iphone XS max'),			
    ('Iphone 11', 'Iphone 11'),
    ('Iphone 11 Pro', 'Iphone 11 Pro'),	
    ('Iphone 11 Pro Max', 'Iphone 11 Pro Max'),		
    ('Iphone 12', 'Iphone 12'),	
    ('Iphone 12 pro', 'Iphone 12 pro'),		
    ('Iphone 12 pro max', 'Iphone 12 pro max'),			
    ('Iphone 13', 'Iphone 13'),	
    ('Iphone 13 pro max', 'Iphone 13 pro max'),			
    ('Samsung s6', 'Samsung s6'),				
    ('Samsung s6 edge', 'Samsung s6 edge'),				
    ('Samsung s6 edge+', 'Samsung s6 edge+'),				
    ('Samsung s7', 'Samsung s7'),				
    ('Samsung s7 edge', 'Samsung s7 edge'),			
    ('Samsung s8', 'Samsung s8'),				
    ('Samsung s8 edge', 'Samsung s8 edge'),				
    ('Samsung s8 edge+', 'Samsung s8 edge+'),				
    ('Samsung s9', 'Samsung s9'),				
    ('Samsung s10', 'Samsung s10'),				
    ('Samsung s10+', 'Samsung s10+'),				
    ('Samsung Note 8', 'Samsung Note 8'),				
    ('Samsung Note 9,', 'Samsung Note 9'),			
    ('Samsung Note 9 Duos', 'Samsung Note 9 Duos'),				
    ('Samsung Note 10', 'Samsung Note 10'),			
    ('Techno Pop3', 'Techno Pop3'),					
    ('Techno Spark4', 'Techno Spark4'),				
    ('Techno Spark 5', 'Techno Spark 5'),				
    ('Techno Spark 5 Air', 'Techno Spark 5 Air'),				
    ('Techno Camon 16s', 'Techno Camon 16s'),				
    ('Techno Camo 16', 'Techno Camo 16'),				
    ('Techno Camon 15 Premier', 'Techno Camon 15 Premier')
]

MEMORY_CHOICES = [
    ('--MEMORY', '--MEMORY--'),
    ('512GB', '512GB'),
    ('256GB', '256GB'),
    ('128GB', '128GB'),
    ('64GB', '64GB'),
    ('32GB', '32GB'),
    ('16GB', '16GB'),

    
]


now = datetime.now()

class Profile(AbstractUser):
    prenom = models.CharField(max_length=30)
    email = models.EmailField(unique=True, null=False)
    nom = models.CharField(max_length=30)
    bio = models.TextField(null=True)
    avatar = models.ImageField(blank=True, null=True)
    date_de_naissance = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=150, null=True)
    commune = models.CharField(default ='KINS', choices=COMMUNES, max_length=255)
    joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []


    def __str__(self):
        return f"{self.prenom} {self.nom}"

    class Meta:
        db_table = 'auth_user'

    @property
    def full_name(self):
        return '%s %s' % (self.prenom, self.nom)


class Product(models.Model):
    nom = models.CharField(max_length=150)
    model = models.CharField(default= '--Phone model--',  choices= MODEL_CHOICES, max_length=255)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update = models.DateTimeField(auto_now= True)
    cat = models.CharField(max_length=150, default = '--Categorie du produit--', choices=CAT_CHOICES)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    price = models.CharField(blank=False, default ="no price", max_length=5)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank =True)
    fissure1 = models.PositiveIntegerField(blank=False, default=0) #grosse fissures
    fissure2 = models.PositiveIntegerField(blank=False, default=0) #petites fissures
    imei = models.CharField(max_length=150, blank=False) # numero imei
    battery = models.CharField(blank=False, max_length=150) #pourcentage de battery
    is_sold = models.BooleanField(default=False) # est vandu ou pas vendu
    memory = models.CharField(default='--MEMORY--', choices= MEMORY_CHOICES, max_length=255)

    """Model, battery, fracture """


    def __str__(self):
        return self.nom

class EarlyUser(models.Model):
    nom = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    registered = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    def __str__(self):
        return f"{self.nom}"