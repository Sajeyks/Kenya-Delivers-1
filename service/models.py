from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime

from django.utils.safestring import mark_safe
# for media cleanup
from django.db.models.signals import post_delete
from django.dispatch import receiver

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
        date_of_birth = models.DateField(null=True, blank=True)
        county = models.CharField(max_length=30 ,choices=KEN_COUNTIES)

        def __init__(self, *args, **kwargs):
            super().__init__(*args,**kwargs)


class agencyCategory(models.Model):
        agency_logo = models.CharField(max_length=50,null=False, blank=False)
        agency_Category = models.CharField(max_length=50, null=False,blank=False)
        category_Summary = models.TextField(max_length=200)

        def  __str__(self):
                return  self.agency_Category

        class  Meta:
            verbose_name_plural  =  "Categories"


class Agency(models.Model):
        agency_Title = models.CharField(max_length=50, null=False,blank=False)
        agency_Description = models.TextField()
        agency_Link = models.URLField(null=False, blank=False)
        agency_Cover = models.ImageField(upload_to='images/')
        agency_Added = models.DateTimeField(auto_now_add=True)
        agency_Category = models.ForeignKey(agencyCategory,default=1,verbose_name="Category",on_delete=models.SET_DEFAULT)

        def  image_tag(self):
            return mark_safe('<img src="/../../media/%s" width="150" height="150" />' % (self.agency_Cover))
    
        
        image_tag.allow_tags = True


        def  __str__(self):
            return  self.agency_Title

        class  Meta:
            verbose_name_plural  =  "Agencies"  
        
@receiver(post_delete,sender=Agency)
def submission_del(sender,instance,**kwargs):
    instance.Cover.delete(False)        
    


