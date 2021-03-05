from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    # county choices
    KEN_COUNTIES =(
        (1,'Mombasa'),(2,'Kwale'),(3,'Kilifi'),(4,'Tana River'),(5,'Lamu'),(6,'Taita/Taveta'),(7,'Garissa'),(8,'Wajir'),
        (9,'Mandera'),(10,' Marsabit'),(11,'Isiolo'),(12,'Meru'),(13,'Tharaka-Nithi'),(14,'Embu'),
        (15,'Kitui'),(16,'Machakos'),(17,'Makueni'),(18,'Nyandarua'),(19,'Nyeri'),(20,'Kirinyaga'),
        (21,'Murang\'a'),(22,'Kiambu'),(23,'Turkana'),(24,'West Pokot'),(25,'Samburu'),(26,'Trans Nzoia'),(27,'Uasin Gishu'),
        (28,'Elgeyo/Marakwet'),(29,'Nandi'),(30,'Baringo'),(31,'Laikipia'),(32,'Nakuru'),(33,'Narok'),(34,'Kajiado'),
        (35,'Kericho'),(36,'Bomet'),(37,'Kakamega'),(38,'Vihiga'),(39,'Bungoma'),(40,'Busia'),
        (41,'Siaya'),(42,'Kisumu'),(43,'Homa Bay'),(44,'Migori'),(45,'Kisii'),(46,'Nyamira'),(47,'Nairobi City')
        )
    first_name = models.CharField(max_length=30, null=False,blank=False)
    last_name = models.CharField(max_length=30,null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    date_of_birth = models.DateField(null=False, blank=False)
    county = models.CharField(max_length=30 ,choices=KEN_COUNTIES)

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)


#class Editors(AbstractUser):
 #   username = models.CharField(max_length =30)

  #  def __init__(self):
   #     return self.username
        


