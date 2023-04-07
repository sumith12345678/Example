from django.db import models




    
    
class Book(models.Model):
    CATEGORY = (
        ('FICTION', 'FICTION'),
        ('SCIFI', 'SCIFI'),
        ('ENGINEERING', 'ENGINEERING'),
      
        
       
           
    )
    Book_name = models.CharField(max_length=250, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    image = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, null=True)
    Author=models.CharField(max_length=250, null=True)
    status=models.BooleanField(default=False)
    
    
  
        
    def __str__(self):
        return self.Book_name


# class NewPost(models.Model):
#     name=models.ForeignKey(Book,on_delete=models.CASCADE)
#     upload_photo=models.ImageField(upload_to='uploads/')
#     Author=models.CharField(max_length=250)
#     price = models.FloatField(null=True)
#     def __str__(self):
#         return self.Book_name
# Create your models here.
