from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
  
    @staticmethod
    def get_all_categories():
        return Category.objects.all()
  
    def __str__(self):
        return self.name

  
  
class Gig(models.Model):
    profile = models.ForeignKey("users.Profile", on_delete=models.CASCADE, related_name="gigs")
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/gig/')
  
    @staticmethod
    def get_gig_by_id(ids):
        return Gig.objects.filter(id__in=ids)
  
    @staticmethod
    def get_all_gig():
        return Gig.objects.all()
  
    @staticmethod
    def get_all_gig_by_categoryid(category_id):
        if category_id:
            return Gig.objects.filter(category=category_id)
        else:
            return Gig.get_all_gig()