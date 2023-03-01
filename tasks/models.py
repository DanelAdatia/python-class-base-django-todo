from django.db import models
from django.utils import timezone


# Create your models here.
 
CATEGORIES = (
        ("default","Default"),
        ("personal","Personal"),
        ("shopping","Shopping"),
        ("wishlist","Wishlist"),
        ("work","Work")
    )
class TaskItem(models.Model):
   
    title = models.CharField(max_length=100)
    body =models.TextField(null= True,blank=True)
    due_date = models.DateField(default= timezone.now)
    task_finished = models.BooleanField(default= True)
    category = models. CharField(max_length= 20, choices= CATEGORIES , default= "default")

    def __str__(self):
        return f'{self.title}'